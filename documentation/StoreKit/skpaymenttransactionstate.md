# SKPaymentTransactionState

**Framework**: StoreKit  
**Kind**: enum

Values representing the state of a transaction.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
enum SKPaymentTransactionState
```

## Topics

### Constants
- [SKPaymentTransactionState.purchasing](skpaymenttransactionstate/purchasing.md)
  A transaction that is being processed by the App Store.
- [SKPaymentTransactionState.purchased](skpaymenttransactionstate/purchased.md)
  A successfully processed transaction.
- [SKPaymentTransactionState.failed](skpaymenttransactionstate/failed.md)
  A failed transaction.
- [SKPaymentTransactionState.restored](skpaymenttransactionstate/restored.md)
  A transaction that restores content previously purchased by the user.
- [SKPaymentTransactionState.deferred](skpaymenttransactionstate/deferred.md)
  A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.
### Initializers
- [init?(rawValue: Int)](skpaymenttransactionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var transactionState: SKPaymentTransactionState](skpaymenttransaction/transactionstate.md)
  The current state of the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate)*