# expirationIntent

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The reason an auto-renewable subscription expired.

**Availability**:
- App Store Server API 1.0+

## Declaration

```
int32 expirationIntent
```

## Possible Values

- `1`: The customer canceled their subscription.
- `2`: Billing error; for example, the customer’s payment information is no longer valid.
- `3`: The customer didn’t consent to an auto-renewable subscription price increase that requires their consent, or to a subscription offer conversion that requires their consent, so the subscription expired. For more information about subscription price increases that require customer consent, see [Auto-renewable subscription price increase thresholds](https://developer.apple.com/help/app-store-connect/reference/auto-renewable-subscription-price-increase-thresholds). For more information about offer conversions that require customer consent, see [Consent for subscription offer conversions](https://developer.apple.com/help/app-store-connect/reference/consent-for-subscription-offer-conversions).
- `4`: The product wasn’t available for purchase at the time of renewal.
- `5`: The subscription expired for some other reason.

## See Also

### Subscription renewal and expiration
- [type autoRenewStatus](./autorenewstatus.md)
  The renewal status for an auto-renewable subscription.
- [type autoRenewProductId](./autorenewproductid.md)
  The identifier of the product that renews at the next billing period.
- [type billingPlanType](./billingplantype.md)
- [type expiresDate](./expiresdate.md)
  The UNIX time, in milliseconds, an auto-renewable subscription purchase expires or renews.
- [type isUpgraded](./isupgraded.md)
  The Boolean value that indicates whether the customer upgraded to another subscription.
- [type renewalBillingPlanType](./renewalbillingplantype.md)
- [type renewalDate](./renewaldate.md)
  The UNIX time, in milliseconds, when the most recent auto-renewable subscription purchase expires.
- [type renewalPrice](./renewalprice.md)
  The renewal price, in milliunits, of the auto-renewable subscription that renews at the next billing period.
- [type status](./status.md)
  The status of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/expirationintent)*