# ILMessageFilterAction.allow

**Framework**: SMS and Call Reporting  
**Kind**: case  
**Role**: Case

Allows the system to show the message unfiltered.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
case allow
```

```c
ILMessageFilterActionAllow
```

## See Also

### Filter Actions
- [ILMessageFilterAction.none](./none.md)
  Allows the system to show the message unfiltered due to insufficient information to determine an action.
- [ILMessageFilterAction.junk](./junk.md)
  Prevents the system from showing the message normally, filtered as a Junk message.
- [ILMessageFilterAction.promotion](./promotion.md)
  Prevents the system from showing the message normally, filtered as a Promotional message.
- [ILMessageFilterAction.transaction](./transaction.md)
  Prevents the system from showing the message normally, filtered as a Transactional message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilteraction/allow)*