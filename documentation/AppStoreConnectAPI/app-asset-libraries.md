# App Asset Libraries

**Framework**: App Store Connect API

Read an app’s library of reusable image and video assets.

#### Overview

The `appAssetLibraries` resource represents an app’s library of reusable image and video assets. Use it to:

- Read an app’s asset library.
- List the image assets in the library.
- List the video assets in the library.

Each app has a single asset library. Read it through the app’s `assetLibrary` relationship, then list its assets to place them across your App Store surfaces.

## Topics

### Getting an asset library
- [Read an app asset library](get-v1-appassetlibraries-_id_.md)
  Get information about an app’s asset library.
### Getting assets in a library
- [List related images](get-v1-appassetlibraries-_id_-images.md)
  List the image assets in an app’s asset library.
- [List related videos](get-v1-appassetlibraries-_id_-videos.md)
  List the video assets in an app’s asset library.
- [List the image IDs for an app asset library](get-v1-appassetlibraries-_id_-relationships-images.md)
  Get a list of image asset resource IDs for a specific asset library.
- [List the video IDs for an app asset library](get-v1-appassetlibraries-_id_-relationships-videos.md)
  Get a list of video asset resource IDs for a specific asset library.
### Objects and types
- [object AppAssetLibrary](appassetlibrary.md)
  The per-app library that holds an app’s reusable image and video assets.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-asset-libraries)*