# Using push notifications to signal changes

**Framework**: File Provider

Send push notifications to a device to signal changes from your server.

#### Overview

You can signal changes by sending push notifications from a remote server, using the [`PushKit`](https://developer.apple.com/documentation/PushKit) framework and the [`fileProvider`](https://developer.apple.com/documentation/PushKit/PKPushType/fileProvider) push type. When the system receives the notification, it automatically calls the [`signalEnumerator(for:completionHandler:)`](nsfileprovidermanager/signalenumerator(for:completionhandler:).md) method with the specified identifier. It also delivers the notification to any [`PKPushRegistryDelegate`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate) objects.

To use push notifications, you start by generating the signing key for your app. Next, you configure your app to receive push notifications. Finally, you send the notifications from your server. The following sections describe each step.

> ❗ **Important**:  Avoid sending unnecessary push notifications. If you send too many, Apple Push Notification service (APNs) throttles your requests. For open files and directories, try to send push notifications only when your File Provider extension has an active enumerator for that item. This means your extension must update your server whenever an enumerator is created or invalidated. Additionally, this coordination must gracefully degrade when an internet connection is unavailable or fails. For items in the working set, the server should always send push notifications.

##### Generate the Signing Key

To signal changes from a remote server, you use provider authentication tokens (not provider certificates). To create an APNs key for your app, see [`Communicate with APNs using authentication tokens`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev54d690a66). Use the APNs key to sign your JSON Web Tokens (JWT) when sending notifications from your server.

##### Enable and Register for Push Notifications

To receive notifications, you first enable push notifications in your app. You can register to receive push notifications in either your app delegate or in your file provider extension. Finally, you send the device token to your server.

First, enable push notifications in your iOS app (not your File Provider extension). For details, see [`Communicate with APNs using authentication tokens`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devdfd3d04a1).

1. Open the Capabilities pane for your app target.
2. Turn on push notifications.

Then, register for push notifications. You can register in your app delegate, your File Provider extension, or both.

> **Note**:  If you only register for push notifications in your app delegate and the device token changes, your app won’t receive notifications until someone launches the app. Registering in the File Provider extension means your app can update the device token the next time anyone interacts with the File Provider extension’s content.

In your `AppDelegate` or `FileProviderExtension` classes, adopt the [`PKPushRegistryDelegate`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate) protocol.

```swift
import PushKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, PKPushRegistryDelegate {
    // ...
}
```

```swift
import PushKit

class FileProviderExtension: NSFileProviderExtension, PKPushRegistryDelegate {
    // ...
}
```

Also, create a `pushRegistry` instance variable in each class.

```swift
var pushRegistry: PKPushRegistry!
```

In your AppDelegate class’s [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)) method, register for push notifications.

```swift
func application(
    _ application: UIApplication, 
    didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?
) -> Bool {
    pushRegistry = PKPushRegistry(queue: nil)
    pushRegistry.delegate = self
    pushRegistry.desiredPushTypes = [.fileProvider]
    return true
}
```

Similarly, in your FileProvider class’s `init()` method, register for push notifications.

```swift
override init() {
    super.init()
    pushRegistry = PKPushRegistry(queue: nil)
    pushRegistry.delegate = self
    pushRegistry.desiredPushTypes = [.fileProvider]
}
```

Finally, implement the [`pushRegistry(_:didUpdate:for:)`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate/pushRegistry(_:didUpdate:for:)) delegate method in both your `AppDelegate` and `FileProvider` classes. The [`pushRegistry(_:didInvalidatePushTokenFor:)`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate/pushRegistry(_:didInvalidatePushTokenFor:)) method is optional.

> **Note**:  The [`pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate/pushRegistry(_:didReceiveIncomingPushWith:for:completion:)) method is never called for [`fileProvider`](https://developer.apple.com/documentation/PushKit/PKPushType/fileProvider) type pushes. These notifications are automatically handled by the system instead.

In both your `AppDelegate` and `FileProvider` classes’ [`pushRegistry(_:didUpdate:for:)`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate/pushRegistry(_:didUpdate:for:)) methods, when you receive a [`PKPushCredentials`](https://developer.apple.com/documentation/PushKit/PKPushCredentials) instance, extract the value of its [`token`](https://developer.apple.com/documentation/PushKit/PKPushCredentials/token) property, and send it to your server. This value is an app-specific device token. Your server uses the device token to request push notifications for this device.

```swift
func pushRegistry(
    _ registry: PKPushRegistry, 
    didUpdate credentials: PKPushCredentials, 
    forType type: PKPushType
) {
    let deviceToken = credentials.token
    // Send the device token to your server here.
}
```

##### Send Push Notifications

You’re now ready to send a push notification. Start by creating a JWT; for details, see [`Provider Authentication Tokens`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html#//apple_ref/doc/uid/TP40008194-CH11-SW3). You can reuse the JWT as long as it remains valid.

Then send a POST request to the APNs server with the following values:

- The `:path` value is `/3/device/<device-token>`. This token is the device token you sent to your server from your [`pushRegistry(_:didUpdate:for:)`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate/pushRegistry(_:didUpdate:for:)) method.
- The `authorization` value is `bearer <provider token>`. This token is your JWT.
- The `apns-topic` value is `<bundle identifier>.pushkit.fileprovider`. The bundle identifier is your app’s bundle identifier.

The POST request’s content is a JSON dictionary that specifies the container and domain for the updated content. Set the container identifier to the unique string used in the container’s [`itemIdentifier`](nsfileprovideritemprotocol/itemidentifier.md) property. You can also use `NSFileProviderRootContainerItemIdentifier` to update the root container, or `NSFileProviderWorkingSetContainerItemIdentifier` to update the working set.

> **Note**:  When using an [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md), always set the container identifier to `NSFileProviderWorkingSetContainerItemIdentifier`. The system automatically propagates any working set changes to the user interface, without requiring you to signal individual containers. It ignores any other identifiers.

Set the domain identifier to the unique string used in the domain’s [`identifier`](nsfileproviderdomain/identifier.md) property.

```swift
 {
     "container-identifier": "<your-container-identifier>"
     "domain": "<your-domain-identifier>"
 }

```

For more information, see [`APNs Notification API`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html#//apple_ref/doc/uid/TP40008194-CH11-SW10).


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/using-push-notifications-to-signal-changes)*