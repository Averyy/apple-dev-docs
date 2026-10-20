# isBlacklisted

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the transit pass issuer disabled the pass.

**Availability**:
- iOS 10.1+ - Deprecated in 15.0
- iPadOS 10.1+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.1+ - Deprecated in 8.0

> **Deprecated**: Use `PKStoredValuePassProperties` property [`blocked`](../pkstoredvaluepassproperties/blocked.md) instead.

## Declaration

```swift
var isBlacklisted: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isBlacklisted) BOOL blacklisted;
```

#### Discussion

Transit pass issuers are responsible for blacklisting transit passes according to their policies. Blacklisted transit passes are not accepted at transit terminals.

## See Also

### Getting pass status
- [var isBlocked: Bool](./isblocked.md)
  A Boolean value that indicates whether the pass issuer disabled the pass.
- [var isGreenCarTicketUsed: Bool](./isgreencarticketused.md)
  A Boolean value that indicates whether the customer has redeemed the Green Car ticket.
- [var isInShinkansenStation: Bool](./isinshinkansenstation.md)
  A Boolean value that indicates whether the pass has tapped in at a Shinkansen Station and has not tapped out.
- [var isInStation: Bool](./isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/isblacklisted)*