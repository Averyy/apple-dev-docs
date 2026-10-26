# isBlacklisted

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the pass issuer disabled a stored-value pass.

**Availability**:
- iOS 15.0+ - Deprecated in 15.0
- iPadOS 15.0+ - Deprecated in 15.0
- Mac Catalyst 15.0+ - Deprecated in 15.0
- macOS 12.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 8.0+ - Deprecated in 8.0

> **Deprecated**: Use `PKStoredValuePassProperties` property [`blocked`](./blocked.md) instead.

## Declaration

```swift
var isBlacklisted: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isBlacklisted) BOOL blacklisted;
```

## See Also

### Reading the stored-value pass properties
- [var balances: [PKStoredValuePassBalance]](./balances.md)
  The amount available for transactions for a service represented by a stored-value pass.
- [var expirationDate: Date?](./expirationdate.md)
  The expiration date of a pass.
- [var isBlocked: Bool](./isblocked.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.
- [blocked](./blocked.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassproperties/isblacklisted)*