# isInStation

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
var isInStation: Bool { get }
```

#### Discussion

Transit networks that have tap-in and tap-out ride accounting use this value. Wallet may display this status as “en-route” in its user interface.

## See Also

- [var expirationDate: Date?](pktransitpassproperties/expirationdate.md)
  The date that the transit card expires.
- [var isBlocked: Bool](pktransitpassproperties/isblocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.
- [var isBlacklisted: Bool](pktransitpassproperties/isblacklisted.md)
  A Boolean value that indicates the transit pass issuer disabled the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/isinstation)*