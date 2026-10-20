# SubscriptionStatusUrlVersion

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

Strings that represent versions of App Store Server Notifications.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```
string SubscriptionStatusUrlVersion
```

## Possible Values

- `V1`: Represents version 1 of App Store Server Notifications, and indicates you receive notifications on your server at the  [App Store Server Notifications V1](../AppStoreServerNotifications/app-store-server-notifications-v1.md) endpoint.  Note that App Store Server Notifications V1 are deprecated.
- `V2`: Represents version 2 of App Store Server Notifications, and indicates you receive notifications on your server at the [App Store Server Notifications V2](../AppStoreServerNotifications/app-store-server-notifications-v2.md) endpoint.

## Mentions

- [App Store Connect API 3.0 release notes](./app-store-connect-api-3-0-release-notes.md)
- [App Store Connect API 3.6 release notes](./app-store-connect-api-3-6-release-notes.md)

#### Discussion

For more infomation see [Enabling App Store Server Notifications](../AppStoreServerNotifications/enabling-app-store-server-notifications.md).

## See Also

### Objects and data types
- [object App](./app.md)
  An app registered in App Store Connect, representing all versions, metadata, and configuration for your iOS, macOS, tvOS, or watchOS application.
- [object AppWithoutIncludesResponse](./appwithoutincludesresponse.md)
  A response containing a single app, without including related resources.
- [object AppsWithoutIncludesResponse](./appswithoutincludesresponse.md)
  A response containing a list of apps, without including related resources.
- [object AppUpdateRequest](./appupdaterequest.md)
  The request body you use to update an App Update.
- [object AppClipsResponse](./appclipsresponse.md)
  The response body for endpoints that list App Clips for an app.
- [object AppResponse](./appresponse.md)
  The response body for endpoints that read or modify a single app in your team.
- [object AppsResponse](./appsresponse.md)
  A response containing a list of apps registered in your App Store Connect team.
- [object InAppPurchase](./inapppurchase.md)
  A one-time purchasable item available in an app, such as a consumable, non-consumable, or non-renewing subscription.
- [object InAppPurchaseResponse](./inapppurchaseresponse.md)
  The response body for endpoints that read a single In-App Purchase.
- [object InAppPurchasesResponse](./inapppurchasesresponse.md)
  The response body for endpoints that list In-App Purchases for an app.
- [object AppBetaTestersLinkagesRequest](./appbetatesterslinkagesrequest.md)
  A request body you use to remove beta testers from an app.
- [object AppPricePointV3](./apppricepointv3.md)
  A specific price tier in App Store pricing, defining the customer price and developer proceeds across territories.
- [object AppPricePointV3Response](./apppricepointv3response.md)
  A response containing a single App Store price point with its territory-specific pricing details.
- [object AppPricePointsV3Response](./apppricepointsv3response.md)
  A response containing a list of available App Store price points.
- [object AppPriceSchedule](./apppriceschedule.md)
  The pricing schedule for an app, specifying base territory prices, manual prices for other territories, and scheduled price changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionstatusurlversion)*