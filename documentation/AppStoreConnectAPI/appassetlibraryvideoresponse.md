# AppAssetLibraryVideoResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify an app asset library video.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibraryVideoResponse
```

## Properties

- `data` (AppAssetLibraryVideo) *(required)*
- `included` ([AppAssetLibraryPlacement])
- `links` (DocumentLinks) *(required)*

## See Also

- [type AppAssetLibraryMediaType](appassetlibrarymediatype.md)
  String that represents the media type of an app asset library asset.
- [object AppAssetLibraryVideo](appassetlibraryvideo.md)
  A video asset uploaded to an app’s asset library that you can reuse across App Store surfaces through placements.
- [object AppAssetLibraryVideoCreateRequest](appassetlibraryvideocreaterequest.md)
  The request body you use to create an app asset library video.
- [object AppAssetLibraryVideoUpdateRequest](appassetlibraryvideoupdaterequest.md)
  The request body you use to update an app asset library video.
- [object AppAssetLibraryVideoPlacementsLinkagesResponse](appassetlibraryvideoplacementslinkagesresponse.md)
  A response body that contains a list of related resource IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryvideoresponse)*