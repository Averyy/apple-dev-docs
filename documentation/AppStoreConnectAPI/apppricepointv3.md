# AppPricePointV3

**Framework**: App Store Connect API  
**Kind**: dictionary

A specific price tier in App Store pricing, defining the customer price and developer proceeds across territories.

**Availability**:
- App Store Connect API 2.3+

## Declaration

```swift
object AppPricePointV3
```

## Mentions

- [App Store Connect API 2.3 release notes](app-store-connect-api-2-3-release-notes.md)

## Topics

### Objects
- [object AppPricePointV3.Attributes](apppricepointv3/attributes-data.dictionary.md)
  Attributes that describe an app price point v3 resource.
- [object AppPricePointV3.Relationships](apppricepointv3/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppPricePointV3.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppPricePointV3.Relationships)
- `type` (string) *(required)*

## See Also

- [object App](app.md)
  An app registered in App Store Connect, representing all versions, metadata, and configuration for your iOS, macOS, tvOS, or watchOS application.
- [object AppWithoutIncludesResponse](appwithoutincludesresponse.md)
  A response containing a single app, without including related resources.
- [object AppsWithoutIncludesResponse](appswithoutincludesresponse.md)
  A response containing a list of apps, without including related resources.
- [object AppUpdateRequest](appupdaterequest.md)
  The request body you use to update an App Update.
- [object AppClipsResponse](appclipsresponse.md)
  The response body for endpoints that list App Clips for an app.
- [object AppResponse](appresponse.md)
  The response body for endpoints that read or modify a single app in your team.
- [object AppsResponse](appsresponse.md)
  A response containing a list of apps registered in your App Store Connect team.
- [object InAppPurchase](inapppurchase.md)
  A one-time purchasable item available in an app, such as a consumable, non-consumable, or non-renewing subscription.
- [object InAppPurchaseResponse](inapppurchaseresponse.md)
  The response body for endpoints that read a single in-app purchase.
- [object InAppPurchasesResponse](inapppurchasesresponse.md)
  The response body for endpoints that list in-app purchases for an app.
- [object AppBetaTestersLinkagesRequest](appbetatesterslinkagesrequest.md)
  A request body you use to remove beta testers from an app.
- [object AppPricePointV3Response](apppricepointv3response.md)
  A response containing a single App Store price point with its territory-specific pricing details.
- [object AppPricePointsV3Response](apppricepointsv3response.md)
  A response containing a list of available App Store price points.
- [object AppPriceSchedule](apppriceschedule.md)
  The pricing schedule for an app, specifying base territory prices, manual prices for other territories, and scheduled price changes.
- [object AppPriceScheduleCreateRequest](apppriceschedulecreaterequest.md)
  The request body you use to create an app price schedule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppricepointv3)*