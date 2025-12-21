# post(_:)

**Framework**: Foundation  
**Kind**: method

Posts a given main actor message to the notification center.

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
@MainActor
func post<Message>(_ message: Message) where Message : NotificationCenter.MainActorMessage
```

## Parameters

- `message`: The message to post.

## See Also

- [func post<Message>(Message, subject: Message.Subject)](notificationcenter/post(_:subject:)-87dbk.md)
  Posts a given main actor message to the notification center.
- [func post<Message>(Message, subject: Message.Subject)](notificationcenter/post(_:subject:)-5271w.md)
  Posts a given asynchronous message to the notification center.
- [func post<Message>(Message)](notificationcenter/post(_:)-7ia4j.md)
  Posts a given asynchronous message to the notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/post(_:)-19s7b)*