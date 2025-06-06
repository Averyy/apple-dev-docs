# PKStoredValuePassBalance.BalanceType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

The type of value that the balance represents, such as money or points.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BalanceType
```

## Topics

### Creating a balance type
- [init(rawValue: String)](pkstoredvaluepassbalance/balancetype-swift.struct/init(rawvalue:).md)
  Creates a balance type.
### Reading the balance type
- [static let cash: PKStoredValuePassBalance.BalanceType](pkstoredvaluepassbalance/balancetype-swift.struct/cash.md)
  An identifier indicating a balance that represents money.
- [static let loyaltyPoints: PKStoredValuePassBalance.BalanceType](pkstoredvaluepassbalance/balancetype-swift.struct/loyaltypoints.md)
  An identifier indicating a balance that represents points.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var expiryDate: Date?](pkstoredvaluepassbalance/expirydate.md)
  The date that the balance expires.
- [var amount: Decimal](pkstoredvaluepassbalance/amount-2nwf5.md)
  The current balance of a stored-value pass in money or points.
- [var balanceType: PKStoredValuePassBalance.BalanceType](pkstoredvaluepassbalance/balancetype-swift.property.md)
  The type of value that the balance represents, such as money or points.
- [var currencyCode: String?](pkstoredvaluepassbalance/currencycode.md)
  The ISO 4217 currency code of the balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassbalance/balancetype-swift.struct)*