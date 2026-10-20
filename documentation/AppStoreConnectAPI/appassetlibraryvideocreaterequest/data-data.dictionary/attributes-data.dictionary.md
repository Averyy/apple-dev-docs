# AppAssetLibraryVideoCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The attributes you set that describe the new app asset library video resource.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```
object AppAssetLibraryVideoCreateRequest.Data.Attributes
```

## Properties

- `category` (AppAssetLibraryAssetCategory) *(required)*: The category that determines how you can use the asset across your App Store content.
- `fileName` (string) *(required)*: The name of the asset file you upload.
- `fileSize` (int64) *(required)*: The size, in bytes, of the asset file.

  **Minimum**: `1`; **Maximum**: `9007199254740991`
- `previewFrameTimeCode` (string): The timecode of the video frame to use as the preview image.
- `referenceName` (string): A name that identifies the asset within its asset library.

## See Also

### Objects
- [object AppAssetLibraryVideoCreateRequest.Data.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryvideocreaterequest/data-data.dictionary/attributes-data.dictionary)*