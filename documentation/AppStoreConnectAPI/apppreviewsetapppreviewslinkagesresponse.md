# AppPreviewSetAppPreviewsLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response body that contains a list of related resource IDs.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This object is deprecated. Use [`AppAssetLibraryPlacement`](./appassetlibraryplacement.md) instead.

## Declaration

```
object AppPreviewSetAppPreviewsLinkagesResponse
```

## Topics

### Objects
- [object AppPreviewSetAppPreviewsLinkagesResponse.Data](./apppreviewsetapppreviewslinkagesresponse/data-data.dictionary.md)
  The data element of the response body.

## Properties

- `data` ([AppPreviewSetAppPreviewsLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object AppPreviewSet](./apppreviewset.md)
  The data structure that represent an App Preview Sets resource.
- [object AppPreviewSetCreateRequest](./apppreviewsetcreaterequest.md)
  The request body you use to create an App Preview Set.
- [object AppPreviewSetResponse](./apppreviewsetresponse.md)
  The response body for endpoints that create or read a set of app preview videos for a display size.
- [object AppPreviewSetsResponse](./apppreviewsetsresponse.md)
  The response body for endpoints that list app preview sets for an App Store version localization.
- [object AppPreviewSetAppPreviewsLinkagesRequest](./apppreviewsetapppreviewslinkagesrequest.md)
  A request body you use to reorder the app previews in a preview set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppreviewsetapppreviewslinkagesresponse)*