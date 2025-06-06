# status

**Framework**: App Store Server API  
**Kind**: typealias

The status of an auto-renewable subscription.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
int32 status
```

#### Discussion

For more information about the Billing Grace Period, see [`Enable Billing Grace Period for auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev58bda3212).

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
- [type renewalDate](renewaldate.md)
  The UNIX time, in milliseconds, when the most recent auto-renewable subscription purchase expires.
- [type renewalPrice](renewalprice.md)
  The renewal price, in milliunits, of the auto-renewable subscription that renews at the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/status)*