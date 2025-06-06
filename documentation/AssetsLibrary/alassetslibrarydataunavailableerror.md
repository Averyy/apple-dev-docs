# ALAssetsLibraryDataUnavailableError

**Framework**: Assets Library  
**Kind**: var

The data was not available.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var ALAssetsLibraryDataUnavailableError: Int { get }
```

#### Discussion

This error may be returned in the [`ALAssetsLibraryAccessFailureBlock`](alassetslibraryaccessfailureblock.md) for [`enumerateGroups(withTypes:using:failureBlock:)`](alassetslibrary/enumerategroups(withtypes:using:failureblock:).md) and [`asset(for:resultBlock:failureBlock:)`](alassetslibrary/asset(for:resultblock:failureblock:).md); and in the completion blocks for [`writeImage(toSavedPhotosAlbum:orientation:completionBlock:)`](alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:).md) and [`writeImage(toSavedPhotosAlbum:orientation:completionBlock:)`](alassetslibrary/writeimage(tosavedphotosalbum:orientation:completionblock:).md); as well as in the completion selector for [`UIImageWriteToSavedPhotosAlbum(_:_:_:_:)`](https://developer.apple.com/documentation/UIKit/UIImageWriteToSavedPhotosAlbum(_:_:_:_:)) and [`UISaveVideoAtPathToSavedPhotosAlbum(_:_:_:_:)`](https://developer.apple.com/documentation/UIKit/UISaveVideoAtPathToSavedPhotosAlbum(_:_:_:_:)).

## See Also

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
- [var ALAssetsLibraryAccessUserDeniedError: Int](alassetslibraryaccessuserdeniederror.md)
  The user denied access to the library.
- [var ALAssetsLibraryAccessGloballyDeniedError: Int](alassetslibraryaccessgloballydeniederror.md)
  Access to the library was denied globally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrarydataunavailableerror)*