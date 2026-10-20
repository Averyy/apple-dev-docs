# isBlocked

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the pass issuer disabled the pass.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 10.1+
- macOS
- visionOS
- watchOS 3.1+

> **Deprecated**: Use `PKStoredValuePassProperties` property [`blocked`](../pkstoredvaluepassproperties/blocked.md) instead.

## Declaration

```swift
override dynamic var isBlocked: Bool { get }
```

## See Also

### Getting pass status
- [var isBlacklisted: Bool](./isblacklisted.md)
  A Boolean value that indicates whether the transit pass issuer disabled the pass.
- [var isGreenCarTicketUsed: Bool](./isgreencarticketused.md)
  A Boolean value that indicates whether the customer has redeemed the Green Car ticket.
- [var isInShinkansenStation: Bool](./isinshinkansenstation.md)
  A Boolean value that indicates whether the pass has tapped in at a Shinkansen Station and has not tapped out.
- [var isInStation: Bool](./isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/isblocked)*