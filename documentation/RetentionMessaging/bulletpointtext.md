# bulletPointText

**Framework**: Retention Messaging API  
**Kind**: typealias  
**Role**: Type

The text you provide for an individual bullet-list item.

**Availability**:
- Retention Messaging API 1.4+

## Declaration

```
string bulletPointText
```

## Mentions

- [Retention Messaging API changelog](./retention-messaging-changelog.md)



**Maximum Length**: `66`

## Discussion

Provide the `bulletPointText` as a UTF-8-encoded string with a maximum length of 66 characters.

This text is one element of a [`BulletPoint`](./bulletpoint.md).

> **Note**: Use only allowed Unicode characters in the string. If it contains a disallowed character, [`Upload Message`](./upload-message.md) returns a [`BadRequestInvalidTextFieldError`](./badrequestinvalidtextfielderror.md).

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
- [type header](./header.md)
  The header text you provide that appears above the body text in a message.
- [type headerPosition](./headerposition.md)
  The position where the header text appears in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/bulletpointtext)*