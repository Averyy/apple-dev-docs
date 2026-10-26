# ILMessageFilterCapabilitiesQueryResponse

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

A response to a message filter capabilities query request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class ILMessageFilterCapabilitiesQueryResponse
```

```objc
@interface ILMessageFilterCapabilitiesQueryResponse : NSObject
```

## Topics

### Setting the Subactions
- [var promotionalSubActions: [ILMessageFilterSubAction]](./ilmessagefiltercapabilitiesqueryresponse/promotionalsubactions-98kzj.md)
- [var transactionalSubActions: [ILMessageFilterSubAction]](./ilmessagefiltercapabilitiesqueryresponse/transactionalsubactions-4bfqz.md)
- [promotionalSubActions](./ilmessagefiltercapabilitiesqueryresponse/promotionalsubactions-5d9c5.md)
  The promotional action the Message Filter app extension recommends that the system perform on the queried message.
- [transactionalSubActions](./ilmessagefiltercapabilitiesqueryresponse/transactionalsubactions-5fmpl.md)
  The transactional action the Message Filter app extension recommends that the system perform on the queried message.
### Initializers
- [init?(coder: NSCoder)](./ilmessagefiltercapabilitiesqueryresponse/init%28coder%29.md)

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

### Responses
- [enum ILMessageFilterSubAction](./ilmessagefiltersubaction.md)
  Responds to a received message with a filter subaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltercapabilitiesqueryresponse)*