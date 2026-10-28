# releaseKnownFolders(_:localizedReason:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Asks the system to stop replicating the specified known folders in the domain.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func releaseKnownFolders(_ knownFolders: NSFileProviderKnownFolders, localizedReason: String, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func releaseKnownFolders(_ knownFolders: NSFileProviderKnownFolders, localizedReason: String) async throws
```

```objc
- (void) releaseKnownFolders:(NSFileProviderKnownFolders) knownFolders localizedReason:(NSString *) localizedReason completionHandler:(void (^)(NSError *)) completionHandler;
```

## Discussion

Use this method to immediately disable replication of the specified known folders.

## See Also

### Syncing Desktop and Documents folders
- [func claimKnownFolders(NSFileProviderKnownFolderLocations, localizedReason: String, completionHandler: ((any Error)?) -> Void)](./claimknownfolders%28_,localizedreason,completionhandler%29.md)
  Asks the domain to sync the specified known folders.
- [struct NSFileProviderKnownFolders](../nsfileproviderknownfolders.md)
  Constants that identify known folders.
- [class NSFileProviderKnownFolderLocations](../nsfileproviderknownfolderlocations.md)
  A class for working with known-folder locations.
- [protocol NSFileProviderKnownFolderSupporting](../nsfileproviderknownfoldersupporting.md)
  A protocol that defines the interface for sharing known-folder locations with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/releaseknownfolders(_:localizedreason:completionhandler:))*