# Error Constants

**Framework**: PhotoKit  
**Role**: API Collection

Error code constants for framework operations.

## Topics

### Constants
- [static var accessRestricted: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/accessrestricted.md)
  An error that indicates the system configuration restricts access to the asset.
- [static var accessUserDenied: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/accessuserdenied.md)
  An error that indicates the user denied access.
- [static var changeNotSupported: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/changenotsupported.md)
  An error that indicates the system doesn’t support the change request configuration.
- [static var identifierNotFound: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/identifiernotfound.md)
  An error that indicates an identifier doesn’t exist.
- [static var internalError: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/internalerror.md)
  An error that indicates an internal error occurs.
- [static var invalidResource: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/invalidresource.md)
  An error that indicates the asset resource validation failed.
- [static var libraryVolumeOffline: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/libraryvolumeoffline.md)
  An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [static var libraryInFileProviderSyncRoot: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/libraryinfileprovidersyncroot.md)
  An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [static var limitExceeded: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/limitexceeded.md)
  An error that indicates the request exceeds a limit.
- [static var missingResource: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/missingresource.md)
  An error that indicates a missing asset resource.
- [static var multipleIdentifiersFound: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/multipleidentifiersfound.md)
  An error that indicates that more than one identifier exists.
- [static var networkAccessRequired: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/networkaccessrequired.md)
  An error that indicates the request for an asset resource failed because it requires network access.
- [static var networkError: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/networkerror.md)
  An error that indicates the request for an asset resource fails because of a network connection error.
- [static var notEnoughSpace: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/notenoughspace.md)
  An error that indicates insufficient space to perform the change.
- [static var operationInterrupted: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/operationinterrupted.md)
  An error that indicates an interruption occurs and the operation can’t complete.
- [static var persistentChangeDetailsUnavailable: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/persistentchangedetailsunavailable.md)
  An error that indicates the change details aren’t available for the persistent change.
- [static var persistentChangeTokenExpired: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/persistentchangetokenexpired.md)
  An error that indicates the library state is older than the available history of persistent changes.
- [static var relinquishingLibraryBundleToWriter: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/relinquishinglibrarybundletowriter.md)
  An error that indicates the photo library isn’t available because the user moves, renames, or deletes the system’s photo library.
- [static var requestNotSupportedForAsset: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/requestnotsupportedforasset.md)
  An error that indicates the system doesn’t support the request for the asset.
- [static var switchingSystemPhotoLibrary: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/switchingsystemphotolibrary.md)
  An error that indicates the photo library isn’t available because the user switched the system’s photo library.
- [static var userCancelled: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/usercancelled.md)
  An error that indicates the user cancels the asset retrieval or editing request.
- [static var invalid: PHPhotosError.Code](../Photos/phphotoserror-swift.struct/code/invalid.md)
  An error that indicates the operation isn’t valid.

## See Also

### Inspecting an Error
- [static var errorDomain: String](../Photos/phphotoserror-swift.struct/errordomain.md)
- [PHPhotosError.Code](../Photos/phphotoserror-swift.struct/code.md)
  Error codes for framework operations.
- [let PHLocalIdentifiersErrorKey: String](../Photos/phlocalidentifierserrorkey.md)
  An error key that retrieves an array of string values representing local identifiers matched to a cloud identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/error-constants)*