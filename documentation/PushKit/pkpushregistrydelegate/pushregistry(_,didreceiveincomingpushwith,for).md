# pushRegistry(_:didReceiveIncomingPushWith:for:)

**Framework**: PushKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that a remote push has been received.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 8.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`](./pushregistry%28_,didreceiveincomingpushwith,for,completion%29.md) instead.

## Declaration

```swift
optional func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, for type: PKPushType)
```

```objc
- (void) pushRegistry:(PKPushRegistry *) registry didReceiveIncomingPushWithPayload:(PKPushPayload *) payload forType:(PKPushType) type;
```

## Discussion

This method is invoked when a push notification has been received for the specified push type.

## Parameters

- `registry`: The [`PKPushRegistry`](../pkpushregistry.md) instance responsible for the delegate callback.
- `payload`: The push payload sent by a developer via APNS server API.
- `type`: This is a [`PKPushType`](../pkpushtype.md) constant, which is present in `[registry desiredPushTypes]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/pushregistry(_:didreceiveincomingpushwith:for:))*