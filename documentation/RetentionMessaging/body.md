# body

**Framework**: Retention Messaging API  
**Kind**: typealias  
**Role**: Type

The main text you provide for a retention message.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```
string body
```



**Maximum Length**: `144`

## Discussion

Provide the `body` as a UTF-8-encoded string with a maximum length of 144 characters.

> **Note**: Use only allowed Unicode characters in the string. If it contains a disallowed character, [`Upload Message`](./upload-message.md) returns a [`BadRequestInvalidTextFieldError`](./badrequestinvalidtextfielderror.md).

The `body` text appears, along with the [`header`](./header.md) text, in a [`message`](./message.md).

## See Also

### Messages
- [type messageIdentifier](./messageidentifier.md)
  A unique identifier for a message, which you provide when you upload the message.
- [type messageState](./messagestate.md)
  The approval state of the message.
- [object BulletPoint](./bulletpoint.md)
  The text and its bullet-point image to include in a retention message’s bulleted list.
- [type bulletPointText](./bulletpointtext.md)
  The text you provide for an individual bullet-list item.
- [type header](./header.md)
  The header text you provide that appears above the body text in a message.
- [type headerPosition](./headerposition.md)
  The position where the header text appears in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/body)*