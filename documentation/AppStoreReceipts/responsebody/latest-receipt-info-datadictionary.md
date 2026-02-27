# responseBody.Latest_receipt_info

**Framework**: App Store Receipts  
**Kind**: dictionary

An array that contains all in-app purchase transactions.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
object responseBody.Latest_receipt_info
```

## Properties

- `app_account_token` (app_account_token): The [`appAccountToken`](https://developer.apple.com/documentation/StoreKit/Transaction/appAccountToken) associated with this transaction. This field is only present if your app supplied an [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) or provided a UUID for the [`applicationUsername`](https://developer.apple.com/documentation/StoreKit/SKMutablePayment/applicationUsername) property when the user made the purchase.
- `cancellation_date` (string): The time the App Store refunded a transaction or revoked it from Family Sharing, in a date-time format similar to the ISO 8601. This field is present only for refunded or revoked transactions.
- `cancellation_date_ms` (cancellation_date_ms): The time the App Store refunded a transaction or revoked it from Family Sharing, in UNIX epoch time format, in milliseconds. This field is present only for refunded or revoked transactions. Use this time format for processing dates.
- `cancellation_date_pst` (string): The time the App Store refunded a transaction or revoked it from Family Sharing, in Pacific Standard Time. This field is present only for refunded or revoked transactions.
- `cancellation_reason` (string): The reason for a refunded or revoked transaction. A value of `1` indicates that the customer canceled their transaction due to an actual or perceived issue within your app. A value of `0` indicates that the transaction was canceled for another reason; for example, if the customer made the purchase accidentally.
- `expires_date` (string): The time an auto-renewable subscription expires or when it will renew, in a date-time format similar to the ISO 8601.
- `expires_date_ms` (expires_date_ms): The time an auto-renewable subscription expires or when it will renew, in UNIX epoch time format, in milliseconds. Use this time format for processing dates.
- `expires_date_pst` (string): The time an auto-renewable subscription expires or when it will renew, in Pacific Standard Time.
- `in_app_ownership_type` (in_app_ownership_type): A value that indicates whether the user is the purchaser of the product or is a family member with access to the product through Family Sharing.
- `is_in_intro_offer_period` (string): An indicator of whether an auto-renewable subscription is in the introductory price period. See [`is_in_intro_offer_period`](responsebody/latest_receipt_info-data.dictionary/is_in_intro_offer_period.md) for more information.
- `is_trial_period` (is_trial_period): An indicator of whether an auto-renewable subscription is in the free trial period.
- `is_upgraded` (string): An indicator that an auto-renewable subscription has been canceled due to an upgrade. This field is only present for upgrade transactions.
- `offer_code_ref_name` (offer_code_ref_name): The reference name of a subscription offer that you configured in App Store Connect. This field is present when a customer redeems a subscription offer code. For more information about offer codes, see [`Set Up Offer Codes`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev6a098e4b1), and [`Implementing offer codes in your app`](https://developer.apple.com/documentation/StoreKit/implementing-offer-codes-in-your-app).
- `original_purchase_date` (string): The time of the original app purchase, in a date-time format similar to ISO 8601.
- `original_purchase_date_ms` (string): The time of the original app purchase, in UNIX epoch time format, in milliseconds. Use this time format for processing dates. For an auto-renewable subscription, this value indicates the date of the subscription’s initial purchase. The original purchase date applies to all product types and remains the same in all transactions for the same product ID. This value corresponds to the original transaction’s [`transactionDate`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction/transactionDate) property in StoreKit.
- `original_purchase_date_pst` (string): The time of the original app purchase, in Pacific Standard Time.
- `original_transaction_id` (original_transaction_id): The transaction identifier of the original purchase.
- `product_id` (string): The unique identifier of the product purchased. You provide this value when creating the product in App Store Connect, and it corresponds to the [`productIdentifier`](https://developer.apple.com/documentation/StoreKit/SKPayment/productIdentifier) property of the [`SKPayment`](https://developer.apple.com/documentation/StoreKit/SKPayment) object stored in the transaction’s payment property.
- `promotional_offer_id` (promotional_offer_id): The identifier of the subscription offer redeemed by the user.
- `purchase_date` (string): The time the App Store charged the user’s account for a purchased or restored product, or the time the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in a date-time format similar to ISO 8601.
- `purchase_date_ms` (string): For consumable, non-consumable, and non-renewing subscription products, the time the App Store charged the user’s account for a purchased or restored product, in the UNIX epoch time format, in milliseconds. For auto-renewable subscriptions, the time the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in the UNIX epoch time format, in milliseconds. Use this time format for processing dates.
- `purchase_date_pst` (string): The time the App Store charged the user’s account for a purchased or restored product, or the time the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in Pacific Standard Time.
- `quantity` (string): The number of consumable products purchased. This value corresponds to the [`quantity`](https://developer.apple.com/documentation/StoreKit/SKPayment/quantity) property of the [`SKPayment`](https://developer.apple.com/documentation/StoreKit/SKPayment) object stored in the transaction’s payment property. The value is usually `1` unless modified with a mutable payment. The maximum value is `10`.
- `subscription_group_identifier` (string): The identifier of the subscription group to which the subscription belongs. The value for this field is identical to the [`subscriptionGroupIdentifier`](https://developer.apple.com/documentation/StoreKit/SKProduct/subscriptionGroupIdentifier) property in [`SKProduct`](https://developer.apple.com/documentation/StoreKit/SKProduct).
- `web_order_line_item_id` (string): A unique identifier for purchase events across devices, including subscription-renewal events. This value is the primary key for identifying subscription purchases.
- `transaction_id` (transaction_id): A unique identifier for a transaction such as a purchase, restore, or renewal.

## See Also

- [object responseBody.Pending_renewal_info](responsebody/pending_renewal_info-data.dictionary.md)
  An array of elements that refers to open or failed auto-renewable subscription renewals.
- [object responseBody.Receipt](responsebody/receipt-data.dictionary.md)
  The decoded version of the encoded receipt data that you send with the request to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/responsebody/latest_receipt_info-data.dictionary)*