# Error Codes

**Framework**: Assets Library

AssetsLibrary-related error codes

## Topics

### Constants
- [var ALAssetsLibraryUnknownError: Int](alassetslibraryunknownerror.md)
  The reason for the error is unknown.
- [var ALAssetsLibraryWriteFailedError: Int](alassetslibrarywritefailederror.md)
  The attempt to write data failed.
- [var ALAssetsLibraryWriteBusyError: Int](alassetslibrarywritebusyerror.md)
  Writing was already busy when the attempt to write was made.
- [var ALAssetsLibraryWriteInvalidDataError: Int](alassetslibrarywriteinvaliddataerror.md)
  The data was invalid.
- [var ALAssetsLibraryWriteIncompatibleDataError: Int](alassetslibrarywriteincompatibledataerror.md)
  The data contained incompatible data.
- [var ALAssetsLibraryWriteDataEncodingError: Int](alassetslibrarywritedataencodingerror.md)
  The data contained data with the wrong encoding.
- [var ALAssetsLibraryWriteDiskSpaceError: Int](alassetslibrarywritediskspaceerror.md)
  There was not enough space on the disk to write the data.
- [var ALAssetsLibraryDataUnavailableError: Int](alassetslibrarydataunavailableerror.md)
  The data was not available.
- [var ALAssetsLibraryAccessUserDeniedError: Int](alassetslibraryaccessuserdeniederror.md)
  The user denied access to the library.
- [var ALAssetsLibraryAccessGloballyDeniedError: Int](alassetslibraryaccessgloballydeniederror.md)
  Access to the library was denied globally.

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
- [Notification Keys](notification-keys.md)
  Keys used to get values from the user information dictionary of the [`ALAssetsLibraryChangedNotification`](alassetslibrarychangednotification.md) notification.
- [Error Domain](error-domain.md)
  Constant for the AssetsLibrary domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/error-codes)*