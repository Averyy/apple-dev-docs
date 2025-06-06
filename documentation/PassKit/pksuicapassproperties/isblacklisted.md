# isBlacklisted

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates whether the transit pass issuer disabled the pass.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
var isBlacklisted: Bool { get }
```

#### Discussion

Transit pass issuers are responsible for blacklisting transit passes according to their policies. Blacklisted transit passes are not accepted at transit terminals.

## See Also

- [var isBlocked: Bool](pksuicapassproperties/isblocked.md)
  A Boolean value that indicates whether the pass issuer disabled the pass.
- [var isGreenCarTicketUsed: Bool](pksuicapassproperties/isgreencarticketused.md)
  A Boolean value that indicates whether the customer has redeemed the Green Car ticket.
- [var isInShinkansenStation: Bool](pksuicapassproperties/isinshinkansenstation.md)
  A Boolean value that indicates whether the pass has tapped in at a Shinkansen Station and has not tapped out.
- [var isInStation: Bool](pksuicapassproperties/isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/isblacklisted)*