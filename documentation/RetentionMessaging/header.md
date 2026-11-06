# header

**Framework**: Retention Messaging API  
**Kind**: typealias  
**Role**: Type

The header text you provide that appears above the body text in a message.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```
string header
```



**Maximum Length**: `66`

## Discussion

Provide the `header` as a UTF-8-encoded string with a maximum length of 66 characters.

The header text appears above the [`body`](./body.md) text in a [`message`](./message.md). If the message includes an image, the header text appears below the image by default, or above it when you set [`headerPosition`](./headerposition.md) to `ABOVE_IMAGE`.

> **Note**: Use only allowed Unicode characters in the header text. If it contains a disallowed character, [`Upload Message`](./upload-message.md) returns a [`BadRequestInvalidTextFieldError`](./badrequestinvalidtextfielderror.md).

## See Also

### Messages
- [type messageIdentifier](./messageidentifier.md)
  A unique identifier for a message, which you provide when you upload the message.
- [type messageState](./messagestate.md)
  The approval state of the message.
- [type body](./body.md)
  The main text you provide for a retention message.
- [object BulletPoint](./bulletpoint.md)
  The text and its bullet-point image to include in a retention message’s bulleted list.
- [type bulletPointText](./bulletpointtext.md)
  The text you provide for an individual bullet-list item.
- [type headerPosition](./headerposition.md)
  The position where the header text appears in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/header)*