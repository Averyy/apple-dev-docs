# isBlacklisted

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates the transit pass issuer disabled the pass.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
var isBlacklisted: Bool { get }
```

#### Discussion

A blocked pass isn’t accepted at a transit terminal.

## See Also

- [var expirationDate: Date?](pktransitpassproperties/expirationdate.md)
  The date that the transit card expires.
- [var isInStation: Bool](pktransitpassproperties/isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.
- [var isBlocked: Bool](pktransitpassproperties/isblocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/isblacklisted)*