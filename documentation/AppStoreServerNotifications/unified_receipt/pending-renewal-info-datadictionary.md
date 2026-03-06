# unified_receipt.Pending_renewal_info

**Framework**: App Store Server Notifications  
**Kind**: dictionary

An array of elements that refers to open auto-renewable subscription renewals or ones that failed in the past.

**Availability**:
- App Store Server Notifications 1.2+

## Declaration

```swift
object unified_receipt.Pending_renewal_info
```

## Properties

- `auto_renew_product_id` (string): The current renewal preference for the auto-renewable subscription. The value for this key corresponds to the [`productIdentifier`](https://developer.apple.com/documentation/StoreKit/SKMutablePayment/productIdentifier) property of the product that the customer’s subscription renews.
- `auto_renew_status` (string): The current renewal status for the auto-renewable subscription. For more information, see [`auto_renew_status`](https://developer.apple.com/documentation/AppStoreReceipts/auto_renew_status).
- `expiration_intent` (string): The reason a subscription expired. This field is only present for a receipt that contains an expired, auto-renewable subscription. For more information, see [`expiration_intent`](https://developer.apple.com/documentation/AppStoreReceipts/expiration_intent).
- `grace_period_expires_date` (string): The time at which the grace period for subscription renewals expires, in a date-time format similar to the ISO 8601.
- `grace_period_expires_date_ms` (string): The time at which the grace period for subscription renewals expires, in UNIX epoch time format, in milliseconds. This key is only present for apps that have Billing Grace Period enabled and when the user experiences a billing error at the time of renewal. Use this time format for processing dates.
- `grace_period_expires_date_pst` (string): The time at which the grace period for subscription renewals expires, in the Pacific Time zone.
- `is_in_billing_retry_period` (string): A flag that indicates Apple is attempting to renew an expired subscription automatically. This field is only present if an auto-renewable subscription is in the billing retry state. For more information, see [`is_in_billing_retry_period`](https://developer.apple.com/documentation/AppStoreReceipts/is_in_billing_retry_period).
- `offer_code_ref_name` (string): The reference name of a subscription offer you configured in App Store Connect. This field is present when a customer redeemed a subscription offer code. For more information, see [`offer_code_ref_name`](https://developer.apple.com/documentation/AppStoreReceipts/offer_code_ref_name).
- `original_transaction_id` (string): The transaction identifier of the original purchase.
- `price_consent_status` (string): The price consent status for a subscription price increase. This field is present only if App Store notified the customer of the price increase. The default value is `"0"` and changes to `"1"` if the customer consents.
- `product_id` (string): The unique identifier of the product purchased. You provide this value when creating the product in App Store Connect, and it corresponds to the [`productIdentifier`](https://developer.apple.com/documentation/StoreKit/SKPayment/productIdentifier) property of the [`SKPayment`](https://developer.apple.com/documentation/StoreKit/SKPayment) object stored in the transaction’s [`payment`](https://developer.apple.com/documentation/StoreKit/SKPaymentTransaction/payment) property.
- `promotional_offer_id` (string): The identifier of the promotional offer for an auto-renewable subscription that the user redeemed. You provide this value in the Promotional Offer Identifier field when you create the promotional offer in App Store Connect. For more information, see [`promotional_offer_id`](https://developer.apple.com/documentation/AppStoreReceipts/promotional_offer_id).
- `price_increase_status` (string)

## See Also

- [object unified_receipt.Latest_receipt_info](unified_receipt/latest_receipt_info-data.dictionary.md)
  An object that contains information about the latest in-app subscription transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/unified_receipt/pending_renewal_info-data.dictionary)*