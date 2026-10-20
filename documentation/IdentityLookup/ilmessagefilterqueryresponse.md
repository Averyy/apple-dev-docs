# ILMessageFilterQueryResponse

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

A response to a message filter query request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILMessageFilterQueryResponse
```

```objc
@interface ILMessageFilterQueryResponse : NSObject
```

## Topics

### Specifying the Action
- [var action: ILMessageFilterAction](./ilmessagefilterqueryresponse/action.md)
  The action the Message Filter app extension recommends that the system perform on the queried message.
- [var subAction: ILMessageFilterSubAction](./ilmessagefilterqueryresponse/subaction.md)
  The subaction the Message Filter app extension recommends that the system perform on the queried message.
### Initializers
- [init?(coder: NSCoder)](./ilmessagefilterqueryresponse/init%28coder%29.md)

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
- [class ILNetworkResponse](./ilnetworkresponse.md)
  A response to an HTTPS network request performed on behalf of a Message Filter app extension.
- [enum ILMessageFilterAction](./ilmessagefilteraction.md)
  Responds to a received message with a filter action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryresponse)*