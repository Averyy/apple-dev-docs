# AppPreviewSetsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list app preview sets for an App Store version localization.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppPreviewSetsResponse
```

## Properties

- `data` ([AppPreviewSet]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppPreviewSet](apppreviewset.md)
  The data structure that represent an App Preview Sets resource.
- [object AppPreviewSetCreateRequest](apppreviewsetcreaterequest.md)
  The request body you use to create an App Preview Set.
- [object AppPreviewSetResponse](apppreviewsetresponse.md)
  The response body for endpoints that create or read a set of app preview videos for a display size.
- [object AppPreviewSetAppPreviewsLinkagesRequest](apppreviewsetapppreviewslinkagesrequest.md)
  A request body you use to reorder the app previews in a preview set.
- [object AppPreviewSetAppPreviewsLinkagesResponse](apppreviewsetapppreviewslinkagesresponse.md)
  A response body that contains a list of related resource IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppreviewsetsresponse)*