# PHPhotosErrorInvalid

**Framework**: Photos  
**Kind**: case  
**Role**: Enumeration Case

An error that indicates the operation isn’t valid.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.0+ - Deprecated in 15.0
- macOS 10.15+ - Deprecated in 12.0
- tvOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`PHPhotosError.Code.internalError`](../phphotoserror-swift.struct/code/internalerror.md) instead.

## Declaration

```c
PHPhotosErrorInvalid
```

## See Also

### Error Codes
- [PHPhotosError.Code.accessRestricted](../phphotoserror-swift.struct/code/accessrestricted.md)
  An error that indicates the system configuration restricts access to the asset.
- [PHPhotosError.Code.accessUserDenied](../phphotoserror-swift.struct/code/accessuserdenied.md)
  An error that indicates the user denies access.
- [PHPhotosError.Code.changeNotSupported](../phphotoserror-swift.struct/code/changenotsupported.md)
  An error that indicates the system doesn’t support the change request configuration.
- [PHPhotosError.Code.identifierNotFound](../phphotoserror-swift.struct/code/identifiernotfound.md)
  An error that indicates an identifier doesn’t exist.
- [PHPhotosError.Code.internalError](../phphotoserror-swift.struct/code/internalerror.md)
  An error that indicates an internal error occurs.
- [PHPhotosError.Code.invalidResource](../phphotoserror-swift.struct/code/invalidresource.md)
  An error that indicates the asset resource validation fails.
- [PHPhotosError.Code.libraryVolumeOffline](../phphotoserror-swift.struct/code/libraryvolumeoffline.md)
  An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [PHPhotosError.Code.libraryInFileProviderSyncRoot](../phphotoserror-swift.struct/code/libraryinfileprovidersyncroot.md)
  An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [PHPhotosError.Code.limitExceeded](../phphotoserror-swift.struct/code/limitexceeded.md)
  An error that indicates the request exceeds a limit.
- [PHPhotosError.Code.missingResource](../phphotoserror-swift.struct/code/missingresource.md)
  An error that indicates a missing asset resource.
- [PHPhotosError.Code.multipleIdentifiersFound](../phphotoserror-swift.struct/code/multipleidentifiersfound.md)
  An error that indicates that more than one identifier exists.
- [PHPhotosError.Code.networkAccessRequired](../phphotoserror-swift.struct/code/networkaccessrequired.md)
  An error that indicates the request for an asset resource fails because it requires network access.
- [PHPhotosError.Code.networkError](../phphotoserror-swift.struct/code/networkerror.md)
  An error that indicates the request for an asset resource fails because of a network connection error.
- [PHPhotosError.Code.notEnoughSpace](../phphotoserror-swift.struct/code/notenoughspace.md)
  An error that indicates there’s not enough space to perform the requested change.
- [PHPhotosError.Code.operationInterrupted](../phphotoserror-swift.struct/code/operationinterrupted.md)
  An error that indicates an interruption occurs and the operation can’t complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotoserror-c.enum/phphotoserrorinvalid)*