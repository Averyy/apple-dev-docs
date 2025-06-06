# Testing complete transactions

**Framework**: StoreKit

Verify that your app completes transactions properly by confirming that any downloadable purchases are present on your test device.

#### Overview

Locate where your app calls the [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md) method, and verify that your app completes all work related to the transaction before calling the method. For example, if the purchase includes downloadable content, verify your app downloaded the content to your test device as described in [`Persisting a purchase`](persisting-a-purchase.md). Verify that you call [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md) for every transaction, whether it succeeded or failed. For more information, see [`Finishing a transaction`](finishing-a-transaction.md).

## See Also

- [Testing transaction observer code](testing-transaction-observer-code.md)
  Verify that your app activates its payment transaction observer by using breakpoints.
- [Testing a successful transaction](testing-a-successful-transaction.md)
  Confirm that your app can make a successful transaction in the sandbox environment by inspecting the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-complete-transactions)*