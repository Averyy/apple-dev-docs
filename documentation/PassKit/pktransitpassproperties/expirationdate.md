# expirationDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The date that the transit card expires.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
var expirationDate: Date? { get }
```

#### Discussion

Rules for expiry depend on the pass provider. The return value can be `nil` if the transit card does not support an expiration date.

## See Also

- [var isInStation: Bool](pktransitpassproperties/isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.
- [var isBlocked: Bool](pktransitpassproperties/isblocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.
- [var isBlacklisted: Bool](pktransitpassproperties/isblacklisted.md)
  A Boolean value that indicates the transit pass issuer disabled the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/expirationdate)*