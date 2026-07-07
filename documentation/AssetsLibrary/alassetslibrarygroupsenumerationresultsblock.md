# ALAssetsLibraryGroupsEnumerationResultsBlock

**Framework**: Assets Library  
**Kind**: typealias

Signature for the block executed when a match is found during enumeration using `ALAssetsLibrary/enumerateGroups(withTypes:using:failureBlock:)`.

## Declaration

```swift
typedef void (^)(ALAssetsGroup *, _Bool *) ALAssetsLibraryGroupsEnumerationResultsBlock;
```

#### Discussion

The block parameters are defined as follows:

- **group**: The current asset group in the enumeration.
- **stop**: A pointer to a boolean value; set the value to [`true`](https://developer.apple.com/documentation/Swift/true) to stop enumeration.

## See Also

- [ALAssetsGroupType](alassetsgrouptype.md)
  A bitfield to identify types of asset.
- [Types of Asset](types-of-asset.md)
  Constants to identify types of asset.
- [ALAssetOrientation](alassetorientation.md)
  Constants to indicate the orientation of an asset.
- [ALAssetsLibraryAssetForURLResultBlock](alassetslibraryassetforurlresultblock.md)
  Signature for the block executed if the user has granted access to the caller to access the data managed by the framework in `ALAssetsLibrary/asset(for:resultBlock:failureBlock:)`.
- [ALAssetsLibraryWriteImageCompletionBlock](alassetslibrarywriteimagecompletionblock.md)
  Signature for the block executed when `ALAssetsLibrary/writeImage(toSavedPhotosAlbum:orientation:completionBlock:)` completes.
- [ALAssetsLibraryWriteVideoCompletionBlock](alassetslibrarywritevideocompletionblock.md)
  Signature for the block executed when `ALAssetsLibrary/writeVideoAtPath(toSavedPhotosAlbum:completionBlock:)` completes.
- [ALAssetsLibraryAccessFailureBlock](alassetslibraryaccessfailureblock.md)
  Signature for the block executed if the user does not grant access to the caller to access the data managed by the framework.
- [ALAssetsLibraryGroupResultBlock](alassetslibrarygroupresultblock.md)
  Signature for the block executed if the user grants access to the caller to access the data managed by the framework..
- [ALAuthorizationStatus](alauthorizationstatus.md)
  Constants to indicate authorization status.
- [Notification Keys](notification-keys.md)
  Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification.
- [Error Domain](error-domain.md)
  Constant for the AssetsLibrary domain.
- [Error Codes](error-codes.md)
  AssetsLibrary-related error codes


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrarygroupsenumerationresultsblock)*