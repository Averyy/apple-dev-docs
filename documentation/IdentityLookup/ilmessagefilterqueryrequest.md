# ILMessageFilterQueryRequest

**Framework**: SMS and Call Reporting  
**Kind**: class

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

## Topics

### Getting Information About a Message
- [var sender: String?](ilmessagefilterqueryrequest/sender.md)
  The sender of the message.
- [var messageBody: String?](ilmessagefilterqueryrequest/messagebody.md)
  The body of a message received from an unknown sender.
- [var receiverISOCountryCode: String?](ilmessagefilterqueryrequest/receiverisocountrycode.md)
  The ISO Country Code of the receiving phone number, in format specified by the ISO 3166-2 standard.

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

- [protocol ILMessageFilterQueryHandling](ilmessagefilterqueryhandling.md)
  A set of methods implemented by a Message Filter app extension to handle query requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterqueryrequest)*