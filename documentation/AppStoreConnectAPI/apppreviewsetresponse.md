# AppPreviewSetResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create or read a set of app preview videos for a display size.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This object is deprecated. Use [`AppAssetLibraryPlacementResponse`](./appassetlibraryplacementresponse.md) instead.

## Declaration

```
object AppPreviewSetResponse
```

## Properties

- `data` (AppPreviewSet) *(required)*
- `included` ([*]): **Allowed Types**: `AppCustomProductPageLocalization`, `AppPreview`, `AppStoreVersionExperimentTreatmentLocalization`, `AppStoreVersionLocalization`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object AppPreviewSet](./apppreviewset.md)
  The data structure that represent an App Preview Sets resource.
- [object AppPreviewSetCreateRequest](./apppreviewsetcreaterequest.md)
  The request body you use to create an App Preview Set.
- [object AppPreviewSetsResponse](./apppreviewsetsresponse.md)
  The response body for endpoints that list app preview sets for an App Store version localization.
- [object AppPreviewSetAppPreviewsLinkagesRequest](./apppreviewsetapppreviewslinkagesrequest.md)
  A request body you use to reorder the app previews in a preview set.
- [object AppPreviewSetAppPreviewsLinkagesResponse](./apppreviewsetapppreviewslinkagesresponse.md)
  A response body that contains a list of related resource IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppreviewsetresponse)*