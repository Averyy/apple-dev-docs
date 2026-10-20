# responseBody.Receipt.In_app

**Framework**: App Store Receipts  
**Kind**: dictionary

An array that contains the in-app purchase receipt fields for all in-app purchase transactions.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
object responseBody.Receipt.In_app
```

#### Discussion

The `in_app` array is not in chronological order. When parsing the array, iterate over all items to ensure all items are fulfilled. For example, you cannot assume that the last item in the array is the most recent.

For receipts containing auto-renewable subscriptions, check the value of the [`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info-data.dictionary.md) key of the response to get the status of the most recent renewal.

You can use this array to:

- Check for an empty array in a valid receipt, indicating that the App Store has made no in-app purchase charges.
- Determine which products the user purchased. Purchases for non-consumable products, auto-renewable subscriptions, and non-renewing subscriptions remain in the receipt indefinitely. For consumable products, the transaction is added to the receipt when the purchase is made, and remains until your app finishes that transaction. It no longer appears in updated receipts after you call [`finishTransaction(_:)`](https://developer.apple.com/documentation/storekit/skpaymentqueue/finishtransaction(_:)).

## Properties

- `cancellation_date` (string): The time the App Store refunded a transaction or revoked it from family sharing, in a date-time format similar to the ISO 8601. This field is present only for refunded or revoked transactions.
- `cancellation_date_ms` (cancellation_date_ms): The time the App Store refunded a transaction or revoked it from family sharing, in UNIX epoch time format, in milliseconds. This field is present only for refunded or revoked transactions. Use this time format for processing dates.  See [`cancellation_date_ms`](responsebody/receipt-data.dictionary/in_app-data.dictionary/cancellation_date_ms.md) for more information.
- `cancellation_date_pst` (string): The time the App Store refunded a transaction or revoked it from family sharing, in the Pacific Time zone. This field is present only for refunded or revoked transactions.
- `cancellation_reason` (string): The reason for a refunded or revoked transaction. A value of `“1”` indicates that the customer canceled their transaction due to an actual or perceived issue within your app. A value of `“0”` indicates that the transaction was canceled for another reason; for example, if the customer made the purchase accidentally.
- `expires_date` (string): The time a subscription expires or when it will renew, in a date-time format similar to the ISO 8601.
- `expires_date_ms` (expires_date_ms): The time a subscription expires or when it will renew, in UNIX epoch time format, in milliseconds. Use this time format for processing dates. See [`expires_date_ms`](responsebody/receipt-data.dictionary/in_app-data.dictionary/expires_date_ms.md) for more information.
- `expires_date_pst` (string): The time a subscription expires or when it will renew, in the Pacific Time zone.
- `is_in_intro_offer_period` (is_in_intro_offer_period): An indicator of whether an auto-renewable subscription is in the introductory price period. See [`is_in_intro_offer_period`](responsebody/receipt-data.dictionary/in_app-data.dictionary/is_in_intro_offer_period.md) for more information.
- `is_trial_period` (is_trial_period): An indication of whether a subscription is in the free trial period. See [`is_trial_period`](responsebody/receipt-data.dictionary/in_app-data.dictionary/is_trial_period.md) for more information.
- `original_purchase_date` (string): The time of the original in-app purchase, in a date-time format similar to ISO 8601.
- `original_purchase_date_ms` (string): The time of the original in-app purchase, in UNIX epoch time format, in milliseconds. For an auto-renewable subscription, this value indicates the date of the subscription’s initial purchase. The original purchase date applies to all product types and remains the same in all transactions for the same product ID. This value corresponds to the original transaction’s [`transactionDate`](https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactiondate) property in StoreKit. Use this time format for processing dates.
- `original_purchase_date_pst` (string): The time of the original in-app purchase, in the Pacific Time zone.
- `original_transaction_id` (original_transaction_id): The transaction identifier of the original purchase. See [`original_transaction_id`](responsebody/receipt-data.dictionary/in_app-data.dictionary/original_transaction_id.md) for more information.
- `product_id` (string): The unique identifier of the product purchased. You provide this value when creating the product in App Store Connect, and it corresponds to the `productIdentifier` property of the [`SKPayment`](https://developer.apple.com/documentation/storekit/skpayment) object stored in the transaction’s payment property.
- `promotional_offer_id` (promotional_offer_id): The identifier of the subscription offer redeemed by the user. See [`promotional_offer_id`](responsebody/receipt-data.dictionary/in_app-data.dictionary/promotional_offer_id.md) for more information.
- `purchase_date` (string): The time the App Store charged the user’s account for a purchased or restored product, or the time the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in a date-time format similar to ISO 8601.
- `purchase_date_ms` (string): For consumable, non-consumable, and non-renewing subscription products, the time the App Store charged the user’s account for a purchased or restored product, in the UNIX epoch time format, in milliseconds. For auto-renewable subscriptions, the time the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in the UNIX epoch time format, in milliseconds. Use this time format for processing dates.
- `purchase_date_pst` (string): The time the App Store charged the user’s account for a purchased or restored product, or the time the App Store charged the user’s account for a subscription purchase or renewal after a lapse, in the Pacific Time zone.
- `quantity` (string): The number of consumable products purchased. This value corresponds to the quantity property of the [`SKPayment`](https://developer.apple.com/documentation/storekit/skpayment) object stored in the transaction’s payment property. The value is usually `“1”` unless modified with a mutable payment. The maximum value is 10.
- `transaction_id` (transaction_id): A unique identifier for a transaction such as a purchase, restore, or renewal. See [`transaction_id`](responsebody/receipt-data.dictionary/in_app-data.dictionary/transaction_id.md) for more information.
- `web_order_line_item_id` (string): A unique identifier for purchase events across devices, including subscription-renewal events. This value is the primary key for identifying subscription purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/responsebody/receipt-data.dictionary/in_app-data.dictionary)*