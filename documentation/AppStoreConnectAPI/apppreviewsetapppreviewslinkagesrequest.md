# AppPreviewSetAppPreviewsLinkagesRequest

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A request body you use to reorder the app previews in a preview set.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 4.5

> **Deprecated**: This object is deprecated. Use [`AppAssetLibraryPlacement`](./appassetlibraryplacement.md) instead.

## Declaration

```
object AppPreviewSetAppPreviewsLinkagesRequest
```

## Topics

### Objects
- [object AppPreviewSetAppPreviewsLinkagesRequest.Data](./apppreviewsetapppreviewslinkagesrequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` ([AppPreviewSetAppPreviewsLinkagesRequest.Data]) *(required)*

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
- [object AppPreviewSetAppPreviewsLinkagesResponse](./apppreviewsetapppreviewslinkagesresponse.md)
  A response body that contains a list of related resource IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppreviewsetapppreviewslinkagesrequest)*