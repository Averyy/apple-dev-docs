# Territories

**Framework**: App Store Connect API

Get a list of active App Store storefronts in which you make your app available.

#### Overview

Use `territories` to get a list of active App Store storefronts in which to make your app available to customers. This is a read-only resource.

For more information see [`Set availability for your app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-your-apps-availability/select-regions).

## Topics

### Getting Territories
- [List Territories](get-v1-territories.md)
  List all territories where the App Store operates.
- [List All Territories for an End User License Agreement](get-v1-enduserlicenseagreements-_id_-territories.md)
  List all the App Store territories to which a specific custom app license agreement applies.
- [GET /v1/endUserLicenseAgreements/{id}/relationships/territories](get-v1-enduserlicenseagreements-_id_-relationships-territories.md)
### Objects
- [object Territory](territory.md)
  The data structure that represents a Territories resource.
- [object TerritoryResponse](territoryresponse.md)
  A response that contains a single Territories resource.
- [object TerritoriesWithoutIncludesResponse](territorieswithoutincludesresponse.md)
- [object TerritoriesResponse](territoriesresponse.md)
  A response that contains a list of Territory resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/territories)*