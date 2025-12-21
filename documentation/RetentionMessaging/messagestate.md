# messageState

**Framework**: Retention Messaging API  
**Kind**: typealias

The approval state of the message.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
string messageState
```

## Mentions

- [Setting up retention messages](setting-up-retention-messages.md)

#### Discussion

Call [`Get Message List`](get-message-list.md) to get the list of messages and their current states.

For messages with images, see [`Get Image List`](get-image-list.md) to get the image state also.

## See Also

- [type messageIdentifier](messageidentifier.md)
  A unique identifier for a message, which you provide when you upload the message.
- [type body](body.md)
  The body text you provide for a message.
- [type header](header.md)
  The header text you provide for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/messagestate)*