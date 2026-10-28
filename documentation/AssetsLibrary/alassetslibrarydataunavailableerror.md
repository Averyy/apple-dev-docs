# ALAssetsLibraryDataUnavailableError

**Framework**: Assets Library  
**Kind**: var  
**Role**: Global Variable

The data was not available.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var ALAssetsLibraryDataUnavailableError: Int { get }
```

```c
ALAssetsLibraryDataUnavailableError
```

## Discussion

This error may be returned in the [`ALAssetsLibraryAccessFailureBlock`](./alassetslibraryaccessfailureblock.md) for `ALAssetsLibrary/enumerateGroups(withTypes:using:failureBlock:)` and `ALAssetsLibrary/asset(for:resultBlock:failureBlock:)`; and in the completion blocks for `ALAssetsLibrary/writeImage(toSavedPhotosAlbum:orientation:completionBlock:)` and `ALAssetsLibrary/writeImage(toSavedPhotosAlbum:orientation:completionBlock:)`; as well as in the completion selector for [`UIImageWriteToSavedPhotosAlbum(_:_:_:_:)`](../UIKit/uiimagewritetosavedphotosalbum%28_,_,_,_%29.md) and [`UISaveVideoAtPathToSavedPhotosAlbum(_:_:_:_:)`](../UIKit/uisavevideoatpathtosavedphotosalbum%28_,_,_,_%29.md).

## See Also

### Constants
- [var ALAssetsLibraryUnknownError: Int](./alassetslibraryunknownerror.md)
  The reason for the error is unknown.
- [var ALAssetsLibraryWriteFailedError: Int](./alassetslibrarywritefailederror.md)
  The attempt to write data failed.
- [var ALAssetsLibraryWriteBusyError: Int](./alassetslibrarywritebusyerror.md)
  Writing was already busy when the attempt to write was made.
- [var ALAssetsLibraryWriteInvalidDataError: Int](./alassetslibrarywriteinvaliddataerror.md)
  The data was invalid.
- [var ALAssetsLibraryWriteIncompatibleDataError: Int](./alassetslibrarywriteincompatibledataerror.md)
  The data contained incompatible data.
- [var ALAssetsLibraryWriteDataEncodingError: Int](./alassetslibrarywritedataencodingerror.md)
  The data contained data with the wrong encoding.
- [var ALAssetsLibraryWriteDiskSpaceError: Int](./alassetslibrarywritediskspaceerror.md)
  There was not enough space on the disk to write the data.
- [var ALAssetsLibraryAccessUserDeniedError: Int](./alassetslibraryaccessuserdeniederror.md)
  The user denied access to the library.
- [var ALAssetsLibraryAccessGloballyDeniedError: Int](./alassetslibraryaccessgloballydeniederror.md)
  Access to the library was denied globally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrarydataunavailableerror)*