# NSFileProviderKnownFolderLocations

**Framework**: File Provider  
**Kind**: class  
**Role**: Class

A class for working with known-folder locations.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class NSFileProviderKnownFolderLocations
```

```objc
@interface NSFileProviderKnownFolderLocations : NSObject
```

## Topics

### Identifying known-folder locations
- [var desktopLocation: NSFileProviderKnownFolderLocations.Location?](./nsfileproviderknownfolderlocations/desktoplocation.md)
- [var documentsLocation: NSFileProviderKnownFolderLocations.Location?](./nsfileproviderknownfolderlocations/documentslocation.md)
- [NSFileProviderKnownFolderLocations.Location](./nsfileproviderknownfolderlocations/location.md)
### Configuring folder options
- [var shouldCreateBinaryCompatibilitySymlink: Bool](./nsfileproviderknownfolderlocations/shouldcreatebinarycompatibilitysymlink.md)
### Creating a known-folder locations object
- [init()](./nsfileproviderknownfolderlocations/init%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Syncing Desktop and Documents folders
- [func claimKnownFolders(NSFileProviderKnownFolderLocations, localizedReason: String, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/claimknownfolders%28_,localizedreason,completionhandler%29.md)
  Asks the domain to sync the specified known folders.
- [func releaseKnownFolders(NSFileProviderKnownFolders, localizedReason: String, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/releaseknownfolders%28_,localizedreason,completionhandler%29.md)
  Asks the system to stop replicating the specified known folders in the domain.
- [struct NSFileProviderKnownFolders](./nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [protocol NSFileProviderKnownFolderSupporting](./nsfileproviderknownfoldersupporting.md)
  A protocol that defines the interface for sharing known-folder locations with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfolderlocations)*