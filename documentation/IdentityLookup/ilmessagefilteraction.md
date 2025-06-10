# ILMessageFilterAction

**Framework**: SMS and Call Reporting  
**Kind**: enum

Responds to a received message with a filter action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
enum ILMessageFilterAction
```

## Topics

### Filter Actions
- [ILMessageFilterAction.none](ilmessagefilteraction/none.md)
  Allows the system to show the message unfiltered due to insufficient information to determine an action.
- [ILMessageFilterAction.allow](ilmessagefilteraction/allow.md)
  Allows the system to show the message unfiltered.
- [ILMessageFilterAction.junk](ilmessagefilteraction/junk.md)
  Prevents the system from showing the message normally, filtered as a Junk message.
- [ILMessageFilterAction.promotion](ilmessagefilteraction/promotion.md)
  Prevents the system from showing the message normally, filtered as a Promotional message.
- [ILMessageFilterAction.transaction](ilmessagefilteraction/transaction.md)
  Prevents the system from showing the message normally, filtered as a Transactional message.
### Deprecations
- [static var filter: ILMessageFilterAction](ilmessagefilteraction/filter.md)
  Prevents the system from showing the message unfiltered.
### Initializers
- [init?(rawValue: Int)](ilmessagefilteraction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ILMessageFilterQueryResponse](ilmessagefilterqueryresponse.md)
  A response to a message filter query request.
- [class ILNetworkResponse](ilnetworkresponse.md)
  A response to an HTTPS network request performed on behalf of a Message Filter app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilteraction)*