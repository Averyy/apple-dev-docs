# renewalDate

**Framework**: App Store Server Notifications  
**Kind**: typealias

The UNIX time, in milliseconds, when the most recent auto-renewable subscription purchase expires.

**Availability**:
- App Store Server Notifications 2.8+

## Declaration

```swift
timestamp renewalDate
```

#### Discussion

The `renewalDate` is a value that’s always present in the payload for auto-renewable subscriptions, even for expired subscriptions. This date indicates the expiration date of the most recent auto-renewable subscription purchase, including renewals, and may be in the past. For subscriptions that renew successfully, the `renewalDate` is the date when the subscription renews.

## See Also

- [type autoRenewStatus](autorenewstatus.md)
  The renewal status for an auto-renewable subscription.
- [type autoRenewProductId](autorenewproductid.md)
  The identifier of the product that renews at the next billing period.
- [type expirationIntent](expirationintent.md)
  The reason a subscription expired.
- [type expiresDate](expiresdate.md)
  The UNIX time, in milliseconds, an auto-renewable subscription purchase expires or renews.
- [type isUpgraded](isupgraded.md)
  A Boolean value that indicates whether the customer upgraded to another subscription.
- [type renewalPrice](renewalprice.md)
  The renewal price, in milliunits, of the auto-renewable subscription that renews at the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/renewaldate)*