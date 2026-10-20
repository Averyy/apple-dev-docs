# AppEventVideoClip.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe an app event video clip resource.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```swift
object AppEventVideoClip.Attributes
```

## Mentions

- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)

## Properties

- `appEventAssetType` (AppEventAssetType)
- `assetDeliveryState` (AppMediaAssetState): This attribute is deprecated. Use [`AppMediaVideoState`](appmediavideostate.md) instead.
- `fileName` (string)
- `fileSize` (integer)
- `previewFrameImage` (PreviewFrameImage)
- `previewFrameTimeCode` (string)
- `previewImage` (ImageAsset): This attribute is deprecated. Use [`PreviewFrameImage`](previewframeimage.md) instead.
- `uploadOperations` ([UploadOperation])
- `videoDeliveryState` (AppMediaVideoState)
- `videoUrl` (string)

## See Also

- [object AppEventVideoClip.Relationships](appeventvideoclip/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appeventvideoclip/attributes-data.dictionary)*