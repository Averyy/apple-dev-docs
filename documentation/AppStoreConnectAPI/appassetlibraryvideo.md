# AppAssetLibraryVideo

**Framework**: App Store Connect API  
**Kind**: dictionary

A video asset uploaded to an app’s asset library that you can reuse across App Store surfaces through placements.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibraryVideo
```

## Mentions

- [Placing assets on your App Store surfaces](placing-assets-on-your-app-store-surfaces.md)

## Topics

### Objects
- [object AppAssetLibraryVideo.Relationships](appassetlibraryvideo/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `attributes` (*)
- `relationships` (AppAssetLibraryVideo.Relationships)
- `links` (ResourceLinks)

## See Also

- [type AppAssetLibraryMediaType](appassetlibrarymediatype.md)
  String that represents the media type of an app asset library asset.
- [object AppAssetLibraryVideoCreateRequest](appassetlibraryvideocreaterequest.md)
  The request body you use to create an app asset library video.
- [object AppAssetLibraryVideoUpdateRequest](appassetlibraryvideoupdaterequest.md)
  The request body you use to update an app asset library video.
- [object AppAssetLibraryVideoResponse](appassetlibraryvideoresponse.md)
  The response body for endpoints that create, read, or modify an app asset library video.
- [object AppAssetLibraryVideoPlacementsLinkagesResponse](appassetlibraryvideoplacementslinkagesresponse.md)
  A response body that contains a list of related resource IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryvideo)*