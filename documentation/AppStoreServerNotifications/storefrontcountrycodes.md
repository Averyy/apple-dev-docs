# storefrontCountryCodes

**Framework**: App Store Server Notifications  
**Kind**: typealias

A list of storefront country codes for limiting the storefronts for a subscription-renewal-date extension.

**Availability**:
- App Store Server Notifications 2.7+

## Declaration

```swift
[storefrontCountryCode] storefrontCountryCodes
```

#### Discussion

If you provide a list of storefronts when you call the [`Extend Subscription Renewal Dates for All Active Subscribers`](https://developer.apple.com/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) endpoint, the notification returns only those storefronts. If you don’t use the `storefrontCountryCodes`, the subscription-renewal-date extension applies to all storefronts.

For information about providing the list of storefronts, see [`MassExtendRenewalDateRequest`](https://developer.apple.com/documentation/AppStoreServerAPI/MassExtendRenewalDateRequest).

## See Also

- [type requestIdentifier](requestidentifier.md)
  A string that contains a unique identifier for a subscription-renewal-date extension request.
- [type environment](environment.md)
  The server environment, either sandbox or production.
- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type productId](productid.md)
  The product identifier of the In-App Purchase.
- [type storefrontCountryCode](storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront.
- [type failedCount](failedcount.md)
  The count of subscriptions that fail to receive a subscription-renewal-date extension.
- [type succeededCount](succeededcount.md)
  The count of subscriptions that successfully receive a subscription-renewal-date extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/storefrontcountrycodes)*