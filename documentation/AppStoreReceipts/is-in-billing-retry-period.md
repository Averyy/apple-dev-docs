# is_in_billing_retry_period

**Framework**: App Store Receipts  
**Kind**: typealias

An indicator of whether an auto-renewable subscription is in the billing retry period.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
string is_in_billing_retry_period
```

#### Discussion

This field is returned in the JSON response, in the [`responseBody.Pending_renewal_info`](responsebody/pending_renewal_info-data.dictionary.md) array.

This field indicates whether Apple is attempting to renew an expired subscription automatically. If the customer’s subscription failed to renew because the App Store was unable to complete the transaction, this value reflects whether the App Store is still trying to renew the subscription.

The subscription retry flag is solely indicative of whether a subscription is in a billing retry state. Use this value in conjunction with `expiration_intent`, `expires_date`, and `transaction_id` for more insight.

You can use this field to:

- Determine that the user has been billed successfully, if this field has been removed and there is a new transaction with a future `expires_date`.
- Inform the user that there may be an issue with their billing information, if the value is `“1”`. For example, an expired credit card or insufficient balance could prevent this customer’s account from being billed.
- Implement a grace period to improve recovery, if the value is `“1”` and the `expires_date` is in the past. A grace period is free or limited subscription access while a subscriber is in a billing retry state. See [`Engineering Subscriptions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2018/705/) from WWDC 2018 for more information.

## See Also

- [type status](status.md)
  The status of the app receipt.
- [type auto_renew_status](auto_renew_status.md)
  The renewal status for the auto-renewable subscription.
- [type is_in_intro_offer_period](is_in_intro_offer_period.md)
  An indicator of whether an auto-renewable subscription is in the introductory price period.
- [type is_trial_period](is_trial_period.md)
  An indicator of whether an auto-renewable subscription is in the free trial period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/is_in_billing_retry_period)*