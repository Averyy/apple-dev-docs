# MMSContent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that holds the content of an MMS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct MMSContent
```

#### Overview

You can use this structure when sending and receiving MMS messages.

## Topics

### Creating an MMS content instance
- [init()](mmscontent/init.md)
  Creates an empty MMS content instance.
- [init(parts: [MMSPartContent], recipients: [MMSHandle], subject: String?)](mmscontent/init(parts:recipients:subject:).md)
  Creates an MMS content instance with the provided values.
### Accessing content properties
- [var parts: [MMSPartContent]](mmscontent/parts.md)
  The individual parts of the MMS message.
- [struct MMSPartContent](mmspartcontent.md)
  A structure that defines custom headers within MMS content.
- [var subject: String?](mmscontent/subject.md)
  The subject of the MMS message.
- [var headers: [String : String]](mmscontent/headers.md)
  Additional headers in a received MMS message, as a key-value dictionary of strings.
### Accessing message participants
- [var from: MMSHandle?](mmscontent/from.md)
  The sender of the MMS message.
- [var recipients: [MMSHandle]](mmscontent/recipients.md)
  The recipients of the MMS message, as an array of MMS handles.
- [struct MMSHandle](mmshandle.md)
  A structure that represents an MMS address.
### Encoding and decoding
- [init(from: any Decoder) throws](mmscontent/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](mmscontent/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var content: MMSContent](mmsmessage/content.md)
  The body content of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmscontent)*