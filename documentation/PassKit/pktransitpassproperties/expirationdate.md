# expirationDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * expirationDate;
```

#### Discussion

Rules for expiry depend on the pass provider. The return value can be `nil` if the transit card does not support an expiration date.

## See Also

### Getting pass status
- [var isInStation: Bool](./isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.
- [var isBlocked: Bool](./isblocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.
- [var isBlacklisted: Bool](./isblacklisted.md)
  A Boolean value that indicates the transit pass issuer disabled the pass.
- [blocked](./blocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/expirationdate)*