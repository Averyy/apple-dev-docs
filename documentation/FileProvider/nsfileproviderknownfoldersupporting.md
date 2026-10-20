# NSFileProviderKnownFolderSupporting

**Framework**: File Provider  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the interface for sharing known-folder locations with the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol NSFileProviderKnownFolderSupporting : NSObjectProtocol
```

```objc
@protocol NSFileProviderKnownFolderSupporting <NSObject>
```

## Topics

### Providing known-folder locations to the system
- [func getKnownFolderLocations(NSFileProviderKnownFolders, completionHandler: (NSFileProviderKnownFolderLocations?, (any Error)?) -> Void)](./nsfileproviderknownfoldersupporting/getknownfolderlocations%28_,completionhandler%29.md)
  Requests suitable locations for known folders.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Syncing Desktop and Documents folders
- [func claimKnownFolders(NSFileProviderKnownFolderLocations, localizedReason: String, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/claimknownfolders%28_,localizedreason,completionhandler%29.md)
  Asks the domain to sync the specified known folders.
- [func releaseKnownFolders(NSFileProviderKnownFolders, localizedReason: String, completionHandler: ((any Error)?) -> Void)](./nsfileprovidermanager/releaseknownfolders%28_,localizedreason,completionhandler%29.md)
  Asks the system to stop replicating the specified known folders in the domain.
- [struct NSFileProviderKnownFolders](./nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [class NSFileProviderKnownFolderLocations](./nsfileproviderknownfolderlocations.md)
  A class for working with known-folder locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfoldersupporting)*