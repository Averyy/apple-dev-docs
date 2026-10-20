# post(_:subject:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Posts a given asynchronous message to the notification center.

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
func post<Message>(_ message: Message, subject: Message.Subject) where Message : NotificationCenter.AsyncMessage, Message.Subject : AnyObject
```

## Parameters

- `message`: The message to post.
- `subject`: The subject instance that corresponds to the message.

## See Also

### Posting notification messages
- [func post<Message>(Message, subject: Message.Subject)](./post%28_,subject%29-87dbk.md)
  Posts a given main actor message to the notification center.
- [func post<Message>(Message)](./post%28_%29-19s7b.md)
  Posts a given main actor message to the notification center.
- [func post<Message>(Message)](./post%28_%29-7ia4j.md)
  Posts a given asynchronous message to the notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/post(_:subject:)-5271w)*