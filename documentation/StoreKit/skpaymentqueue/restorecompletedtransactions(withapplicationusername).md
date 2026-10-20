# restoreCompletedTransactions(withApplicationUsername:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Asks the payment queue to restore previously completed purchases, providing an opaque identifier for the user’s account.

**Availability**:
- iOS 7.0+ - Deprecated in 18.0
- iPadOS 7.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.9+ - Deprecated in 15.0
- tvOS 7.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use AppStore.sync().

## Declaration

```swift
func restoreCompletedTransactions(withApplicationUsername username: String?)
```

```objc
- (void) restoreCompletedTransactionsWithApplicationUsername:(NSString *) username;
```

## Mentions

- [Choosing a receipt validation technique](../choosing-a-receipt-validation-technique.md)
- [Restoring purchased products](../restoring-purchased-products.md)
- [Testing Apple In-App Purchases in Xcode](../testing-in-app-purchases-in-xcode.md)

## Parameters

- `username`: An opaque identifier for the user’s account on your system.

## See Also

### Related Documentation
- [var applicationUsername: String?](../skpayment/applicationusername.md)
  A string that associates the transaction with a user account on your service.
### Restoring Purchases
- [func restoreCompletedTransactions()](./restorecompletedtransactions%28%29.md)
  Asks the payment queue to restore previously completed purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/restorecompletedtransactions(withapplicationusername:))*