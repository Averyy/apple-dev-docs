# didBecomeInvalid

**Framework**: Foundation  
**Kind**: property

An identifier for a message about a port becoming invalid.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var didBecomeInvalid: NotificationCenter.BaseMessageIdentifier<Port.DidBecomeInvalidMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`Port.DidBecomeInvalidMessage`](port/didbecomeinvalidmessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didbecomeinvalid)*