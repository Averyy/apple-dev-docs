# ILClassificationRequest

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

The abstract superclass for classification requests.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILClassificationRequest
```

```objc
@interface ILClassificationRequest : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./ilclassificationrequest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [ILCallClassificationRequest](./ilcallclassificationrequest.md)
- [ILMessageClassificationRequest](./ilmessageclassificationrequest.md)
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
- [class ILMessageClassificationRequest](./ilmessageclassificationrequest.md)
  A classification request for SMS messages.
- [class ILCallClassificationRequest](./ilcallclassificationrequest.md)
  A classification request for phone calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationrequest)*