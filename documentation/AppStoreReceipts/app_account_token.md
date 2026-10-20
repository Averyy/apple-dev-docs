# app_account_token

**Framework**: App Store Receipts  
**Kind**: typealias  
**Role**: Type

The UUID that an app optionally generates to map a customer’s in-app purchase with its resulting App Store transaction.

**Availability**:
- App Store Receipts 1.5+ - Deprecated in 1.7

## Declaration

```
string app_account_token
```

#### Discussion

When a customer initiates an in-app purchase, you can optionally generate an [`appAccountToken(_:)`](../StoreKit/product/purchaseoption/appaccounttoken%28_%29.md) and send it to the App Store. The App Store returns the same value in [`appAccountToken`](../StoreKit/transaction/appaccounttoken.md) in the transaction information after the customer completes the purchase.

If you’re using the [Original API for Apple In-App Purchase](../StoreKit/original-api-for-in-app-purchase.md) and provide a UUID in the [`applicationUsername`](../StoreKit/skmutablepayment/applicationusername.md) property, then the [`app_account_token`](./app_account_token.md) field contains that value.

## See Also

### Transaction identifiers
- [type original_transaction_id](./original_transaction_id.md)
  The transaction identifier of the original purchase.
- [type transaction_id](./transaction_id.md)
  A unique identifier for a transaction, such as a purchase, restore, or renewal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/app_account_token)*