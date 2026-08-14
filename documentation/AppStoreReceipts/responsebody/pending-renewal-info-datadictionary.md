# responseBody.Pending_renewal_info

**Framework**: App Store Receipts  
**Kind**: dictionary

An array of elements that refers to open or failed auto-renewable subscription renewals.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
object responseBody.Pending_renewal_info
```

#### Discussion

In the JSON file, `pending_renewal_info` is an array in which each element contains the pending renewal information for each auto-renewable subscription identified by the `product_id`. A pending renewal may refer to a renewal that the system scheduled in the future or a renewal that failed in the past for some reason.

Use this value to get critical information about any pending renewal transactions for an auto-renewable subscription.

The `pending_renewal_info` array is returned only for app receipts that contain auto-renewable subscriptions. If customers voluntarily cancel a subscription renewal while in the grace period, the App Store pauses billing retry, and removes the transaction from `pending_renewal_info`. The subscription is in the grace period if the key `grace_period_expires_date_ms` is present and the expiration date hasn’t passed.

## Properties

- `auto_renew_product_id` (string): The value for this key corresponds to the [`productIdentifier`](https://developer.apple.com/documentation/storekit/skpayment/productidentifier) property of the product that the customer’s subscription renews.
- `auto_renew_status` (auto_renew_status): The current renewal status for the auto-renewable subscription. See [`auto_renew_status`](responsebody/pending_renewal_info-data.dictionary/auto_renew_status.md) for more information.
- `expiration_intent` (expiration_intent): The reason a subscription expired. This field is present only for a receipt that contains an expired auto-renewable subscription.
- `grace_period_expires_date` (string): The time at which the grace period for subscription renewals expires, in a date-time format similar to the ISO 8601.
- `grace_period_expires_date_ms` (string): The time at which the grace period for subscription renewals expires, in UNIX epoch time format, in milliseconds. This key is present only for apps that have Billing Grace Period enabled and when the user experiences a billing error at the time of renewal. Use this time format for processing dates.
- `grace_period_expires_date_pst` (string): The time at which the grace period for subscription renewals expires, in the Pacific Time zone.
- `is_in_billing_retry_period` (is_in_billing_retry_period): A flag that indicates Apple is attempting to renew an expired subscription automatically. This field is present only if an auto-renewable subscription is in the billing retry state. See [`is_in_billing_retry_period`](responsebody/pending_renewal_info-data.dictionary/is_in_billing_retry_period.md) for more information.
- `offer_code_ref_name` (offer_code_ref_name): The reference name of a subscription offer that you configured in App Store Connect. This field is present when a customer redeemed a subscription offer code. For more information, see [`offer_code_ref_name`](responsebody/pending_renewal_info-data.dictionary/offer_code_ref_name.md).
- `original_transaction_id` (original_transaction_id): The transaction identifier of the original purchase.
- `price_consent_status` (string): The price consent status for an auto-renewable subscription price increase that requires customer consent. This field is present only if the App Store requested customer consent for a price increase that requires customer consent. The default value is `"0"` and changes to `"1"` if the customer consents.
- `product_id` (string): The unique identifier of the product purchased. You provide this value when creating the product in App Store Connect, and it corresponds to the `productIdentifier` property of the [`SKPayment`](https://developer.apple.com/documentation/storekit/skpayment) object stored in the transaction’s payment property.
- `promotional_offer_id` (promotional_offer_id): The identifier of the promotional offer for an auto-renewable subscription that the user redeemed. You provide this value in the Promotional Offer Identifier field when you create the promotional offer in App Store Connect.
- `price_increase_status` (string): The status that indicates if an auto-renewable subscription is subject to a price increase. The price increase status is `"0"` when the App Store has requested consent for an auto-renewable subscription price increase that requires customer consent, and the customer hasn’t yet consented. The price increase status is `"1"` if the customer has consented to a price increase that requires customer consent. The price increase status is also `"1"` if the App Store has notified the customer of the auto-renewable subscription price increase that doesn’t require customer consent.

## See Also

- [object responseBody.Latest_receipt_info](responsebody/latest_receipt_info-data.dictionary.md)
  An array that contains all in-app purchase transactions.
- [object responseBody.Receipt](responsebody/receipt-data.dictionary.md)
  The decoded version of the encoded receipt data that you send with the request to the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/responsebody/pending_renewal_info-data.dictionary)*