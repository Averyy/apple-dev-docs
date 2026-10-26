# Types of Asset

**Framework**: Assets Library  
**Role**: API Collection

Constants to identify types of asset.

## Topics

### Constants
- [ALAssetsGroupLibrary](./alassetsgrouplibrary.md)
  The Library group that includes all assets that are synced from iTunes.
- [ALAssetsGroupAlbum](./alassetsgroupalbum.md)
  All the albums created on the device or synced from iTunes, not including Photo Stream or Shared Streams
- [ALAssetsGroupEvent](./alassetsgroupevent.md)
  All events, including those created during Camera Connection Kit import.
- [ALAssetsGroupFaces](./alassetsgroupfaces.md)
  All the faces albums synced from iTunes.
- [ALAssetsGroupSavedPhotos](./alassetsgroupsavedphotos.md)
  All the photos in the Camera Roll.
- [ALAssetsGroupPhotoStream](./alassetsgroupphotostream.md)
  The PhotoStream album.
- [ALAssetsGroupAll](./alassetsgroupall.md)
  The same as ORing together all the group types except for [`ALAssetsGroupLibrary`](./alassetsgrouplibrary.md).

## See Also

### Constants
- [Notification Keys](./notification-keys.md)
  Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](./alassetslibrarychangednotification.md) notification.
- [Error Domain](./error-domain.md)
  Constant for the AssetsLibrary domain.
- [Error Codes](./error-codes.md)
  AssetsLibrary-related error codes
- [ALAssetsGroupType](./alassetsgrouptype.md)
  A bitfield to identify types of asset.
- [ALAssetOrientation](./alassetorientation.md)
  Constants to indicate the orientation of an asset.
- [ALAssetsLibraryGroupsEnumerationResultsBlock](./alassetslibrarygroupsenumerationresultsblock.md)
  Signature for the block executed when a match is found during enumeration using `ALAssetsLibrary/enumerateGroups(withTypes:using:failureBlock:)`.
- [ALAssetsLibraryAssetForURLResultBlock](./alassetslibraryassetforurlresultblock.md)
  Signature for the block executed if the user has granted access to the caller to access the data managed by the framework in `ALAssetsLibrary/asset(for:resultBlock:failureBlock:)`.
- [ALAssetsLibraryWriteImageCompletionBlock](./alassetslibrarywriteimagecompletionblock.md)
  Signature for the block executed when `ALAssetsLibrary/writeImage(toSavedPhotosAlbum:orientation:completionBlock:)` completes.
- [ALAssetsLibraryWriteVideoCompletionBlock](./alassetslibrarywritevideocompletionblock.md)
  Signature for the block executed when `ALAssetsLibrary/writeVideoAtPath(toSavedPhotosAlbum:completionBlock:)` completes.
- [ALAssetsLibraryAccessFailureBlock](./alassetslibraryaccessfailureblock.md)
  Signature for the block executed if the user does not grant access to the caller to access the data managed by the framework.
- [ALAssetsLibraryGroupResultBlock](./alassetslibrarygroupresultblock.md)
  Signature for the block executed if the user grants access to the caller to access the data managed by the framework..
- [ALAuthorizationStatus](./alauthorizationstatus.md)
  Constants to indicate authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/types-of-asset)*