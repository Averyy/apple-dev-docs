# App Asset Library videos

**Framework**: App Store Connect API

Upload and manage video assets in an app’s asset library.

#### Overview

The `appAssetLibraryVideos` resource represents a video asset in an app’s asset library that you can reuse across App Store surfaces through placements. Use it to:

- Upload a new video asset.
- Read a video asset and its review and processing state.
- Update a video asset.
- Delete a video asset.
- List the placements that reuse a video asset.

A video asset moves through a series of states as it uploads and goes through review. For video requirements, see [`App preview specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-preview-specifications).

## Topics

### Getting videos and reading information
- [Read an app asset library video](get-v1-appassetlibraryvideos-_id_.md)
  Get information about an app asset library video.
- [List related placements](get-v1-appassetlibraryvideos-_id_-placements.md)
  List the placements that reuse an app asset library video.
- [List the placement IDs for an app asset library video](get-v1-appassetlibraryvideos-_id_-relationships-placements.md)
  Get a list of placement resource IDs for a specific app asset library video.
### Creating, modifying, and deleting videos
- [Create an app asset library video](post-v1-appassetlibraryvideos.md)
  Create an app asset library video.
- [Modify an app asset library video](patch-v1-appassetlibraryvideos-_id_.md)
  Update an app asset library video.
- [Delete an app asset library video](delete-v1-appassetlibraryvideos-_id_.md)
  Delete an app asset library video.
### Objects and types
- [type AppAssetLibraryMediaType](appassetlibrarymediatype.md)
  String that represents the media type of an app asset library asset.
- [object AppAssetLibraryVideo](appassetlibraryvideo.md)
  A video asset uploaded to an app’s asset library that you can reuse across App Store surfaces through placements.
- [object AppAssetLibraryVideoCreateRequest](appassetlibraryvideocreaterequest.md)
  The request body you use to create an app asset library video.
- [object AppAssetLibraryVideoUpdateRequest](appassetlibraryvideoupdaterequest.md)
  The request body you use to update an app asset library video.
- [object AppAssetLibraryVideoResponse](appassetlibraryvideoresponse.md)
  The response body for endpoints that create, read, or modify an app asset library video.
- [object AppAssetLibraryVideoPlacementsLinkagesResponse](appassetlibraryvideoplacementslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
### Asset state attributes
- [object AppAssetLibraryVideoCommonAttributes](appassetlibraryvideocommonattributes.md)
  The attributes common to an app asset library video in any state.
- [object AppAssetLibraryVideoAwaitingUploadAttributes](appassetlibraryvideoawaitinguploadattributes.md)
  The attributes of an app asset library video that’s in the awaiting upload state.
- [object AppAssetLibraryVideoUploadCompleteAttributes](appassetlibraryvideouploadcompleteattributes.md)
  The attributes of an app asset library video that’s in the upload complete state.
- [object AppAssetLibraryVideoReadyForReviewAttributes](appassetlibraryvideoreadyforreviewattributes.md)
  The attributes of an app asset library video that’s in the ready for review state.
- [object AppAssetLibraryVideoWaitingForReviewAttributes](appassetlibraryvideowaitingforreviewattributes.md)
  The attributes of an app asset library video that’s in the waiting for review state.
- [object AppAssetLibraryVideoInReviewAttributes](appassetlibraryvideoinreviewattributes.md)
  The attributes of an app asset library video that’s in the in review state.
- [object AppAssetLibraryVideoAcceptedAttributes](appassetlibraryvideoacceptedattributes.md)
  The attributes of an app asset library video that’s in the accepted state.
- [object AppAssetLibraryVideoApprovedAttributes](appassetlibraryvideoapprovedattributes.md)
  The attributes of an app asset library video that’s in the approved state.
- [object AppAssetLibraryVideoRejectedAttributes](appassetlibraryvideorejectedattributes.md)
  The attributes of an app asset library video that’s in the rejected state.
- [object AppAssetLibraryVideoFailedAttributes](appassetlibraryvideofailedattributes.md)
  The attributes of an app asset library video that’s in the failed state.
- [object AppAssetLibraryVideoArchivedAttributes](appassetlibraryvideoarchivedattributes.md)
  The attributes of an app asset library video that’s in the archived state.

## See Also

- [App Asset Library images](app-asset-library-images.md)
  Upload and manage image assets in an app’s asset library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-asset-library-videos)*