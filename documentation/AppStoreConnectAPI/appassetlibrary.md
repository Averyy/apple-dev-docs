# AppAssetLibrary

**Framework**: App Store Connect API  
**Kind**: dictionary

The per-app library that holds an app’s reusable image and video assets.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibrary
```

## Topics

### Objects
- [object AppAssetLibrary.Relationships](appassetlibrary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `relationships` (AppAssetLibrary.Relationships)
- `links` (ResourceLinks)

## See Also

- [object AppAssetLibraryResponse](appassetlibraryresponse.md)
  The response body for endpoints that read an app’s asset library.
- [object AppAssetLibraryImagesResponse](appassetlibraryimagesresponse.md)
  The response body for endpoints that list the image assets in an app’s asset library.
- [object AppAssetLibraryImagesLinkagesResponse](appassetlibraryimageslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object AppAssetLibraryVideosResponse](appassetlibraryvideosresponse.md)
  The response body for endpoints that list the video assets in an app’s asset library.
- [object AppAssetLibraryVideosLinkagesResponse](appassetlibraryvideoslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type AppAssetLibraryAssetCategory](appassetlibraryassetcategory.md)
  String that represents the category of an app asset library asset.
- [type AppAssetLibraryAssetState](appassetlibraryassetstate.md)
  String that represents the state of an app asset library asset.
- [type AppAssetLibraryDisplayClass](appassetlibrarydisplayclass.md)
  String that represents the display class of an app asset library asset.
- [type AppAssetLibraryFeature](appassetlibraryfeature.md)
  String that represents the App Store feature an app asset library asset supports.
- [type AppAssetLibraryMediaType](appassetlibrarymediatype.md)
  String that represents the media type of an app asset library asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibrary)*