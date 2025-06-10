# SMSContent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that holds the content of an SMS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct SMSContent
```

## Topics

### Creating SMS content
- [init(body: String)](smscontent/init(body:).md)
  Initializes a content instance with the given message body.
### Accessing content properties
- [let body: String](smscontent/body.md)
  The body of the SMS message.
### Encoding and decoding
- [init(from: any Decoder) throws](smscontent/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](smscontent/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let content: SMSContent](smsmessage/content.md)
  The textual content of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smscontent)*