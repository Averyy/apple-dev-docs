# ILMessageClassificationRequest

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

A classification request for SMS messages.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILMessageClassificationRequest
```

```objc
@interface ILMessageClassificationRequest : ILClassificationRequest
```

## Topics

### Accessing Messages
- [var messageCommunications: [ILMessageCommunication]](./ilmessageclassificationrequest/messagecommunications.md)
  The messages the user selected to report.

## Relationships

### Inherits From
- [ILClassificationRequest](./ilclassificationrequest.md)
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

### Requests
- [class ILClassificationRequest](./ilclassificationrequest.md)
  The abstract superclass for classification requests.
- [class ILCallClassificationRequest](./ilcallclassificationrequest.md)
  A classification request for phone calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessageclassificationrequest)*