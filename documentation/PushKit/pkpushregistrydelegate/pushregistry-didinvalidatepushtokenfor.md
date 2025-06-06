# pushRegistry(_:didInvalidatePushTokenFor:)

**Framework**: PushKit  
**Kind**: method

Tells the delegate that the system invalidated the push token for the specified type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func pushRegistry(_ registry: PKPushRegistry, didInvalidatePushTokenFor type: PKPushType)
```

#### Discussion

The system calls this method when a previously provided push token is no longer valid for use. No action is necessary on your part to reregister the push type. Instead, use this method to notify your server not to send push notifications using the matching push token.

## Parameters

- `registry`: The   instance responsible for the delegate callback.
- `type`: This is a   constant, which is present in  .

## See Also

- [func pushRegistry(PKPushRegistry, didUpdate: PKPushCredentials, for: PKPushType)](pkpushregistrydelegate/pushregistry(_:didupdate:for:).md)
  Tells the delegate that the system updated the credentials for the specified type of push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/pushregistry(_:didinvalidatepushtokenfor:))*