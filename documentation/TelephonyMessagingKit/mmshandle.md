# MMSHandle

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that represents an MMS address.

**Availability**:
- iOS 26.0+

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

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var from: MMSHandle?](mmscontent/from.md)
  The sender of the MMS message.
- [var recipients: [MMSHandle]](mmscontent/recipients.md)
  The recipients of the MMS message, as an array of MMS handles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmshandle)*