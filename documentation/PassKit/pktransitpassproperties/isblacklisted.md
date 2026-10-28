# isBlacklisted

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the transit pass issuer disabled the pass.

**Availability**:
- iOS 11.3+ - Deprecated in 15.0
- iPadOS 11.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 11.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.3+ - Deprecated in 8.0

> **Deprecated**: Use `PKStoredValuePassProperties` property [`blocked`](../pkstoredvaluepassproperties/blocked.md) instead.

## Declaration

```swift
var isBlacklisted: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isBlacklisted) BOOL blacklisted;
```

## Discussion

A blocked pass isn’t accepted at a transit terminal.

## See Also

### Getting pass status
- [var expirationDate: Date?](./expirationdate.md)
  The date that the transit card expires.
- [var isInStation: Bool](./isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.
- [var isBlocked: Bool](./isblocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.
- [blocked](./blocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/isblacklisted)*