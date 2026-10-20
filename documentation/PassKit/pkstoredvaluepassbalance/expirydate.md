# expiryDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The date that the balance expires.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var expiryDate: Date? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSDate * expiryDate;
```

## See Also

### Getting the pass status
- [var amount: Decimal](./amount-2nwf5.md)
  The current balance of a stored-value pass in money or points.
- [var balanceType: PKStoredValuePassBalance.BalanceType](./balancetype-swift.property.md)
  The type of value that the balance represents, such as money or points.
- [var currencyCode: String?](./currencycode.md)
  The ISO 4217 currency code of the balance.
- [PKStoredValuePassBalance.BalanceType](./balancetype-swift.struct.md)
  The type of value that the balance represents, such as money or points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassbalance/expirydate)*