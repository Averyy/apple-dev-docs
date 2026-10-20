# pushRegistry(_:didInvalidatePushTokenFor:)

**Framework**: PushKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) pushRegistry:(PKPushRegistry *) registry didInvalidatePushTokenForType:(PKPushType) type;
```

#### Discussion

The system calls this method when a previously provided push token is no longer valid for use. No action is necessary on your part to reregister the push type. Instead, use this method to notify your server not to send push notifications using the matching push token.

## Parameters

- `registry`: The [`PKPushRegistry`](../pkpushregistry.md) instance responsible for the delegate callback.
- `type`: This is a [`PKPushType`](../pkpushtype.md) constant, which is present in `[registry desiredPushTypes]`.

## See Also

### Responding to Registration Events
- [func pushRegistry(PKPushRegistry, didUpdate: PKPushCredentials, for: PKPushType)](./pushregistry%28_,didupdate,for%29.md)
  Tells the delegate that the system updated the credentials for the specified type of push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/pushregistry(_:didinvalidatepushtokenfor:))*