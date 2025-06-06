# token

**Framework**: PushKit  
**Kind**: property

A unique device token to use when sending push notifications to the current device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var token: Data { get }
```

#### Discussion

Forward this token to the server you use to generate push notifications. When preparing to deliver a push notification to the current device, include the token in the HTTP request you send to Apple Push Notification service (APNs).

## See Also

- [var type: PKPushType](pkpushcredentials/type.md)
  The push type constant associated with the token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushcredentials/token)*