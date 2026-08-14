# ILCommunication

**Framework**: SMS and Call Reporting  
**Kind**: class

An abstract superclass representing a message or call to the user.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILCommunication
```

## Topics

### Accessing Data
- [var sender: String?](ilcommunication/sender.md)
  The email address or phone number of the sender.
- [var dateReceived: Date](ilcommunication/datereceived.md)
  The date and time when the system received the message.
### Initializers
- [init?(coder: NSCoder)](ilcommunication/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [ILCallCommunication](ilcallcommunication.md)
- [ILMessageCommunication](ilmessagecommunication.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class ILMessageCommunication](ilmessagecommunication.md)
  A concrete subclass representing a SMS message.
- [class ILCallCommunication](ilcallcommunication.md)
  A concrete subclass representing a  phone call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilcommunication)*