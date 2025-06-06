# ILMessageFilterQueryResponse

**Framework**: SMS and Call Reporting  
**Kind**: class

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

## Topics

### Specifying the Action
- [var action: ILMessageFilterAction](ilmessagefilterqueryresponse/action.md)
  The action the Message Filter app extension recommends that the system perform on the queried message.
- [var subAction: ILMessageFilterSubAction](ilmessagefilterqueryresponse/subaction.md)
  The subaction the Message Filter app extension recommends that the system perform on the queried message.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class ILNetworkResponse](ilnetworkresponse.md)
  A response to an HTTPS network request performed on behalf of a Message Filter app extension.
- [enum ILMessageFilterAction](ilmessagefilteraction.md)
  Responds to a received message with a filter action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryresponse)*