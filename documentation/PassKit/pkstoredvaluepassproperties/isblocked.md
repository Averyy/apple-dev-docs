# isBlocked

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates the pass issuer disabled a stored-value pass.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
@objc
dynamic var isBlocked: Bool { get }
```

#### Discussion

The pass issuer is responsible for blocking a stored-value pass according to their policy. The service provider can’t process transactions for a blocked pass.

## See Also

- [var balances: [PKStoredValuePassBalance]](pkstoredvaluepassproperties/balances.md)
  The amount available for transactions for a service represented by a stored-value pass.
- [var expirationDate: Date?](pkstoredvaluepassproperties/expirationdate.md)
  The expiration date of a pass.
- [var isBlacklisted: Bool](pkstoredvaluepassproperties/isblacklisted.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassproperties/isblocked)*