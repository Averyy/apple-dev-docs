# Error Constants

**Framework**: PhotoKit  
**Role**: API Collection

Error code constants for framework operations.

## Topics

### Constants
- [static var accessRestricted: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/accessrestricted)
  An error that indicates the system configuration restricts access to the asset.
- [static var accessUserDenied: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/accessuserdenied)
  An error that indicates the user denied access.
- [static var changeNotSupported: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/changenotsupported)
  An error that indicates the system doesn’t support the change request configuration.
- [static var identifierNotFound: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/identifiernotfound)
  An error that indicates an identifier doesn’t exist.
- [static var internalError: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/internalerror)
  An error that indicates an internal error occurs.
- [static var invalidResource: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/invalidresource)
  An error that indicates the asset resource validation failed.
- [static var libraryVolumeOffline: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/libraryvolumeoffline)
  An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [static var libraryInFileProviderSyncRoot: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/libraryinfileprovidersyncroot)
  An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [static var limitExceeded: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/limitexceeded)
  An error that indicates the request exceeds a limit.
- [static var missingResource: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/missingresource)
  An error that indicates a missing asset resource.
- [static var multipleIdentifiersFound: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/multipleidentifiersfound)
  An error that indicates that more than one identifier exists.
- [static var networkAccessRequired: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/networkaccessrequired)
  An error that indicates the request for an asset resource failed because it requires network access.
- [static var networkError: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/networkerror)
  An error that indicates the request for an asset resource fails because of a network connection error.
- [static var notEnoughSpace: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/notenoughspace)
  An error that indicates insufficient space to perform the change.
- [static var operationInterrupted: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/operationinterrupted)
  An error that indicates an interruption occurs and the operation can’t complete.
- [static var persistentChangeDetailsUnavailable: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/persistentchangedetailsunavailable)
  An error that indicates the change details aren’t available for the persistent change.
- [static var persistentChangeTokenExpired: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/persistentchangetokenexpired)
  An error that indicates the library state is older than the available history of persistent changes.
- [static var relinquishingLibraryBundleToWriter: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/relinquishinglibrarybundletowriter)
  An error that indicates the photo library isn’t available because the user moves, renames, or deletes the system’s photo library.
- [static var requestNotSupportedForAsset: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/requestnotsupportedforasset)
  An error that indicates the system doesn’t support the request for the asset.
- [static var switchingSystemPhotoLibrary: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/switchingsystemphotolibrary)
  An error that indicates the photo library isn’t available because the user switched the system’s photo library.
- [static var userCancelled: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/usercancelled)
  An error that indicates the user cancels the asset retrieval or editing request.
- [static var invalid: PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/code/invalid)
  An error that indicates the operation isn’t valid.

## See Also

### Inspecting an Error
- [static var errorDomain: String](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/errordomain)
- [PHPhotosError.Code](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/code)
  Error codes for framework operations.
- [let PHLocalIdentifiersErrorKey: String](https://developer.apple.com/documentation/photos/phlocalidentifierserrorkey)
  An error key that retrieves an array of string values representing local identifiers matched to a cloud identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/error-constants)*