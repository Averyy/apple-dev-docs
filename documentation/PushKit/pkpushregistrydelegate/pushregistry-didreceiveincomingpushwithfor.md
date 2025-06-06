# pushRegistry(_:didReceiveIncomingPushWith:for:)

**Framework**: PushKit  
**Kind**: method

Notifies the delegate that a remote push has been received.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
optional func pushRegistry(_ registry: PKPushRegistry, didReceiveIncomingPushWith payload: PKPushPayload, for type: PKPushType)
```

#### Discussion

This method is invoked when a push notification has been received for the specified push type.

## Parameters

- `registry`: The   instance responsible for the delegate callback.
- `payload`: The push payload sent by a developer via APNS server API.
- `type`: This is a   constant, which is present in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/pushregistry(_:didreceiveincomingpushwith:for:))*