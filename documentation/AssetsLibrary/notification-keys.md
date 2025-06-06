# Notification Keys

**Framework**: Assets Library

Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification.

#### Overview

Assets that are modified use the [`ALAssetLibraryUpdatedAssetsKey`](alassetlibraryupdatedassetskey.md) key. Assets that are inserted or deleted use the [`ALAssetLibraryUpdatedAssetGroupsKey`](alassetlibraryupdatedassetgroupskey.md) key for the asset group that contains the asset.

Assets and asset groups that have no strong references are omitted from the notification’s user information dictionary.

## Topics

### Constants
- [let ALAssetLibraryUpdatedAssetsKey: String](alassetlibraryupdatedassetskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the assets that were updated.
- [let ALAssetLibraryInsertedAssetGroupsKey: String](alassetlibraryinsertedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the assets that were inserted.
- [let ALAssetLibraryUpdatedAssetGroupsKey: String](alassetlibraryupdatedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the asset groups that were updated.
- [let ALAssetLibraryDeletedAssetGroupsKey: String](alassetlibrarydeletedassetgroupskey.md)
  Value is a set of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects identifying the asset groups that were deleted.

## See Also

- [typealias ALAssetsGroupType](alassetsgrouptype.md)
  A bitfield to identify types of asset.
- [Types of Asset](types-of-asset.md)
  Constants to identify types of asset.
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
- [Error Domain](error-domain.md)
  Constant for the AssetsLibrary domain.
- [Error Codes](error-codes.md)
  AssetsLibrary-related error codes


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/notification-keys)*