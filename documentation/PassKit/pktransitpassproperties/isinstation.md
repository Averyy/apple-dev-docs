# isInStation

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
var isInStation: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isInStation) BOOL inStation;
```

#### Discussion

Transit networks that have tap-in and tap-out ride accounting use this value. Wallet may display this status as “en-route” in its user interface.

## See Also

### Getting pass status
- [var expirationDate: Date?](./expirationdate.md)
  The date that the transit card expires.
- [var isBlocked: Bool](./isblocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.
- [var isBlacklisted: Bool](./isblacklisted.md)
  A Boolean value that indicates the transit pass issuer disabled the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties/isinstation)*