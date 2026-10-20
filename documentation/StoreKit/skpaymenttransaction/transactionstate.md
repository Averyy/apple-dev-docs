# transactionState

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The current state of the transaction.

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
var transactionState: SKPaymentTransactionState { get }
```

```objc
@property (nonatomic, readonly) SKPaymentTransactionState transactionState;
```

## See Also

### Getting Transaction State
- [enum SKPaymentTransactionState](../skpaymenttransactionstate.md)
  Values representing the state of a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactionstate)*