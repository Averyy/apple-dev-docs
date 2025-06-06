# NSFileProviderKnownFolderLocations

**Framework**: File Provider  
**Kind**: class

A class for working with known-folder locations.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class NSFileProviderKnownFolderLocations
```

## Topics

### Identifying known-folder locations
- [var desktopLocation: NSFileProviderKnownFolderLocations.Location?](nsfileproviderknownfolderlocations/desktoplocation.md)
- [var documentsLocation: NSFileProviderKnownFolderLocations.Location?](nsfileproviderknownfolderlocations/documentslocation.md)
- [NSFileProviderKnownFolderLocations.Location](nsfileproviderknownfolderlocations/location.md)
### Configuring folder options
- [var shouldCreateBinaryCompatibilitySymlink: Bool](nsfileproviderknownfolderlocations/shouldcreatebinarycompatibilitysymlink.md)
### Creating a known-folder locations object
- [init()](nsfileproviderknownfolderlocations/init.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func claimKnownFolders(NSFileProviderKnownFolderLocations, localizedReason: String, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/claimknownfolders(_:localizedreason:completionhandler:).md)
  Asks the domain to sync the specified known folders.
- [func releaseKnownFolders(NSFileProviderKnownFolders, localizedReason: String, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/releaseknownfolders(_:localizedreason:completionhandler:).md)
  Asks the system to stop replicating the specified known folders in the domain.
- [struct NSFileProviderKnownFolders](nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [protocol NSFileProviderKnownFolderSupporting](nsfileproviderknownfoldersupporting.md)
  A protocol that defines the interface for sharing known-folder locations with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfolderlocations)*