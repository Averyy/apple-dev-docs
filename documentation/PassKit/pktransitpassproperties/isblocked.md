# isBlocked

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates the pass issuer disabled the pass.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst ?+
- macOS 11.3+
- visionOS ?+
- watchOS 7.5+

## Declaration

```swift
override dynamic var isBlocked: Bool { get }
```

#### Discussion

A blocked pass isn’t accepted at a transit terminal.

## See Also

- [var expirationDate: Date?](pktransitpassproperties/expirationdate.md)
  The date that the transit card expires.
- [var isInStation: Bool](pktransitpassproperties/isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.
- [var isBlacklisted: Bool](pktransitpassproperties/isblacklisted.md)
  A Boolean value that indicates the transit pass issuer disabled the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/isblocked)*