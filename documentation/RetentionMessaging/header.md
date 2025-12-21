# header

**Framework**: Retention Messaging API  
**Kind**: typealias

The header text you provide for a message.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
string header
```

#### Discussion

Provide the `header` as a UTF-8-encoded string. The maximum string length is `66`.

The header text appears above the [`body`](body.md) text in a [`message`](message.md).

## See Also

- [type messageIdentifier](messageidentifier.md)
  A unique identifier for a message, which you provide when you upload the message.
- [type messageState](messagestate.md)
  The approval state of the message.
- [type body](body.md)
  The body text you provide for a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/header)*