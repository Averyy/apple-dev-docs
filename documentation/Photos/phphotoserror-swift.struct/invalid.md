# invalid

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

The requested operation is invalid.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0 (renamed: PHPhotosError.internalError)
- iPadOS 13.0+ - Deprecated in 15.0 (renamed: PHPhotosError.internalError)
- Mac Catalyst 13.0+ - Deprecated in 15.0 (renamed: PHPhotosError.internalError)
- macOS 10.15+ - Deprecated in 12.0 (renamed: PHPhotosError.internalError)
- tvOS 13.0+ - Deprecated in 15.0 (renamed: PHPhotosError.internalError)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: PHPhotosError.internalError)

> **Deprecated**: Use [`internalError`](./internalerror.md) instead.

## Declaration

```swift
static var invalid: PHPhotosError.Code { get }
```

## See Also

### Error Codes
- [var PHPhotosErrorInvalid: Int](../phphotoserrorinvalid.md)
  The requested operation is invalid.
- [var PHPhotosErrorLibraryVolumeOffline: Int](../phphotoserrorlibraryvolumeoffline.md)
  The photo library is unavailable because the file system volume that stores it isn’t mounted.
- [var PHPhotosErrorRelinquishingLibraryBundleToWriter: Int](../phphotoserrorrelinquishinglibrarybundletowriter.md)
  The photo library is unavailable because the user moved, renamed, or deleted the system photo library.
- [var PHPhotosErrorSwitchingSystemPhotoLibrary: Int](../phphotoserrorswitchingsystemphotolibrary.md)
  The photo library is unavailable because the user switched the system photo library.
- [var PHPhotosErrorUserCancelled: Int](../phphotoserrorusercancelled.md)
  The user canceled the asset retrieval or editing request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/invalid)*