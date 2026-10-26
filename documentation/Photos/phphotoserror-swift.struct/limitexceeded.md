# limitExceeded

**Framework**: Photos  
**Kind**: property  
**Role**: Type Property

An error that indicates the request exceeds a limit.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- tvOS 26.1+
- visionOS 26.0+

## Declaration

```swift
static var limitExceeded: PHPhotosError.Code { get }
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## See Also

### Constants
- [static var accessRestricted: PHPhotosError.Code](./accessrestricted.md)
  An error that indicates the system configuration restricts access to the asset.
- [static var accessUserDenied: PHPhotosError.Code](./accessuserdenied.md)
  An error that indicates the user denied access.
- [static var changeNotSupported: PHPhotosError.Code](./changenotsupported.md)
  An error that indicates the system doesn’t support the change request configuration.
- [static var identifierNotFound: PHPhotosError.Code](./identifiernotfound.md)
  An error that indicates an identifier doesn’t exist.
- [static var internalError: PHPhotosError.Code](./internalerror.md)
  An error that indicates an internal error occurs.
- [static var invalidResource: PHPhotosError.Code](./invalidresource.md)
  An error that indicates the asset resource validation failed.
- [static var libraryVolumeOffline: PHPhotosError.Code](./libraryvolumeoffline.md)
  An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [static var libraryInFileProviderSyncRoot: PHPhotosError.Code](./libraryinfileprovidersyncroot.md)
  An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [static var missingResource: PHPhotosError.Code](./missingresource.md)
  An error that indicates a missing asset resource.
- [static var multipleIdentifiersFound: PHPhotosError.Code](./multipleidentifiersfound.md)
  An error that indicates that more than one identifier exists.
- [static var networkAccessRequired: PHPhotosError.Code](./networkaccessrequired.md)
  An error that indicates the request for an asset resource failed because it requires network access.
- [static var networkError: PHPhotosError.Code](./networkerror.md)
  An error that indicates the request for an asset resource fails because of a network connection error.
- [static var notEnoughSpace: PHPhotosError.Code](./notenoughspace.md)
  An error that indicates insufficient space to perform the change.
- [static var operationInterrupted: PHPhotosError.Code](./operationinterrupted.md)
  An error that indicates an interruption occurs and the operation can’t complete.
- [static var persistentChangeDetailsUnavailable: PHPhotosError.Code](./persistentchangedetailsunavailable.md)
  An error that indicates the change details aren’t available for the persistent change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/limitexceeded)*