# unified_receipt.Latest_receipt_info

**Framework**: App Store Server Notifications  
**Kind**: dictionary

An object that contains information about the latest in-app subscription transaction.

**Availability**:
- App Store Server Notifications 1.2+

## Declaration

```swift
object unified_receipt.Latest_receipt_info
```

## Properties

- `app_account_token` (string): The [`appAccountToken`](https://developer.apple.com/documentation/StoreKit/Transaction/appAccountToken) associated with this transaction. This field is only present if your app supplied an [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) or provided a UUID for the [`applicationUsername`](https://developer.apple.com/documentation/StoreKit/SKMutablePayment/applicationUsername) property when the user made the purchase.
- `cancellation_date` (string): The time the App Store refunded a transaction or revoked it from family sharing, in a date-time format similar to the ISO 8601. This field is present only for refunded or revoked transactions.
- `cancellation_date_ms` (string): The time the App Store refunded a transaction or revoked it from family sharing, in UNIX epoch time format, in milliseconds. This field is present only for refunded or revoked transactions. Use this time format for processing dates. For more information, see [`cancellation_date_ms`](https://developer.apple.com/documentation/AppStoreReceipts/cancellation_date_ms).
- `cancellation_date_pst` (string): The time the App Store refunded a transaction or revoked it from family sharing, in Pacific Standard Time. This field is present only for refunded or revoked transactions.
- `cancellation_reason` (string): The reason for a refunded or revoked transaction. A value of `1` indicates that the customer canceled their transaction due to an actual or perceived issue within your app. A value of `0` indicates that the transaction was canceled for another reason, for example, if the customer made the purchase accidentally.
- `expires_date` (string): The time a subscription expires or when it will renew, in a date-time format similar to the ISO 8601.
- `expires_date_ms` (string): The time when a subscription expires or when it will renew, in UNIX epoch time format, in milliseconds. Use this time format for processing dates. For more information, see [`expires_date_ms`](https://developer.apple.com/documentation/AppStoreReceipts/expires_date_ms).
- `expires_date_pst` (string): The time when a subscription expires or when it will renew, in Pacific Standard Time.
- `in_app_ownership_type` (string): A value that indicates whether the user is the purchaser of the product or is a family member with access to the product through Family Sharing. See [`in_app_ownership_type`](https://developer.apple.com/documentation/AppStoreReceipts/in_app_ownership_type) for more information.
- `is_in_intro_offer_period` (string): An indicator of whether an auto-renewable subscription is in the introductory price period. For more information, see [`is_in_intro_offer_period`](https://developer.apple.com/documentation/AppStoreReceipts/is_in_intro_offer_period).
- `is_trial_period` (string): An indicator of whether a subscription is in the free trial period. For more information, see [`is_trial_period`](https://developer.apple.com/documentation/AppStoreReceipts/is_trial_period).
- `is_upgraded` (string): An indicator that the system canceled a subscription because the user upgraded. This field is only present for subscription upgrade transactions.
- `offer_code_ref_name` (string): The reference name of a subscription offer you configured in App Store Connect. This field is present when a customer redeemed a subscription offer code. For more information, see [`offer_code_ref_name`](https://developer.apple.com/documentation/AppStoreReceipts/offer_code_ref_name).
- `original_purchase_date` (string): The time of the original app purchase, in a date-time format similar to the ISO 8601 standard.
- `original_purchase_date_ms` (string): The time of the original app purchase, in UNIX epoch time format, in milliseconds. Use this time format for processing dates. This value indicates the date of the subscription’s initial purchase. The original purchase date applies to all product types and remains the same in all transactions for the same product ID. This value corresponds to the original transaction’s [`transactionDate`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction/transactionDate) property in StoreKit.
- `original_purchase_date_pst` (string): The time of the original app purchase, in Pacific Standard Time.
- `original_transaction_id` (string): The transaction identifier of the original purchase. For more information, see [`original_transaction_id`](https://developer.apple.com/documentation/AppStoreReceipts/original_transaction_id).
- `promotional_offer_id` (string): The identifier of the subscription offer redeemed by the user. For more information, see [`promotional_offer_id`](https://developer.apple.com/documentation/AppStoreReceipts/promotional_offer_id).
- `product_id` (string): The unique identifier of the product purchased. You provide this value when creating the product in App Store Connect, and it corresponds to the [`productIdentifier`](https://developer.apple.com/documentation/StoreKit/SKPayment/productIdentifier) property of the [`SKPayment`](https://developer.apple.com/documentation/StoreKit/SKPayment) object stored in the transaction’s [`payment`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction/payment) property.
- `purchase_date` (string): The time when the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in a date-time format similar to the ISO 8601 standard.
- `purchase_date_ms` (string): The time when the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in the UNIX epoch time format, in milliseconds. Use this time format for processing dates.
- `purchase_date_pst` (string): The time when the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in Pacific Standard Time.
- `quantity` (string): The number of consumable products purchased. This value corresponds to the [`quantity`](https://developer.apple.com/documentation/StoreKit/SKPayment/quantity) property of the [`SKPayment`](https://developer.apple.com/documentation/StoreKit/SKPayment) object stored in the transaction’s [`payment`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction/payment) property. The value is usually `1` unless modified with a mutable payment. The maximum value is `10`.
- `subscription_group_identifier` (string): The identifier of the subscription group to which the subscription belongs. The value for this field is identical to the [`subscriptionGroupIdentifier`](https://developer.apple.com/documentation/StoreKit/SKProduct/subscriptionGroupIdentifier) property in [`SKProduct`](https://developer.apple.com/documentation/StoreKit/SKProduct).
- `transaction_id` (string): A unique identifier for a transaction such as a purchase, restore, or renewal. For more information, see [`transaction_id`](https://developer.apple.com/documentation/AppStoreReceipts/transaction_id).
- `web_order_line_item_id` (string): A unique identifier for purchase events across devices, including subscription-renewal events. This value is the primary key to identify subscription purchases.

## See Also

- [object unified_receipt.Pending_renewal_info](unified_receipt/pending_renewal_info-data.dictionary.md)
  An array of elements that refers to open auto-renewable subscription renewals or ones that failed in the past.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/unified_receipt/latest_receipt_info-data.dictionary)*