# pushRegistry(_:didReceiveIncomingPushWith:for:completion:)

**Framework**: PushKit  
**Kind**: method

Tells the delegate that a remote push notification arrived.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, for type: PKPushType) async
```

## Mentions

- [Responding to VoIP Notifications from PushKit](responding-to-voip-notifications-from-pushkit.md)

#### Discussion

> **Note**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, for type: PKPushType) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, for type: PKPushType) async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The system calls this method when it receives a push notification for the specified push type. Use this method to extract data from the notification’s payload and to perform the relevant task for that data. For example, use this method to update the complication data of your watchOS app. When you finish the task, execute the provided `completion` handler block to let PushKit know you are finished.

When linking against the iOS 13 SDK or later, your implementation of this method must report notifications of type [`voIP`](pkpushtype/voip.md) to the [`CallKit`](https://developer.apple.com/documentation/CallKit) framework by calling the [`reportNewIncomingCall(with:update:completion:)`](https://developer.apple.com/documentation/CallKit/CXProvider/reportNewIncomingCall(with:update:completion:)) method of your app’s `CXProvider` object. When you call that method, the system displays the standard incoming call interface to the user unless an error occurs. For example, the system reports an error if the user enabled Do Not Disturb. You may establish a connection to your VoIP server in tandem with notify CallKit.

> ❗ **Important**: On iOS 13.0 and later, if you fail to report a call to CallKit, the system will terminate your app. Repeatedly failing to report calls may cause the system to stop delivering any more VoIP push notifications to your app. If you want to initiate a VoIP call without using CallKit, register for push notifications using the User Notifications framework instead of PushKit. For more information, see [`User Notifications`](https://developer.apple.com/documentation/UserNotifications).

On iOS 13.0 and later, if you fail to report a call to CallKit, the system will terminate your app. Repeatedly failing to report calls may cause the system to stop delivering any more VoIP push notifications to your app. If you want to initiate a VoIP call without using CallKit, register for push notifications using the User Notifications framework instead of PushKit. For more information, see [`User Notifications`](https://developer.apple.com/documentation/UserNotifications).

## Parameters

- `registry`: The   instance responsible for the delegate callback.
- `payload`: The push payload sent by a developer via APNs server API.
- `type`: This is a   constant, which is present in  .
- `completion`: The notification’s completion handler. Execute this block when you finish processing the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/pushregistry(_:didreceiveincomingpushwith:for:completion:))*