# AssetsLibrary Data Types

**Framework**: Assets Library  
**Role**: API Collection

## Topics

### Data Types
- [ALAssetsGroupEnumerationResultsBlock](./alassetsgroupenumerationresultsblock.md)
  Signature for the block executed during enumeration of assets.
- [ALAssetsGroupType](./alassetsgrouptype.md)
  A bitfield to identify types of asset.
- [ALAssetsLibraryAccessFailureBlock](./alassetslibraryaccessfailureblock.md)
  Signature for the block executed if the user does not grant access to the caller to access the data managed by the framework.
- [ALAssetsLibraryAssetForURLResultBlock](./alassetslibraryassetforurlresultblock.md)
  Signature for the block executed if the user has granted access to the caller to access the data managed by the framework in `ALAssetsLibrary/asset(for:resultBlock:failureBlock:)`.
- [ALAssetsLibraryGroupResultBlock](./alassetslibrarygroupresultblock.md)
  Signature for the block executed if the user grants access to the caller to access the data managed by the framework..
- [ALAssetsLibraryGroupsEnumerationResultsBlock](./alassetslibrarygroupsenumerationresultsblock.md)
  Signature for the block executed when a match is found during enumeration using `ALAssetsLibrary/enumerateGroups(withTypes:using:failureBlock:)`.
- [ALAssetsLibraryWriteImageCompletionBlock](./alassetslibrarywriteimagecompletionblock.md)
  Signature for the block executed when `ALAssetsLibrary/writeImage(toSavedPhotosAlbum:orientation:completionBlock:)` completes.
- [ALAssetsLibraryWriteVideoCompletionBlock](./alassetslibrarywritevideocompletionblock.md)
  Signature for the block executed when `ALAssetsLibrary/writeVideoAtPath(toSavedPhotosAlbum:completionBlock:)` completes.

## See Also

### Reference
- [AssetsLibrary Enumerations](./assetslibrary-enumerations.md)
- [AssetsLibrary Constants](./assetslibrary-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/assetslibrary-data-types)*