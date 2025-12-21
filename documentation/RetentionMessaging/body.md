# body

**Framework**: Retention Messaging API  
**Kind**: typealias

The body text you provide for a message.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
string body
```

#### Discussion

Provide the `body` as a UTF-8-encoded string. The maximum string length is `144`.

The `body` text appears, along with the [`header`](header.md) text, in a [`message`](message.md).

## See Also

- [type messageIdentifier](messageidentifier.md)
  A unique identifier for a message, which you provide when you upload the message.
- [type messageState](messagestate.md)
  The approval state of the message.
- [type header](header.md)
  The header text you provide for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/body)*