# restoreCompletedTransactions(withApplicationUsername:)

**Framework**: StoreKit  
**Kind**: method

Asks the payment queue to restore previously completed purchases, providing an opaque identifier for the user’s account.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
func restoreCompletedTransactions(withApplicationUsername username: String?)
```

## Mentions

- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md)
- [Testing In-App Purchases in Xcode](testing-in-app-purchases-in-xcode.md)
- [Restoring purchased products](restoring-purchased-products.md)

## Parameters

- `username`: An opaque identifier for the user’s account on your system.

## See Also

- [var applicationUsername: String?](skpayment/applicationusername.md)
  A string that associates the transaction with a user account on your service.
- [func restoreCompletedTransactions()](skpaymentqueue/restorecompletedtransactions.md)
  Asks the payment queue to restore previously completed purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/restorecompletedtransactions(withapplicationusername:))*