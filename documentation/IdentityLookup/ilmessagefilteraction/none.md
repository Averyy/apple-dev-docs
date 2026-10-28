# ILMessageFilterAction.none

**Framework**: SMS and Call Reporting  
**Kind**: case  
**Role**: Case

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

```c
ILMessageFilterActionNone
```

## Discussion

In a query response, setting this value allows the system to show the message unfiltered.

## See Also

### Filter Actions
- [ILMessageFilterAction.allow](./allow.md)
  Allows the system to show the message unfiltered.
- [ILMessageFilterAction.junk](./junk.md)
  Prevents the system from showing the message normally, filtered as a Junk message.
- [ILMessageFilterAction.promotion](./promotion.md)
  Prevents the system from showing the message normally, filtered as a Promotional message.
- [ILMessageFilterAction.transaction](./transaction.md)
  Prevents the system from showing the message normally, filtered as a Transactional message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilteraction/none)*