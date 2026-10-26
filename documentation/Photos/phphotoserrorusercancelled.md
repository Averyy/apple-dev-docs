# PHPhotosErrorUserCancelled

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

The user canceled the asset retrieval or editing request.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.userCancelled)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.userCancelled)
- Mac Catalyst 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.userCancelled)
- macOS 10.15+ - Deprecated in 11.0 (renamed: PHPhotosError.userCancelled)
- tvOS 13.0+ - Deprecated in 14.0 (renamed: PHPhotosError.userCancelled)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: PHPhotosError.userCancelled)

> **Deprecated**: Use [`PHPhotosError.Code.userCancelled`](./phphotoserror-swift.struct/code/usercancelled.md) instead.

## Declaration

```swift
var PHPhotosErrorUserCancelled: Int { get }
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
- [var PHPhotosErrorSwitchingSystemPhotoLibrary: Int](./phphotoserrorswitchingsystemphotolibrary.md)
  The photo library is unavailable because the user switched the system photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotoserrorusercancelled)*