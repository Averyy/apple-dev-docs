# AppPreviewsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list app preview videos in a preview set.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppPreviewsResponse
```

## Properties

- `data` ([AppPreview]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)
- `included` ([AppPreviewSet])

## See Also

- [object AppPreview](apppreview.md)
  The data structure that represent an App Previews resource.
- [object AppPreviewCreateRequest](apppreviewcreaterequest.md)
  The request body you use to create an App Preview.
- [object AppPreviewUpdateRequest](apppreviewupdaterequest.md)
  The request body you use to update an App Preview.
- [object AppPreviewResponse](apppreviewresponse.md)
  The response body for endpoints that create, read, or modify an app preview video.
- [object UploadOperation](uploadoperation.md)
  Upload instructions for assets such as app previews and app screenshots.
- [type PreviewType](previewtype.md)
  String that represents the display type of an app preview.
- [object PreviewFrameImage](previewframeimage.md)
  The properties that describe a preview frame image for an app preview or app event video.
- [object AppMediaVideoState](appmediavideostate.md)
  The properties that describe the state of an app preview or app event video.
- [object AppMediaPreviewFrameImageState](appmediapreviewframeimagestate.md)
  The properties that describe the state of a preview frame image for an app preveiew or app event video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppreviewsresponse)*