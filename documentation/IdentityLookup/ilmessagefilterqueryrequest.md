# ILMessageFilterQueryRequest

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

A request for a Message Filter app extension to determine the status of a message received from an unknown sender.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILMessageFilterQueryRequest
```

```objc
@interface ILMessageFilterQueryRequest : NSObject
```

## Topics

### Getting Information About a Message
- [var sender: String?](./ilmessagefilterqueryrequest/sender.md)
  The sender of the message.
- [var messageBody: String?](./ilmessagefilterqueryrequest/messagebody.md)
  The body of a message received from an unknown sender.
- [var receiverISOCountryCode: String?](./ilmessagefilterqueryrequest/receiverisocountrycode.md)
  The ISO Country Code of the receiving phone number, in format specified by the ISO 3166-2 standard.
### Initializers
- [init?(coder: NSCoder)](./ilmessagefilterqueryrequest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Queries
- [protocol ILMessageFilterQueryHandling](./ilmessagefilterqueryhandling.md)
  A set of methods implemented by a Message Filter app extension to handle query requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryrequest)*