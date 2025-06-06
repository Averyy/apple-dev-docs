# balances

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The amount available for transactions for a service represented by a stored-value pass.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS ?+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var balances: [PKStoredValuePassBalance] { get }
```

## See Also

- [var expirationDate: Date?](pkstoredvaluepassproperties/expirationdate.md)
  The expiration date of a pass.
- [var isBlocked: Bool](pkstoredvaluepassproperties/isblocked.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.
- [var isBlacklisted: Bool](pkstoredvaluepassproperties/isblacklisted.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassproperties/balances)*