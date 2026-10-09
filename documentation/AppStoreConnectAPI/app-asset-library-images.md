# App Asset Library images

**Framework**: App Store Connect API

Upload and manage image assets in an app’s asset library.

#### Overview

The `appAssetLibraryImages` resource represents an image asset in an app’s asset library that you can reuse across App Store surfaces through placements. Use it to:

- Upload a new image asset.
- Read an image asset and its review and processing state.
- Update an image asset.
- Delete an image asset.
- List the placements that reuse an image asset.

An image asset moves through a series of states as it uploads and goes through review. For image requirements, see [`Screenshot specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/screenshot-specifications).

## Topics

### Getting images and reading information
- [Read an app asset library image](get-v1-appassetlibraryimages-_id_.md)
  Get information about an app asset library image.
- [List related placements](get-v1-appassetlibraryimages-_id_-placements.md)
  List the placements that reuse an app asset library image.
- [List the placement IDs for an app asset library image](get-v1-appassetlibraryimages-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific app asset library image.
### Creating, modifying, and deleting images
- [Create an app asset library image](post-v1-appassetlibraryimages.md)
  Create an app asset library image.
- [Modify an app asset library image](patch-v1-appassetlibraryimages-_id_.md)
  Update an app asset library image.
- [Delete an app asset library image](delete-v1-appassetlibraryimages-_id_.md)
  Delete an app asset library image.
### Objects and types
- [object AppAssetLibraryImage](appassetlibraryimage.md)
  An image asset uploaded to an app’s asset library that you can reuse across App Store surfaces through placements.
- [object AppAssetLibraryImageCreateRequest](appassetlibraryimagecreaterequest.md)
  The request body you use to create an app asset library image.
- [object AppAssetLibraryImageUpdateRequest](appassetlibraryimageupdaterequest.md)
  The request body you use to update an app asset library image.
- [object AppAssetLibraryImageResponse](appassetlibraryimageresponse.md)
  The response body for endpoints that create, read, or modify an app asset library image.
- [object AppAssetLibraryImagePlacementsLinkagesResponse](appassetlibraryimageplacementslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [type AppAssetLibraryMediaType](appassetlibrarymediatype.md)
  String that represents the media type of an app asset library asset.
### Asset state attributes
- [object AppAssetLibraryImageCommonAttributes](appassetlibraryimagecommonattributes.md)
  The attributes common to an app asset library image in any state.
- [object AppAssetLibraryImageAwaitingUploadAttributes](appassetlibraryimageawaitinguploadattributes.md)
  The attributes of an app asset library image that’s in the awaiting upload state.
- [object AppAssetLibraryImageUploadCompleteAttributes](appassetlibraryimageuploadcompleteattributes.md)
  The attributes of an app asset library image that’s in the upload complete state.
- [object AppAssetLibraryImageReadyForReviewAttributes](appassetlibraryimagereadyforreviewattributes.md)
  The attributes of an app asset library image that’s in the ready for review state.
- [object AppAssetLibraryImageWaitingForReviewAttributes](appassetlibraryimagewaitingforreviewattributes.md)
  The attributes of an app asset library image that’s in the waiting for review state.
- [object AppAssetLibraryImageInReviewAttributes](appassetlibraryimageinreviewattributes.md)
  The attributes of an app asset library image that’s in the in review state.
- [object AppAssetLibraryImageAcceptedAttributes](appassetlibraryimageacceptedattributes.md)
  The attributes of an app asset library image that’s in the accepted state.
- [object AppAssetLibraryImageApprovedAttributes](appassetlibraryimageapprovedattributes.md)
  The attributes of an app asset library image that’s in the approved state.
- [object AppAssetLibraryImageRejectedAttributes](appassetlibraryimagerejectedattributes.md)
  The attributes of an app asset library image that’s in the rejected state.
- [object AppAssetLibraryImageFailedAttributes](appassetlibraryimagefailedattributes.md)
  The attributes of an app asset library image that’s in the failed state.
- [object AppAssetLibraryImageArchivedAttributes](appassetlibraryimagearchivedattributes.md)
  The attributes of an app asset library image that’s in the archived state.

## See Also

- [App Asset Library videos](app-asset-library-videos.md)
  Upload and manage video assets in an app’s asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-asset-library-images)*