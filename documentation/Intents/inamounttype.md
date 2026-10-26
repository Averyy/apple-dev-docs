# INAmountType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating an account-specific amount to apply to a payment.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INAmountType
```

```c
enum INAmountType : NSInteger;
```

## Topics

### Enumeration Cases
- [INAmountType.unknown](./inamounttype/unknown.md)
  An unknown amount.
- [INAmountType.minimumDue](./inamounttype/minimumdue.md)
  The minimum amount the user must apply to the bill.
- [INAmountType.amountDue](./inamounttype/amountdue.md)
  The amount due for the bill.
- [INAmountType.currentBalance](./inamounttype/currentbalance.md)
  The current account balance.
- [INAmountType.maximumTransferAmount](./inamounttype/maximumtransferamount.md)
  The maximum amount the user can transfer.
- [INAmountType.minimumTransferAmount](./inamounttype/minimumtransferamount.md)
  The minimum amount the user can transfer.
- [INAmountType.statementBalance](./inamounttype/statementbalance.md)
  The statement balance.
### Initializers
- [init?(rawValue: Int)](./inamounttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Payment Amount
- [var amount: INCurrencyAmount?](./inpaymentamount/amount.md)
  The precise amount of money to pay.
- [var amountType: INAmountType](./inpaymentamount/amounttype.md)
  The account-specific amount to pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inamounttype)*