# renewalPrice

**Framework**: App Store Server Notifications  
**Kind**: typealias

The renewal price, in milliunits, of the auto-renewable subscription that renews at the next billing period.

**Availability**:
- App Store Server Notifications 2.12+

## Declaration

```swift
int64 renewalPrice
```

#### Discussion

This value represents the renewal price, in milliunits of the [`currency`](currency.md), of the auto-renewable subscription. One unit of the currency equals 1000 milliunits.

If the next billing period includes an offer specified by the [`offerIdentifier`](offeridentifier.md), the [`renewalPrice`](renewalprice.md) value reflects the discount.

> ❗ **Important**:  For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

To determine the storefront, use the [`storefront`](storefront.md) value in the transaction. Don’t use the [`currency`](currency.md) value to infer the storefront.

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
  A Boolean value that indicates whether the customer upgraded to another subscription.
- [type renewalDate](renewaldate.md)
  The UNIX time, in milliseconds, when the most recent auto-renewable subscription purchase expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/renewalprice)*