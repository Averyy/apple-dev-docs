# Testing transaction observer code

**Framework**: StoreKit

Verify that your app activates its payment transaction observer by using breakpoints.

#### Overview

Review the transaction observer’s implementation of the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) protocol. Verify that the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) listens for transactions when:

- Your app isn’t displaying its store UI
- If you didn’t recently initiate a purchase

Locate the call to the [`add(_:)`](skpaymentqueue/add(_:)-5ciz2.md) method of [`SKPaymentQueue`](skpaymentqueue.md) in your code. Verify that your app calls this method at app launch. For more information, see [`Setting up the transaction observer for the payment queue`](setting-up-the-transaction-observer-for-the-payment-queue.md).

## See Also

- [Testing a successful transaction](testing-a-successful-transaction.md)
  Confirm that your app can make a successful transaction in the sandbox environment by inspecting the transaction.
- [Testing complete transactions](testing-complete-transactions.md)
  Verify that your app completes transactions properly by confirming that any downloadable purchases are present on your test device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-transaction-observer-code)*