# headerPosition

**Framework**: Retention Messaging API  
**Kind**: typealias

The position where the header text appears in a message.

**Availability**:
- Retention Messaging API 1.4+

## Declaration

```swift
string headerPosition
```

## Mentions

- [Retention Messaging API changelog](retention-messaging-changelog.md)

#### Discussion

The `headerPosition` defaults to `ABOVE_BODY`. Include it in your request if you want the header to appear above the image instead.

## See Also

- [type messageIdentifier](messageidentifier.md)
  A unique identifier for a message, which you provide when you upload the message.
- [type messageState](messagestate.md)
  The approval state of the message.
- [type body](body.md)
  The body text you provide for a message.
- [object BulletPoint](bulletpoint.md)
  The text and its bullet-point image to include in a retention message’s bulleted list.
- [type bulletPointText](bulletpointtext.md)
  The text you provide for an individual bullet-list item.
- [type header](header.md)
  The header text you provide that appears above the body text in a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/headerposition)*