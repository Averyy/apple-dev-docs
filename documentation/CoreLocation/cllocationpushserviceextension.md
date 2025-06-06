# CLLocationPushServiceExtension

**Framework**: Core Location  
**Kind**: protocol

The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
protocol CLLocationPushServiceExtension : NSObjectProtocol
```

## Mentions

- [Creating a location push service extension](creating-a-location-push-service-extension.md)

#### Overview

A type that adopts the [`CLLocationPushServiceExtension`](cllocationpushserviceextension.md) protocol acts as the entry point to a Location Push Service Extension. You use this type to respond to incoming location push notifications and perform app-specific tasks. For example, you use it to get someone’s current location and send it to your server.

Don’t adopt this protocol in your own custom types. Instead, add a Location Push Service Extension target to your project and modify the type that Xcode provides. To start the delivery of location push notifications, call the [`startMonitoringLocationPushes(completion:)`](cllocationmanager/startmonitoringlocationpushes(completion:).md) method to request a unique token from the device. Send that token to your server and use it to generate HTTP requests for APNs to deliver to the device.

When the device receives a location push notification that your server generated, the system loads your app extension and calls its [`didReceiveLocationPushPayload(_:completion:)`](cllocationpushserviceextension/didreceivelocationpushpayload(_:completion:).md) method. Use that method to configure a [`CLLocationManager`](cllocationmanager.md) object and request the person’s current location. Collect the location, encrypt it, and send it back to your server using a custom connection.

> ❗ **Important**:  In order for your app extension to receive push notifications, the app that contains the app extension must have Always authorization for location services. For information about how to request this access, see [`Requesting authorization to use location services`](requesting-authorization-to-use-location-services.md).

 In order for your app extension to receive push notifications, the app that contains the app extension must have Always authorization for location services. For information about how to request this access, see [`Requesting authorization to use location services`](requesting-authorization-to-use-location-services.md).

Location Push Service Extensions aren’t supported in visionOS. If a compatible iPad or iPhone app contains an app extension of this type, the system doesn’t load it.

For more information about adding the extension to your app, see [`Creating a location push service extension`](creating-a-location-push-service-extension.md). For information about how to generate push notifications from your server, see [`Setting up a remote notification server`](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server).

## Topics

### Getting the push notification payload
- [func didReceiveLocationPushPayload([String : Any], completion: () -> Void)](cllocationpushserviceextension/didreceivelocationpushpayload(_:completion:).md)
  Delivers a location push notification for your app extension to process.
### Handling the extension termination
- [func serviceExtensionWillTerminate()](cllocationpushserviceextension/serviceextensionwillterminate.md)
  Notifies your app extension that the system is about to terminate the extension because it’s taking too long to complete its task.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [com.apple.developer.location.push](../BundleResources/Entitlements/com.apple.developer.location.push.md)
  An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [struct CLLocationPushServiceError](cllocationpushserviceerror-swift.struct.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.
- [let CLLocationPushServiceErrorDomain: String](cllocationpushserviceerrordomain.md)
  The domain for Location Push Service Extension errors.
- [CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceextension)*