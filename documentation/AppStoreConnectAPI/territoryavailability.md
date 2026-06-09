# TerritoryAvailability

**Framework**: App Store Connect API  
**Kind**: dictionary

The availability setting for an app or content in a specific App Store territory, including release date configuration.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object TerritoryAvailability
```

## Topics

### Objects
- [object TerritoryAvailability.Attributes](territoryavailability/attributes-data.dictionary.md)
  The attributes that describe a territory availability resource.
- [object TerritoryAvailability.Relationships](territoryavailability/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (TerritoryAvailability.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (TerritoryAvailability.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppAvailabilityV2](appavailabilityv2.md)
  The territory availability configuration for an app, specifying which App Store territories it’s available in and the release date settings.
- [object AppAvailabilityV2CreateRequest](appavailabilityv2createrequest.md)
  The request body you use to create an app availability.
- [object AppAvailabilityV2Response](appavailabilityv2response.md)
  The response body for endpoints that read or modify the availability settings for an app.
- [object AppAppAvailabilityV2LinkageResponse](appappavailabilityv2linkageresponse.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/territoryavailability)*