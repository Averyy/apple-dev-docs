# PKStoredValuePassBalance.BalanceType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

The type of value that the balance represents, such as money or points.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
struct BalanceType
```

```c
typedef NSString * PKStoredValuePassBalanceType;
```

## Topics

### Creating a balance type
- [init(rawValue: String)](./balancetype-swift.struct/init%28rawvalue%29.md)
  Creates a balance type.
### Reading the balance type
- [static let cash: PKStoredValuePassBalance.BalanceType](./balancetype-swift.struct/cash.md)
  An identifier indicating a balance that represents money.
- [static let loyaltyPoints: PKStoredValuePassBalance.BalanceType](./balancetype-swift.struct/loyaltypoints.md)
  An identifier indicating a balance that represents points.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the pass status
- [var expiryDate: Date?](./expirydate.md)
  The date that the balance expires.
- [var amount: Decimal](./amount-2nwf5.md)
  The current balance of a stored-value pass in money or points.
- [var balanceType: PKStoredValuePassBalance.BalanceType](./balancetype-swift.property.md)
  The type of value that the balance represents, such as money or points.
- [var currencyCode: String?](./currencycode.md)
  The ISO 4217 currency code of the balance.
- [amount](./amount-2vfd3.md)
  The current balance in money or points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassbalance/balancetype-swift.struct)*