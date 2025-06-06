# claimKnownFolders(_:localizedReason:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Asks the domain to sync the specified known folders.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func claimKnownFolders(_ knownFolders: NSFileProviderKnownFolderLocations, localizedReason: String) async throws
```

#### Discussion

Use this method to claim a set of known folders according to the information in the `knownFolders` parameter. The system only enables sync for these folders in the domain if the set of locations is valid and if the user agrees.

## See Also

- [func releaseKnownFolders(NSFileProviderKnownFolders, localizedReason: String, completionHandler: ((any Error)?) -> Void)](nsfileprovidermanager/releaseknownfolders(_:localizedreason:completionhandler:).md)
  Asks the system to stop replicating the specified known folders in the domain.
- [struct NSFileProviderKnownFolders](nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [class NSFileProviderKnownFolderLocations](nsfileproviderknownfolderlocations.md)
  A class for working with known-folder locations.
- [protocol NSFileProviderKnownFolderSupporting](nsfileproviderknownfoldersupporting.md)
  A protocol that defines the interface for sharing known-folder locations with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/claimknownfolders(_:localizedreason:completionhandler:))*