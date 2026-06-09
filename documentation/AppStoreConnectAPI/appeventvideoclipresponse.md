# AppEventVideoClipResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify an in-app event video clip.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEventVideoClipResponse
```

## Properties

- `data` (AppEventVideoClip) *(required)*
- `included` ([AppEventLocalization])
- `links` (DocumentLinks) *(required)*

## See Also

- [object AppEventVideoClip](appeventvideoclip.md)
  A video clip used to promote an app event on the App Store product page.
- [object AppEventVideoClipCreateRequest](appeventvideoclipcreaterequest.md)
  The request body you use to create an app event video clip.
- [object AppEventVideoClipUpdateRequest](appeventvideoclipupdaterequest.md)
  The request body you use to update an app event video clip update request.
- [object AppEventVideoClipsResponse](appeventvideoclipsresponse.md)
  The response body for endpoints that list video clips for an in-app event localization.
- [object PreviewFrameImage](previewframeimage.md)
  The properties that describe a preview frame image for an app preview or app event video.
- [object AppMediaVideoState](appmediavideostate.md)
  The properties that describe the state of an app preview or app event video.
- [object AppMediaPreviewFrameImageState](appmediapreviewframeimagestate.md)
  The properties that describe the state of a preview frame image for an app preveiew or app event video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventvideoclipresponse)*