# AppAssetLibraryRefDataResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that list app asset library reference data.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object AppAssetLibraryRefDataResponse
```

## Properties

- `data` ([AppAssetLibraryRefDatum]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects and types
- [object AppAssetLibraryRefDatum](./appassetlibraryrefdatum.md)
  Reference data that describes the valid asset specifications, placement groups, and limits for the asset library.
- [object AppAssetLibraryRefDatumResponse](./appassetlibraryrefdatumresponse.md)
  The response body for endpoints that read an app asset library reference data resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryrefdataresponse)*