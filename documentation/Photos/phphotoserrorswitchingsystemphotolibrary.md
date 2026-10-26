# PHPhotosErrorSwitchingSystemPhotoLibrary

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

The photo library is unavailable because the user switched the system photo library.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.switchingSystemPhotoLibrary)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.switchingSystemPhotoLibrary)
- Mac Catalyst 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.switchingSystemPhotoLibrary)
- macOS 10.15+ - Deprecated in 11.0 (renamed: PHPhotosError.switchingSystemPhotoLibrary)
- tvOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.switchingSystemPhotoLibrary)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: PHPhotosError.switchingSystemPhotoLibrary)

> **Deprecated**: Use [`PHPhotosError.Code.switchingSystemPhotoLibrary`](./phphotoserror-swift.struct/code/switchingsystemphotolibrary.md) instead.

## Declaration

```swift
var PHPhotosErrorSwitchingSystemPhotoLibrary: Int { get }
```

## See Also

### Error Codes
- [static var invalid: PHPhotosError.Code](./phphotoserror-swift.struct/invalid.md)
  The requested operation is invalid.
- [var PHPhotosErrorInvalid: Int](./phphotoserrorinvalid.md)
  The requested operation is invalid.
- [var PHPhotosErrorLibraryVolumeOffline: Int](./phphotoserrorlibraryvolumeoffline.md)
  The photo library is unavailable because the file system volume that stores it isn’t mounted.
- [var PHPhotosErrorRelinquishingLibraryBundleToWriter: Int](./phphotoserrorrelinquishinglibrarybundletowriter.md)
  The photo library is unavailable because the user moved, renamed, or deleted the system photo library.
- [var PHPhotosErrorUserCancelled: Int](./phphotoserrorusercancelled.md)
  The user canceled the asset retrieval or editing request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotoserrorswitchingsystemphotolibrary)*