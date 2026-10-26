# ILMessageCommunication

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

A concrete subclass representing a SMS message.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILMessageCommunication
```

```objc
@interface ILMessageCommunication : ILCommunication
```

## Topics

### Accessing Data
- [var messageBody: String?](./ilmessagecommunication/messagebody.md)
  The content of the SMS message.
### Comparing Communications
- [- isEqualToMessageCommunication:](./ilmessagecommunication/isequaltomessagecommunication_.md)
  Indicates whether the current message is equal to the provided argument.

## Relationships

### Inherits From
- [ILCommunication](./ilcommunication.md)
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
- [class ILCommunication](./ilcommunication.md)
  An abstract superclass representing a message or call to the user.
- [class ILCallCommunication](./ilcallcommunication.md)
  A concrete subclass representing a  phone call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagecommunication)*