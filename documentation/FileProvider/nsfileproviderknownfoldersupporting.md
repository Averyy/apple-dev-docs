# NSFileProviderKnownFolderSupporting

**Framework**: File Provider  
**Kind**: protocol

A protocol that defines the interface for sharing known-folder locations with the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol NSFileProviderKnownFolderSupporting : NSObjectProtocol
```

## Topics

### Providing known-folder locations to the system
- [func getKnownFolderLocations(NSFileProviderKnownFolders, completionHandler: (NSFileProviderKnownFolderLocations?, (any Error)?) -> Void)](nsfileproviderknownfoldersupporting/getknownfolderlocations(_:completionhandler:).md)
  Requests suitable locations for known folders.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func claimKnownFolders(NSFileProviderKnownFolderLocations, localizedReason: String, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/claimknownfolders(_:localizedreason:completionhandler:).md)
  Asks the domain to sync the specified known folders.
- [func releaseKnownFolders(NSFileProviderKnownFolders, localizedReason: String, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/releaseknownfolders(_:localizedreason:completionhandler:).md)
  Asks the system to stop replicating the specified known folders in the domain.
- [struct NSFileProviderKnownFolders](nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [class NSFileProviderKnownFolderLocations](nsfileproviderknownfolderlocations.md)
  A class for working with known-folder locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfoldersupporting)*