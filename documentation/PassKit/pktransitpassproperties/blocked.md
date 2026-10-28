# blocked

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the pass issuer disabled the pass.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+
- watchOS 7.5+

> **Deprecated**: Use `PKStoredValuePassProperties` property [`blocked`](../pkstoredvaluepassproperties/blocked.md) instead.

## Declaration

```objc
@property (nonatomic, assign, readonly, getter=isBlocked) BOOL blocked;
```

## Discussion

A blocked pass isn’t accepted at a transit terminal.

## See Also

### Getting pass status
- [var expirationDate: Date?](./expirationdate.md)
  The date that the transit card expires.
- [var isInStation: Bool](./isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.
- [var isBlacklisted: Bool](./isblacklisted.md)
  A Boolean value that indicates the transit pass issuer disabled the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/blocked)*