# NEAppPushProvider

**Framework**: Network Extension  
**Kind**: class

An object that creates and maintains a persistent network connection to a local push server.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class NEAppPushProvider
```

## Mentions

- [Maintaining a Reliable Network Connection](maintaining-a-reliable-network-connection.md)

#### Overview

Subclass [`NEAppPushProvider`](neapppushprovider.md) to provide the connection to your local push server. A [`NEAppPushManager`](neapppushmanager.md) creates instances of your provider class based on the [`providerBundleIdentifier`](neapppushmanager/providerbundleidentifier.md) in the manager’s configuration. The manager then calls methods on your provider to start and stop communication with the server, and periodically check the provider’s status. When your provider receives an incoming call from your server, call the provider’s [`reportIncomingCall(userInfo:)`](neapppushprovider/reportincomingcall(userinfo:).md) method to alert the manager’s [`delegate`](neapppushmanager/delegate.md).

##### Creating a Local Push Provider Extension

Local Push Providers run as App Extensions for the `app-push-provider` extension point, which is a possible value the [`Network Extensions Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.networkextension).

To create a Local Push Provider extension, first create a new App Extension target in your project.

For an example of an Xcode build target for this app extension, see the [`Receiving Voice and Text Communications on a Local Network`](receiving-voice-and-text-communications-on-a-local-network.md) sample code project.

Once you have an extension target, create a subclass of [`NEAppPushProvider`](neapppushprovider.md). Then set the `NSExtensionPrincipalClass` key in the extension’s `Info.plist` to the name of your subclass. Set the `NSExtensionPointIdentifier` key in the extension’s `Info.plist` to `com.apple.networkextension.app-push`, if it’s not set already.

Here’s an example of the `NSExtension` dictionary in a Local Push Provider extension’s `Info.plist`:

```xml
<key>NSExtension</key>
<dict>
    <key>NSExtensionPointIdentifier</key>
    <string>com.apple.networkextension.app-push</string>
    <key>NSExtensionPrincipalClass</key>
    <string>$(PRODUCT_MODULE_NAME).MyPushProvider</string>
</dict>

```

Finally, add your Local Push Provider extension target to your app’s Embed App Extensions build phase.

## Topics

### Inspecting provider properties
- [var providerConfiguration: [String : Any]?](neapppushprovider/providerconfiguration.md)
  A dictionary that contains current vendor-specific configuration parameters.
### Implementing provider life cycle
- [func start()](neapppushprovider/start.md)
  Indicates that the framework has started the provider.
- [func start(completionHandler: ((any Error)?) -> Void)](neapppushprovider/start(completionhandler:).md)
  Indicates that the framework has started the provider, and provides a completion handler for subclasses to signal their readiness.
- [func stop(with: NEProviderStopReason, completionHandler: () -> Void)](neapppushprovider/stop(with:completionhandler:).md)
  Indicates that the framework needs to stop the provider.
- [func handleTimerEvent()](neapppushprovider/handletimerevent.md)
  Indicates a periodic status check from the framework to the provider.
### Receiving local events
- [func reportIncomingCall(userInfo: [AnyHashable : Any])](neapppushprovider/reportincomingcall(userinfo:).md)
  Informs the manager about an incoming call.
- [func reportPushToTalkMessage(userInfo: [AnyHashable : Any])](neapppushprovider/reportpushtotalkmessage(userinfo:).md)
  Informs the manager about a push-to-talk message on the connection.
### Instance Methods
- [func unmatchEthernet()](neapppushprovider/unmatchethernet.md)

## Relationships

### Inherits From
- [NEProvider](neprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEAppPushManager](neapppushmanager.md)
  An object that configures a push provider and manages its life cycle.
- [Maintaining a Reliable Network Connection](maintaining-a-reliable-network-connection.md)
  Implement your Local Push Connectivity app to ensure delivery of notifications.
- [Receiving Voice and Text Communications on a Local Network](receiving-voice-and-text-communications-on-a-local-network.md)
  Provide voice and text communication on a local network isolated from Apple Push Notification service by adopting Local Push Connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushprovider)*