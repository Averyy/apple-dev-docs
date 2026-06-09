# sizeLimitExceeded

**Framework**: Foundation  
**Kind**: property

An identifier for a message about a user defaults database exceeding its maximum size.

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
static var sizeLimitExceeded: NotificationCenter.BaseMessageIdentifier<UserDefaults.SizeLimitExceededMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`UserDefaults.SizeLimitExceededMessage`](userdefaults/sizelimitexceededmessage.md).

## See Also

- [static var didChange: NotificationCenter.BaseMessageIdentifier<UserDefaults.DidChangeMessage>](notificationcenter/messageidentifier/didchange-187tw.md)
  An identifier for a message about a change in a user defaults setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/sizelimitexceeded)*