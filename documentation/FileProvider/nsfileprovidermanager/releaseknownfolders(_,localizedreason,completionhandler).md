# releaseKnownFolders(_:localizedReason:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Asks the system to stop replicating the specified known folders in the domain.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func releaseKnownFolders(_ knownFolders: NSFileProviderKnownFolders, localizedReason: String) async throws
```

#### Discussion

Use this method to immediately disable replication of the specified known folders.

## See Also

- [func claimKnownFolders(NSFileProviderKnownFolderLocations, localizedReason: String, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/claimknownfolders(_:localizedreason:completionhandler:).md)
  Asks the domain to sync the specified known folders.
- [struct NSFileProviderKnownFolders](nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [class NSFileProviderKnownFolderLocations](nsfileproviderknownfolderlocations.md)
  A class for working with known-folder locations.
- [protocol NSFileProviderKnownFolderSupporting](nsfileproviderknownfoldersupporting.md)
  A protocol that defines the interface for sharing known-folder locations with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/releaseknownfolders(_:localizedreason:completionhandler:))*