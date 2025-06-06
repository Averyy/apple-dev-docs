# renewalDate

**Framework**: App Store Server API  
**Kind**: typealias

The UNIX time, in milliseconds, when the most recent auto-renewable subscription purchase expires.

**Availability**:
- App Store Server API 1.8+

## Declaration

```swift
timestamp renewalDate
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The `renewalDate` is a value that’s always present in the payload for auto-renewable subscriptions, even for expired subscriptions. This date indicates the expiration date of the most recent auto-renewable subscription purchase, including renewals, and may be in the past. For subscriptions that renew successfully, the [`renewalDate`](renewaldate.md) is the date when the subscription renews.

## See Also

- [type autoRenewStatus](autorenewstatus.md)
  The renewal status for an auto-renewable subscription.
- [type autoRenewProductId](autorenewproductid.md)
  The identifier of the product that renews at the next billing period.
- [type expirationIntent](expirationintent.md)
  The reason an auto-renewable subscription expired.
- [type expiresDate](expiresdate.md)
  The UNIX time, in milliseconds, an auto-renewable subscription purchase expires or renews.
- [type isUpgraded](isupgraded.md)
  The Boolean value that indicates whether the customer upgraded to another subscription.
- [type renewalPrice](renewalprice.md)
  The renewal price, in milliunits, of the auto-renewable subscription that renews at the next billing period.
- [type status](status.md)
  The status of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/renewaldate)*