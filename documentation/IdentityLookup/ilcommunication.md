# ILCommunication

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

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

```objc
@interface ILCommunication : NSObject
```

## Topics

### Accessing Data
- [var sender: String?](./ilcommunication/sender.md)
  The email address or phone number of the sender.
- [var dateReceived: Date](./ilcommunication/datereceived.md)
  The date and time when the system received the message.
### Initializers
- [init?(coder: NSCoder)](./ilcommunication/init%28coder%29.md)
### Comparing Communications
- [- isEqualToCommunication:](./ilcommunication/isequaltocommunication_.md)
  Indicates whether the current communication is equal to the provided argument.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [ILCallCommunication](./ilcallcommunication.md)
- [ILMessageCommunication](./ilmessagecommunication.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Communications
- [class ILMessageCommunication](./ilmessagecommunication.md)
  A concrete subclass representing a SMS message.
- [class ILCallCommunication](./ilcallcommunication.md)
  A concrete subclass representing a  phone call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilcommunication)*