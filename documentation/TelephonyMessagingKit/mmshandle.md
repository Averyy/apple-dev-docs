# MMSHandle

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an MMS address.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct MMSHandle
```

## Topics

### Creating a handle
- [init(phoneNumber: String)](mmshandle/init(phonenumber:).md)
  Initializes a handle instance with the given phone number.
### Accessing handle properties
- [var phoneNumber: String](mmshandle/phonenumber.md)
  The phone number for the handle.
### Encoding and decoding
- [init(from: any Decoder) throws](mmshandle/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](mmshandle/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var from: MMSHandle?](mmscontent/from.md)
  The sender of the MMS message.
- [var recipients: [MMSHandle]](mmscontent/recipients.md)
  The recipients of the MMS message, as an array of MMS handles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmshandle)*