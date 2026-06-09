# App availability

**Framework**: App Store Connect API

Manage territory and date settings that make your app available for pre-order.

## Topics

### Managing app and territory availability
- [Read app availability](get-v2-appavailabilities-_id_.md)
  Get information about your app’s availalbility.
- [Read app availablity territories](get-v2-appavailabilities-_id_-territoryavailabilities.md)
  Read the territory availablity for a specific app.
- [List territory availability IDs for an app availability](get-v2-appavailabilities-_id_-relationships-territoryavailabilities.md)
  Get a list of territory availability IDs for a specific app availability.
- [Create an app pre-order](post-v2-appavailabilities.md)
  Create an app pre-order and set the expected app release date.
- [Modify the territory availability for an app pre-order](patch-v1-territoryavailabilities-_id_.md)
  Update the release territories for your app pre-order.
- [End an app pre-order](post-v1-endappavailabilitypreorders.md)
  End the pre-order for your app and release to store immediately.
### Objects
- [object AppAvailabilityV2](appavailabilityv2.md)
  The territory availability configuration for an app, specifying which App Store territories it’s available in and the release date settings.
- [object AppAvailabilityV2CreateRequest](appavailabilityv2createrequest.md)
  The request body you use to create an app availability.
- [object AppAvailabilityV2Response](appavailabilityv2response.md)
  The response body for endpoints that read or modify the availability settings for an app.
- [object AppAppAvailabilityV2LinkageResponse](appappavailabilityv2linkageresponse.md)
- [object TerritoryAvailability](territoryavailability.md)
  The availability setting for an app or content in a specific App Store territory, including release date configuration.
- [object TerritoryAvailabilitiesResponse](territoryavailabilitiesresponse.md)
  The response body for endpoints that list an app’s availability across territories.
- [object TerritoryAvailabilityInlineCreate](territoryavailabilityinlinecreate.md)
  The request body you use to create a territory availability.
- [object TerritoryAvailabilityResponse](territoryavailabilityresponse.md)
  The response body for endpoints that read or modify an app’s availability in a single territory.
- [object TerritoryAvailabilityUpdateRequest](territoryavailabilityupdaterequest.md)
  The request body for updating the availability settings for an app or content in a specific territory.
- [object EndAppAvailabilityPreOrder](endappavailabilitypreorder.md)
  A request action to end an active pre-order and immediately make an app available for download.
- [object EndAppAvailabilityPreOrderCreateRequest](endappavailabilitypreordercreaterequest.md)
  The request body you use to end an app’s preorder availability.
- [object EndAppAvailabilityPreOrderResponse](endappavailabilitypreorderresponse.md)
  A response confirming that an app’s pre-order period has ended and the app is now available.

## See Also

- [App Store Version Phased Releases](app-store-version-phased-releases.md)
  Manage phased releases of updates to your app.
- [App Store Version Release Requests](app-store-version-release-requests.md)
  Manually release an App Store approved version of your app to the App Store.
- [App Pre-Orders](app-pre-orders.md)
  Manage the settings that make your app available for pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-availability)*