# SKPaymentTransactionState

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Values representing the state of a transaction.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use PurchaseResult from Product.purchase(confirmIn:options:).

## Declaration

```swift
enum SKPaymentTransactionState
```

```c
enum SKPaymentTransactionState : NSInteger;
```

## Topics

### Constants
- [SKPaymentTransactionState.purchasing](./skpaymenttransactionstate/purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.purchased](./skpaymenttransactionstate/purchased.md)
  A successfully processed transaction.
- [SKPaymentTransactionState.failed](./skpaymenttransactionstate/failed.md)
  A failed transaction.
- [SKPaymentTransactionState.restored](./skpaymenttransactionstate/restored.md)
  A transaction that restores content previously purchased by the user.
- [SKPaymentTransactionState.deferred](./skpaymenttransactionstate/deferred.md)
  A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.
### Initializers
- [init?(rawValue: Int)](./skpaymenttransactionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Transaction State
- [var transactionState: SKPaymentTransactionState](./skpaymenttransaction/transactionstate.md)
  The current state of the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate)*