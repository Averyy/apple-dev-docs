# balances

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The amount available for transactions for a service represented by a stored-value pass.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var balances: [PKStoredValuePassBalance] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<PKStoredValuePassBalance *> * balances;
```

## See Also

### Reading the stored-value pass properties
- [var expirationDate: Date?](./expirationdate.md)
  The expiration date of a pass.
- [var isBlocked: Bool](./isblocked.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.
- [var isBlacklisted: Bool](./isblacklisted.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassproperties/balances)*