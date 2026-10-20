# MMSHandle

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that represents an MMS address.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct MMSHandle
```

## Topics

### Creating a handle
- [init(phoneNumber: String)](./mmshandle/init%28phonenumber%29.md)
  Initializes a handle instance with the given phone number.
### Accessing handle properties
- [var phoneNumber: String](./mmshandle/phonenumber.md)
  The phone number for the handle.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing message participants
- [var from: MMSHandle?](./mmscontent/from.md)
  The sender of the MMS message.
- [var recipients: [MMSHandle]](./mmscontent/recipients.md)
  The recipients of the MMS message, as an array of MMS handles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmshandle)*