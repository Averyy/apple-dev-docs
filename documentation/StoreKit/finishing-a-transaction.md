# Finishing a transaction

**Framework**: StoreKit

Finish the transaction to complete the purchase process.

#### Overview

Finishing a transaction tells StoreKit that your app completed its workflow to make a purchase complete. Unfinished transactions remain in the queue until they’re finished, so be sure to add the transaction queue observer every time your app launches, to enable your app to finish the transactions. Your app needs to finish each transaction, whether it succeeds or fails.

Do all of the following before you finish a transaction:

- Persist the purchase.
- Deliver, download, or unlock the purchased content.
- Update your app’s UI so the user can access the product.

To finish the transaction, call the [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md) method on the payment queue.

After you finish a transaction, don’t take any actions on it or do any work to deliver the product. If any work remains, your app isn’t ready to finish the transaction.

> ❗ **Important**:  Don’t call the [`finishTransaction(_:)`](skpaymentqueue/finishtransaction(_:).md) method before the transaction is actually complete and attempt to use some other mechanism in your app to track the transaction as unfinished. StoreKit doesn’t function that way, and doing that prevents your app from downloading Apple-hosted content and can lead to other issues.

## See Also

- [Unlocking purchased content](unlocking-purchased-content.md)
  Deliver content to the customer after validating the purchase.
- [Persisting a purchase](persisting-a-purchase.md)
  Keep a persistent record of a purchase to continue making the product available as needed.
- [class SKDownload](skdownload.md)
  Downloadable content associated with a product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/finishing-a-transaction)*