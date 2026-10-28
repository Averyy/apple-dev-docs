# expiration_intent

**Framework**: App Store Receipts  
**Kind**: typealias  
**Role**: Type

The reason a subscription expires.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

## Declaration

```
string expiration_intent
```

## Possible Values

- `1`: The customer canceled their subscription.
- `2`: Billing error; for example, the customer’s payment information is no longer valid.
- `3`: The customer didn’t consent to an auto-renewable subscription price increase that requires customer consent, allowing the subscription to expire.
- `4`: The product wasn’t available for purchase at the time of renewal.
- `5`: The subscription expired for some other reason.

## Discussion

This field is returned in the JSON response, in the [`responseBody.Pending_renewal_info`](./responsebody/pending_renewal_info-data.dictionary.md) array.

You can use this value to do the following:

- If the value is `"1"`, decide whether to survey the subscribers who have opted in to an account on your system or show alternative subscription products within the same group. Decide whether to present a subscription offer to win back the user.
- If the value is `"2"`, decide whether to show the same or alternative subscription products because the user didn’t actively make the choice to unsubscribe.

For more information, see [Engineering Subscriptions](https://developer.apple.com/videos/play/wwdc2018/705/) from WWDC 2018 and [Implementing promotional offers in your app](../StoreKit/implementing-promotional-offers-in-your-app.md).

## See Also

### Dates and intent
- [type cancellation_date_ms](./cancellation_date_ms.md)
  The time and date that the App Store refunds a transaction or revokes it from Family Sharing.
- [type expires_date_ms](./expires_date_ms.md)
  The time, in milliseconds, a subscription expires or renews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/expiration_intent)*