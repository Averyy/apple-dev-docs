# PHPhotosErrorLibraryVolumeOffline

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

The photo library is unavailable because the file system volume that stores it isn’t mounted.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.libraryVolumeOffline)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.libraryVolumeOffline)
- Mac Catalyst 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.libraryVolumeOffline)
- macOS 10.15+ - Deprecated in 11.0 (renamed: PHPhotosError.libraryVolumeOffline)
- tvOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.libraryVolumeOffline)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: PHPhotosError.libraryVolumeOffline)

> **Deprecated**: Use [`PHPhotosError.Code.libraryVolumeOffline`](./phphotoserror-swift.struct/code/libraryvolumeoffline.md) instead.

## Declaration

```swift
var PHPhotosErrorLibraryVolumeOffline: Int { get }
```

## See Also

### Error Codes
- [static var invalid: PHPhotosError.Code](./phphotoserror-swift.struct/invalid.md)
  The requested operation is invalid.
- [var PHPhotosErrorInvalid: Int](./phphotoserrorinvalid.md)
  The requested operation is invalid.
- [var PHPhotosErrorRelinquishingLibraryBundleToWriter: Int](./phphotoserrorrelinquishinglibrarybundletowriter.md)
  The photo library is unavailable because the user moved, renamed, or deleted the system photo library.
- [var PHPhotosErrorSwitchingSystemPhotoLibrary: Int](./phphotoserrorswitchingsystemphotolibrary.md)
  The photo library is unavailable because the user switched the system photo library.
- [var PHPhotosErrorUserCancelled: Int](./phphotoserrorusercancelled.md)
  The user canceled the asset retrieval or editing request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotoserrorlibraryvolumeoffline)*