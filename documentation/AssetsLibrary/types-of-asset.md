# Types of Asset

**Framework**: Assets Library

Constants to identify types of asset.

## Topics

### Constants
- [var ALAssetsGroupLibrary: UInt32](alassetsgrouplibrary.md)
  The Library group that includes all assets that are synced from iTunes.
- [var ALAssetsGroupAlbum: UInt32](alassetsgroupalbum.md)
  All the albums created on the device or synced from iTunes, not including Photo Stream or Shared Streams
- [var ALAssetsGroupEvent: UInt32](alassetsgroupevent.md)
  All events, including those created during Camera Connection Kit import.
- [var ALAssetsGroupFaces: UInt32](alassetsgroupfaces.md)
  All the faces albums synced from iTunes.
- [var ALAssetsGroupSavedPhotos: UInt32](alassetsgroupsavedphotos.md)
  All the photos in the Camera Roll.
- [var ALAssetsGroupPhotoStream: UInt32](alassetsgroupphotostream.md)
  The PhotoStream album.
- [var ALAssetsGroupAll: UInt32](alassetsgroupall.md)
  The same as ORing together all the group types except for [`ALAssetsGroupLibrary`](alassetsgrouplibrary.md).

## See Also

- [typealias ALAssetsGroupType](alassetsgrouptype.md)
  A bitfield to identify types of asset.
- [enum ALAssetOrientation](alassetorientation.md)
  Constants to indicate the orientation of an asset.
- [typealias ALAssetsLibraryGroupsEnumerationResultsBlock](alassetslibrarygroupsenumerationresultsblock.md)
  Signature for the block executed when a match is found during enumeration using [`enumerateGroups(withTypes:using:failureBlock:)`](alassetslibrary/enumerategroups(withtypes:using:failureblock:).md).
- [typealias ALAssetsLibraryAssetForURLResultBlock](alassetslibraryassetforurlresultblock.md)
  Signature for the block executed if the user has granted access to the caller to access the data managed by the framework in [`asset(for:resultBlock:failureBlock:)`](alassetslibrary/asset(for:resultblock:failureblock:).md).
- [typealias ALAssetsLibraryWriteImageCompletionBlock](alassetslibrarywriteimagecompletionblock.md)
  Signature for the block executed when [`writeImage(toSavedPhotosAlbum:orientation:completionBlock:)`](alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:).md) completes.
- [typealias ALAssetsLibraryWriteVideoCompletionBlock](alassetslibrarywritevideocompletionblock.md)
  Signature for the block executed when [`writeVideoAtPath(toSavedPhotosAlbum:completionBlock:)`](alassetslibrary/writevideoatpath(tosavedphotosalbum:completionblock:).md) completes.
- [typealias ALAssetsLibraryAccessFailureBlock](alassetslibraryaccessfailureblock.md)
  Signature for the block executed if the user does not grant access to the caller to access the data managed by the framework.
- [typealias ALAssetsLibraryGroupResultBlock](alassetslibrarygroupresultblock.md)
  Signature for the block executed if the user grants access to the caller to access the data managed by the framework..
- [enum ALAuthorizationStatus](alauthorizationstatus.md)
  Constants to indicate authorization status.
- [Notification Keys](notification-keys.md)
  Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification.
- [Error Domain](error-domain.md)
  Constant for the AssetsLibrary domain.
- [Error Codes](error-codes.md)
  AssetsLibrary-related error codes


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/types-of-asset)*