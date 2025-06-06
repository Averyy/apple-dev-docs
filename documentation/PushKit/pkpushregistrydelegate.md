# PKPushRegistryDelegate

**Framework**: PushKit  
**Kind**: protocol

The methods that you use to handle incoming PushKit notifications and registration events.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol PKPushRegistryDelegate : NSObjectProtocol
```

#### Overview

Implement the methods of this protocol in an object of your app and assign that object to the [`delegate`](pkpushregistry/delegate.md) property of your `PKPushRegistry` object. Use the methods of this protocol to process incoming notifications and to react to token registration and invalidation.

## Topics

### Responding to Registration Events
- [func pushRegistry(PKPushRegistry, didUpdate: PKPushCredentials, for: PKPushType)](pkpushregistrydelegate/pushregistry(_:didupdate:for:).md)
  Tells the delegate that the system updated the credentials for the specified type of push notification.
- [func pushRegistry(PKPushRegistry, didInvalidatePushTokenFor: PKPushType)](pkpushregistrydelegate/pushregistry(_:didinvalidatepushtokenfor:).md)
  Tells the delegate that the system invalidated the push token for the specified type.
### Handling an Incoming Notification
- [func pushRegistry(PKPushRegistry, didReceiveIncomingPushWith: PKPushPayload, for: PKPushType, completion: () -> Void)](pkpushregistrydelegate/pushregistry(_:didreceiveincomingpushwith:for:completion:).md)
  Tells the delegate that a remote push notification arrived.
### Deprecated Methods
- [func pushRegistry(PKPushRegistry, didReceiveIncomingPushWith: PKPushPayload, for: PKPushType)](pkpushregistrydelegate/pushregistry(_:didreceiveincomingpushwith:for:).md)
  Notifies the delegate that a remote push has been received.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Supporting PushKit Notifications in Your App](supporting-pushkit-notifications-in-your-app.md)
  Declare the types of PushKit notifications your app supports and configure objects to respond to them.
- [class PKPushRegistry](pkpushregistry.md)
  An object that requests the delivery and handles the receipt of PushKit notifications.
- [class PKPushCredentials](pkpushcredentials.md)
  An object that encapsulates the device token you use to deliver push notifications to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate)*