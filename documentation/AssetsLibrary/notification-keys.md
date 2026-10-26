# Notification Keys

**Framework**: Assets Library  
**Role**: API Collection

Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](./alassetslibrarychangednotification.md) notification.

#### Overview

Assets that are modified use the [`ALAssetLibraryUpdatedAssetsKey`](./alassetlibraryupdatedassetskey.md) key. Assets that are inserted or deleted use the [`ALAssetLibraryUpdatedAssetGroupsKey`](./alassetlibraryupdatedassetgroupskey.md) key for the asset group that contains the asset.

Assets and asset groups that have no strong references are omitted from the notification’s user information dictionary.

## Topics

### Constants
- [ALAssetLibraryUpdatedAssetsKey](./alassetlibraryupdatedassetskey.md)
  Value is a set of [`NSURL`](../Foundation/nsurl.md) objects identifying the assets that were updated.
- [ALAssetLibraryInsertedAssetGroupsKey](./alassetlibraryinsertedassetgroupskey.md)
  Value is a set of [`NSURL`](../Foundation/nsurl.md) objects identifying the assets that were inserted.
- [ALAssetLibraryUpdatedAssetGroupsKey](./alassetlibraryupdatedassetgroupskey.md)
  Value is a set of [`NSURL`](../Foundation/nsurl.md) objects identifying the asset groups that were updated.
- [ALAssetLibraryDeletedAssetGroupsKey](./alassetlibrarydeletedassetgroupskey.md)
  Value is a set of [`NSURL`](../Foundation/nsurl.md) objects identifying the asset groups that were deleted.

## See Also

### Constants
- [Types of Asset](./types-of-asset.md)
  Constants to identify types of asset.
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

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/notification-keys)*