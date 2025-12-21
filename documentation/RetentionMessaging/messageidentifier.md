# messageIdentifier

**Framework**: Retention Messaging API  
**Kind**: typealias

A unique identifier for a message, which you provide when you upload the message.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
uuid messageIdentifier
```

#### Discussion

You create the UUID to identify a message when you call [`Upload Message`](upload-message.md). Use this identifier to refer to the same message throughout the API.

## See Also

- [type messageState](messagestate.md)
  The approval state of the message.
- [type body](body.md)
  The body text you provide for a message.
- [type header](header.md)
  The header text you provide for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/messageidentifier)*