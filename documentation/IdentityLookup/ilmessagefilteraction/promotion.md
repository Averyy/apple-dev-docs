# ILMessageFilterAction.promotion

**Framework**: SMS and Call Reporting  
**Kind**: case  
**Role**: Case

Prevents the system from showing the message normally, filtered as a Promotional message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
case promotion
```

```c
ILMessageFilterActionPromotion
```

## See Also

### Filter Actions
- [ILMessageFilterAction.none](./none.md)
  Allows the system to show the message unfiltered due to insufficient information to determine an action.
- [ILMessageFilterAction.allow](./allow.md)
  Allows the system to show the message unfiltered.
- [ILMessageFilterAction.junk](./junk.md)
  Prevents the system from showing the message normally, filtered as a Junk message.
- [ILMessageFilterAction.transaction](./transaction.md)
  Prevents the system from showing the message normally, filtered as a Transactional message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilteraction/promotion)*