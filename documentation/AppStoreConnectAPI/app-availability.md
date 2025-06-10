# App availability

**Framework**: App Store Connect API

Manage territory and date settings that make your app available for pre-order.

## Topics

### Managing app and territory availability
- [Read App Availabilty](get-v2-appavailabilities-_id_.md)
  Get information about your app’s availalbility.
- [Read App Availablity Territories](get-v2-appavailabilities-_id_-territoryavailabilities.md)
  Read the territory availablity for a specific app.
- [GET /v2/appAvailabilities/{id}/relationships/territoryAvailabilities](get-v2-appavailabilities-_id_-relationships-territoryavailabilities.md)
- [Create an App Pre-Order](post-v2-appavailabilities.md)
  Create an app pre-order and set the expected app release date.
- [Modify the Territory Availabilty for an App Pre-Order](patch-v1-territoryavailabilities-_id_.md)
  Update the release territories for your app pre-order.
- [End an App Pre-Order](post-v1-endappavailabilitypreorders.md)
  End the pre-order for your app and release to store immediately.
### Objects
- [object AppAvailabilityV2](appavailabilityv2.md)
  The data structure that represents an app availability resource.
- [object AppAvailabilityV2CreateRequest](appavailabilityv2createrequest.md)
  The request body you use to create an app availability.
- [object AppAvailabilityV2Response](appavailabilityv2response.md)
  A response that contains a single app availability resource.
- [object AppAppAvailabilityV2LinkageResponse](appappavailabilityv2linkageresponse.md)
- [object TerritoryAvailability](territoryavailability.md)
  The data structure that represents a territory availability resource.
- [object TerritoryAvailabilitiesResponse](territoryavailabilitiesresponse.md)
  A response that contains a list of territory availability resources.
- [object TerritoryAvailabilityInlineCreate](territoryavailabilityinlinecreate.md)
  The request body you use to create a territory availability.
- [object TerritoryAvailabilityResponse](territoryavailabilityresponse.md)
  A response that contains a single territory availability resource.
- [object TerritoryAvailabilityUpdateRequest](territoryavailabilityupdaterequest.md)
  The request body you use to update a single territory availability resource.
- [object EndAppAvailabilityPreOrder](endappavailabilitypreorder.md)
  The data structure that represents the ending of an app preorder resource.
- [object EndAppAvailabilityPreOrderCreateRequest](endappavailabilitypreordercreaterequest.md)
  The request body you use to end an app’s preorder availability.
- [object EndAppAvailabilityPreOrderResponse](endappavailabilitypreorderresponse.md)
  A response that contains a single end app availability resource.

## See Also

- [App Store Version Phased Releases](app-store-version-phased-releases.md)
  Manage phased releases of updates to your app.
- [App Store Version Release Requests](app-store-version-release-requests.md)
  Manually release an App Store approved version of your app to the App Store.
- [App Pre-Orders](app-pre-orders.md)
  Manage the settings that make your app available for pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-availability)*