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
- [object BulletPoint](bulletpoint.md)
  The text and its bullet-point image to include in a retention message’s bulleted list.
- [type bulletPointText](bulletpointtext.md)
  The text you provide for an individual bullet-list item.
- [type header](header.md)
  The header text you provide that appears above the body text in a message.
- [type headerPosition](headerposition.md)
  The position where the header text appears in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/body)*