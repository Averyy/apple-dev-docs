# ALAssetsLibraryGroupResultBlock

**Framework**: Assets Library  
**Kind**: typealias

Signature for the block executed if the user grants access to the caller to access the data managed by the framework..

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
typealias ALAssetsLibraryGroupResultBlock = (ALAssetsGroup?) -> Void
```

#### Discussion

The block parameter is defined as follows:

If the group is not found or not created (for example, because of a name collision), `group` is `nil`.

This block type is used by [`addAssetsGroupAlbum(withName:resultBlock:failureBlock:)`](alassetslibrary/addassetsgroupalbum(withname:resultblock:failureblock:).md) and [`group(for:resultBlock:failureBlock:)`](alassetslibrary/group(for:resultblock:failureblock:).md).

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
- [enum ALAuthorizationStatus](alauthorizationstatus.md)
  Constants to indicate authorization status.
- [Notification Keys](notification-keys.md)
  Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification.
- [Error Domain](error-domain.md)
  Constant for the AssetsLibrary domain.
- [Error Codes](error-codes.md)
  AssetsLibrary-related error codes


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrarygroupresultblock)*