# AppAssetLibraryPlacementOrderingRequest

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A request that sets the display order of an app’s asset library placements within a localization.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object AppAssetLibraryPlacementOrderingRequest
```

## Topics

### Objects
- [object AppAssetLibraryPlacementOrderingRequest.Relationships](./appassetlibraryplacementorderingrequest/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: **Allowed Values**: `appAssetLibraryPlacementOrderingRequests`
- `id` (string) *(required)*
- `relationships` (AppAssetLibraryPlacementOrderingRequest.Relationships)
- `links` (ResourceLinks)

## See Also

### Objects and types
- [object AppAssetLibraryPlacementOrderingRequestCreateRequest](./appassetlibraryplacementorderingrequestcreaterequest.md)
  The request body you use to create an app asset library placement ordering request.
- [object AppAssetLibraryPlacementOrderingRequestResponse](./appassetlibraryplacementorderingrequestresponse.md)
  The response body for endpoints that create an app asset library placement ordering request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryplacementorderingrequest)*