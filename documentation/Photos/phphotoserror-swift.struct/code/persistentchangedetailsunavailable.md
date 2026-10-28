# PHPhotosError.Code.persistentChangeDetailsUnavailable

**Framework**: Photos  
**Kind**: case  
**Role**: Case

An error that indicates the change details aren’t available for the persistent change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case persistentChangeDetailsUnavailable
```

```c
PHPhotosErrorPersistentChangeDetailsUnavailable
```

## Discussion

If a change can’t provide change details, [`changeDetails(for:)`](../../phpersistentchange/changedetails%28for%29.md) returns `nil` and an error that indicates the reason. This error indicates you can’t rely on the change to completely reconstruct the state changes that occur, so you need to determine it by using the current library state.

## See Also

### Error Codes
- [PHPhotosError.Code.accessRestricted](./accessrestricted.md)
  An error that indicates the system configuration restricts access to the asset.
- [PHPhotosError.Code.accessUserDenied](./accessuserdenied.md)
  An error that indicates the user denies access.
- [PHPhotosError.Code.changeNotSupported](./changenotsupported.md)
  An error that indicates the system doesn’t support the change request configuration.
- [PHPhotosError.Code.identifierNotFound](./identifiernotfound.md)
  An error that indicates an identifier doesn’t exist.
- [PHPhotosError.Code.internalError](./internalerror.md)
  An error that indicates an internal error occurs.
- [static var invalid: PHPhotosError.Code](./invalid.md)
  An error that indicates the operation isn’t valid.
- [PHPhotosError.Code.invalidResource](./invalidresource.md)
  An error that indicates the asset resource validation fails.
- [PHPhotosError.Code.libraryVolumeOffline](./libraryvolumeoffline.md)
  An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [PHPhotosError.Code.libraryInFileProviderSyncRoot](./libraryinfileprovidersyncroot.md)
  An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [PHPhotosError.Code.limitExceeded](./limitexceeded.md)
  An error that indicates the request exceeds a limit.
- [PHPhotosError.Code.missingResource](./missingresource.md)
  An error that indicates a missing asset resource.
- [PHPhotosError.Code.multipleIdentifiersFound](./multipleidentifiersfound.md)
  An error that indicates that more than one identifier exists.
- [PHPhotosError.Code.networkAccessRequired](./networkaccessrequired.md)
  An error that indicates the request for an asset resource fails because it requires network access.
- [PHPhotosError.Code.networkError](./networkerror.md)
  An error that indicates the request for an asset resource fails because of a network connection error.
- [PHPhotosError.Code.notEnoughSpace](./notenoughspace.md)
  An error that indicates there’s not enough space to perform the requested change.
- [PHPhotosErrorOperationInterrupted](./operationinterrupted.md)
  An error that indicates an interruption occurs and the operation can’t complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/code/persistentchangedetailsunavailable)*