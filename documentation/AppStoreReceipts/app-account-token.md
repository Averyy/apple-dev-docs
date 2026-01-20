# app_account_token

**Framework**: App Store Receipts  
**Kind**: typealias

The UUID that an app optionally generates to map a customer’s in-app purchase with its resulting App Store transaction.

**Availability**:
- App Store Receipts 1.5+

## Declaration

```swift
string app_account_token
```

#### Discussion

When a customer initiates an in-app purchase, you can optionally generate an [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) and send it to the App Store. The App Store returns the same value in [`appAccountToken`](https://developer.apple.com/documentation/StoreKit/Transaction/appAccountToken) in the transaction information after the customer completes the purchase.

If you’re using the [`Original API for In-App Purchase`](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase) and provide a UUID in the [`applicationUsername`](https://developer.apple.com/documentation/StoreKit/SKMutablePayment/applicationUsername) property, then the [`app_account_token`](app_account_token.md) field contains that value.

## See Also

- [type original_transaction_id](original_transaction_id.md)
  The transaction identifier of the original purchase.
- [type transaction_id](transaction_id.md)
  A unique identifier for a transaction, such as a purchase, restore, or renewal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/app_account_token)*