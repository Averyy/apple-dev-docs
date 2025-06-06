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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ILCallCommunication](ilcallcommunication.md)
- [ILMessageCommunication](ilmessagecommunication.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class ILMessageCommunication](ilmessagecommunication.md)
  A concrete subclass representing a SMS message.
- [class ILCallCommunication](ilcallcommunication.md)
  A concrete subclass representing a  phone call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilcommunication)*