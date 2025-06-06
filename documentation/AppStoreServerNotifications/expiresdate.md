# expiresDate

**Framework**: App Store Server Notifications  
**Kind**: typealias

The UNIX time, in milliseconds, an auto-renewable subscription purchase expires or renews.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
timestamp expiresDate
```

#### Discussion

The `expiresDate` is a static value that applies for each transaction. When the auto-renewable subscription renews, the App Store creates a new transaction with a new `expiresDate`.

## See Also

- [type autoRenewStatus](autorenewstatus.md)
  The renewal status for an auto-renewable subscription.
- [type autoRenewProductId](autorenewproductid.md)
  The identifier of the product that renews at the next billing period.
- [type expirationIntent](expirationintent.md)
  The reason a subscription expired.
- [type isUpgraded](isupgraded.md)
  A Boolean value that indicates whether the customer upgraded to another subscription.
- [type renewalDate](renewaldate.md)
  The UNIX time, in milliseconds, when the most recent auto-renewable subscription purchase expires.
- [type renewalPrice](renewalprice.md)
  The renewal price, in milliunits, of the auto-renewable subscription that renews at the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/expiresdate)*