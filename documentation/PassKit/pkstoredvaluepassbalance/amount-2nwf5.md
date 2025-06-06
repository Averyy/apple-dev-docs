# amount

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The current balance of a stored-value pass in money or points.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var amount: Decimal { get }
```

## See Also

- [var expiryDate: Date?](pkstoredvaluepassbalance/expirydate.md)
  The date that the balance expires.
- [var balanceType: PKStoredValuePassBalance.BalanceType](pkstoredvaluepassbalance/balancetype-swift.property.md)
  The type of value that the balance represents, such as money or points.
- [var currencyCode: String?](pkstoredvaluepassbalance/currencycode.md)
  The ISO 4217 currency code of the balance.
- [PKStoredValuePassBalance.BalanceType](pkstoredvaluepassbalance/balancetype-swift.struct.md)
  The type of value that the balance represents, such as money or points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassbalance/amount-2nwf5)*