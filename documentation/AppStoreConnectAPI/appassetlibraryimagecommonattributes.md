# AppAssetLibraryImageCommonAttributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes common to an app asset library image in any state.

**Availability**:
- App Store Connect API 4.5+

## Declaration

```swift
object AppAssetLibraryImageCommonAttributes
```

## Properties

- `category` (AppAssetLibraryAssetCategory): The category that determines how you can use the asset across your App Store content.
- `createdDate` (date-time): The date and time when App Store Connect created the resource.
- `lastModifiedDate` (date-time): The date and time when App Store Connect last modified the resource.
- `fileName` (string): The name of the asset file you upload.
- `fileSize` (int64): The size, in bytes, of the asset file.
- `imageAsset` (ImageAsset): The uploaded image, including its dimensions and the URLs for uploading and delivering the file.
- `referenceName` (string): A name that identifies the asset within its asset library.
- `specId` (string): The identifier of the specification to which the asset conforms; App Store Connect populates this identifier after it validates the upload.
- `state` (AppAssetLibraryAssetState) *(required)*: The current state of the resource in App Store Connect.
- `stateDetails` ([StateDetail]): Additional details about the current state, such as validation errors.

## Relationships

### Inherited By
- [AppAssetLibraryImageAcceptedAttributes](appassetlibraryimageacceptedattributes.md)
- [AppAssetLibraryImageApprovedAttributes](appassetlibraryimageapprovedattributes.md)
- [AppAssetLibraryImageArchivedAttributes](appassetlibraryimagearchivedattributes.md)
- [AppAssetLibraryImageAwaitingUploadAttributes](appassetlibraryimageawaitinguploadattributes.md)
- [AppAssetLibraryImageFailedAttributes](appassetlibraryimagefailedattributes.md)
- [AppAssetLibraryImageInReviewAttributes](appassetlibraryimageinreviewattributes.md)
- [AppAssetLibraryImageReadyForReviewAttributes](appassetlibraryimagereadyforreviewattributes.md)
- [AppAssetLibraryImageRejectedAttributes](appassetlibraryimagerejectedattributes.md)
- [AppAssetLibraryImageUploadCompleteAttributes](appassetlibraryimageuploadcompleteattributes.md)
- [AppAssetLibraryImageWaitingForReviewAttributes](appassetlibraryimagewaitingforreviewattributes.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appassetlibraryimagecommonattributes)*