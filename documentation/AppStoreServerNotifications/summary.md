# summary

**Framework**: App Store Server Notifications  
**Kind**: dictionary

The payload data for a subscription-renewal-date extension notification.

**Availability**:
- App Store Server Notifications 2.7+

## Declaration

```swift
object summary
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

The `summary` object appears in the [`responseBodyV2DecodedPayload`](responsebodyv2decodedpayload.md) when the [`notificationType`](notificationtype.md) is `RENEWAL_EXTENSION` and the [`subtype`](subtype.md) is `SUMMARY`. This notification occurs when the App Store completes your request to extend the subscription renewal date for eligible subscribers. For more information about this request, see [`Extend Subscription Renewal Dates for All Active Subscribers`](https://developer.apple.com/documentation/AppStoreServerAPI/Extend-Subscription-Renewal-Dates-for-All-Active-Subscribers) in the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI).

## Topics

### Data types
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
- [type storefrontCountryCodes](storefrontcountrycodes.md)
  A list of storefront country codes for limiting the storefronts for a subscription-renewal-date extension.
- [type storefrontCountryCode](storefrontcountrycode.md)
  The three-letter code that represents the country or region associated with the App Store storefront.
- [type failedCount](failedcount.md)
  The count of subscriptions that fail to receive a subscription-renewal-date extension.
- [type succeededCount](succeededcount.md)
  The count of subscriptions that successfully receive a subscription-renewal-date extension.

## See Also

- [object data](data.md)
  The payload data that contains app metadata and the signed renewal and transaction information.
- [object appData](appdata.md)
  The object that contains the app metadata and signed app transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/summary)*