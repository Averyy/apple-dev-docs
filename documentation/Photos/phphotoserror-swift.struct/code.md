# PHPhotosError.Code

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Error codes for framework operations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum PHPhotosError : NSInteger;
```

## Topics

### Error Codes
- [PHPhotosError.Code.accessRestricted](./code/accessrestricted.md)
  An error that indicates the system configuration restricts access to the asset.
- [PHPhotosError.Code.accessUserDenied](./code/accessuserdenied.md)
  An error that indicates the user denies access.
- [PHPhotosError.Code.changeNotSupported](./code/changenotsupported.md)
  An error that indicates the system doesn’t support the change request configuration.
- [PHPhotosError.Code.identifierNotFound](./code/identifiernotfound.md)
  An error that indicates an identifier doesn’t exist.
- [PHPhotosError.Code.internalError](./code/internalerror.md)
  An error that indicates an internal error occurs.
- [static var invalid: PHPhotosError.Code](./code/invalid.md)
  An error that indicates the operation isn’t valid.
- [PHPhotosError.Code.invalidResource](./code/invalidresource.md)
  An error that indicates the asset resource validation fails.
- [PHPhotosError.Code.libraryVolumeOffline](./code/libraryvolumeoffline.md)
  An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [PHPhotosError.Code.libraryInFileProviderSyncRoot](./code/libraryinfileprovidersyncroot.md)
  An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [PHPhotosError.Code.limitExceeded](./code/limitexceeded.md)
  An error that indicates the request exceeds a limit.
- [PHPhotosError.Code.missingResource](./code/missingresource.md)
  An error that indicates a missing asset resource.
- [PHPhotosError.Code.multipleIdentifiersFound](./code/multipleidentifiersfound.md)
  An error that indicates that more than one identifier exists.
- [PHPhotosError.Code.networkAccessRequired](./code/networkaccessrequired.md)
  An error that indicates the request for an asset resource fails because it requires network access.
- [PHPhotosError.Code.networkError](./code/networkerror.md)
  An error that indicates the request for an asset resource fails because of a network connection error.
- [PHPhotosError.Code.notEnoughSpace](./code/notenoughspace.md)
  An error that indicates there’s not enough space to perform the requested change.
- [PHPhotosError.Code.operationInterrupted](./code/operationinterrupted.md)
  An error that indicates an interruption occurs and the operation can’t complete.
- [PHPhotosError.Code.persistentChangeDetailsUnavailable](./code/persistentchangedetailsunavailable.md)
  An error that indicates the change details aren’t available for the persistent change.
- [PHPhotosError.Code.persistentChangeTokenExpired](./code/persistentchangetokenexpired.md)
  An error that indicates the library state is older than the available history of persistent changes.
- [PHPhotosError.Code.relinquishingLibraryBundleToWriter](./code/relinquishinglibrarybundletowriter.md)
  An error that indicates the photo library isn’t available because the user moves, renames, or deletes the system’s photo library.
- [PHPhotosError.Code.requestNotSupportedForAsset](./code/requestnotsupportedforasset.md)
  An error that indicates the system doesn’t support the request for the specified asset.
- [PHPhotosError.Code.switchingSystemPhotoLibrary](./code/switchingsystemphotolibrary.md)
  An error that indicates the photo library isn’t available because the user switches the system’s photo library.
- [PHPhotosError.Code.userCancelled](./code/usercancelled.md)
  An error that indicates the user cancels the asset retrieval or editing request.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting an Error
- [static var errorDomain: String](./errordomain.md)
- [Error Constants](../../PhotoKit/error-constants.md)
  Error code constants for framework operations.
- [let PHLocalIdentifiersErrorKey: String](../phlocalidentifierserrorkey.md)
  An error key that retrieves an array of string values representing local identifiers matched to a cloud identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/code)*