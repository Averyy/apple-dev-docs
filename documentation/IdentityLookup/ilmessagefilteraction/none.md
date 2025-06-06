# ILMessageFilterAction.none

**Framework**: SMS and Call Reporting  
**Kind**: case

Allows the system to show the message unfiltered due to insufficient information to determine an action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

#### Discussion

In a query response, setting this value allows the system to show the message unfiltered.

## See Also

- [ILMessageFilterAction.allow](ilmessagefilteraction/allow.md)
  Allows the system to show the message unfiltered.
- [ILMessageFilterAction.junk](ilmessagefilteraction/junk.md)
  Prevents the system from showing the message normally, filtered as a Junk message.
- [ILMessageFilterAction.promotion](ilmessagefilteraction/promotion.md)
  Prevents the system from showing the message normally, filtered as a Promotional message.
- [ILMessageFilterAction.transaction](ilmessagefilteraction/transaction.md)
  Prevents the system from showing the message normally, filtered as a Transactional message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilteraction/none)*