# amount

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The current balance in money or points.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@property (nonatomic, strong, readonly) NSDecimalNumber * amount;
```

## See Also

### Getting the pass status
- [var expiryDate: Date?](./expirydate.md)
  The date that the balance expires.
- [var balanceType: PKStoredValuePassBalance.BalanceType](./balancetype-swift.property.md)
  The type of value that the balance represents, such as money or points.
- [var currencyCode: String?](./currencycode.md)
  The ISO 4217 currency code of the balance.
- [PKStoredValuePassBalance.BalanceType](./balancetype-swift.struct.md)
  The type of value that the balance represents, such as money or points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassbalance/amount-2vfd3)*