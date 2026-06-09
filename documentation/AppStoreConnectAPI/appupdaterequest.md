# AppUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update an App Update.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppUpdateRequest
```

## Topics

### Objects
- [object AppUpdateRequest.Data](appupdaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (AppUpdateRequest.Data) *(required)*

## See Also

- [object App](app.md)
  An app registered in App Store Connect, representing all versions, metadata, and configuration for your iOS, macOS, tvOS, or watchOS application.
- [object AppWithoutIncludesResponse](appwithoutincludesresponse.md)
  A response containing a single app, without including related resources.
- [object AppsWithoutIncludesResponse](appswithoutincludesresponse.md)
  A response containing a list of apps, without including related resources.
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
- [object AppPricePointV3](apppricepointv3.md)
  A specific price tier in App Store pricing, defining the customer price and developer proceeds across territories.
- [object AppPricePointV3Response](apppricepointv3response.md)
  A response containing a single App Store price point with its territory-specific pricing details.
- [object AppPricePointsV3Response](apppricepointsv3response.md)
  A response containing a list of available App Store price points.
- [object AppPriceSchedule](apppriceschedule.md)
  The pricing schedule for an app, specifying base territory prices, manual prices for other territories, and scheduled price changes.
- [object AppPriceScheduleCreateRequest](apppriceschedulecreaterequest.md)
  The request body you use to create an app price schedule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appupdaterequest)*