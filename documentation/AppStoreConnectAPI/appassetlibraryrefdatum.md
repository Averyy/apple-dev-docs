# AppAssetLibraryRefDatum

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Reference data that describes the valid asset specifications, placement groups, and limits for the asset library.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object AppAssetLibraryRefDatum
```

## Mentions

- [Discovering asset specifications](./discovering-asset-specifications.md)

## Topics

### Objects
- [object AppAssetLibraryRefDatum.Attributes](./appassetlibraryrefdatum/attributes-data.dictionary.md)
  Attributes that describe an app asset library reference data resource.

## Properties

- `type` (string) *(required)*: **Allowed Values**: `appAssetLibraryRefData`
- `id` (string) *(required)*
- `attributes` (AppAssetLibraryRefDatum.Attributes)
- `links` (ResourceLinks)

## See Also

### Objects and types
- [object AppAssetLibraryRefDataResponse](./appassetlibraryrefdataresponse.md)
  The response body for endpoints that list app asset library reference data.
- [object AppAssetLibraryRefDatumResponse](./appassetlibraryrefdatumresponse.md)
  The response body for endpoints that read an app asset library reference data resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryrefdatum)*