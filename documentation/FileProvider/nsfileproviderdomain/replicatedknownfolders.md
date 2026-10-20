# replicatedKnownFolders

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A list of known folders that the domain currently replicates.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var replicatedKnownFolders: NSFileProviderKnownFolders { get }
```

```objc
@property (assign, readonly) NSFileProviderKnownFolders replicatedKnownFolders;
```

## See Also

### Syncing Desktop and Documents folders
- [var supportedKnownFolders: NSFileProviderKnownFolders](./supportedknownfolders.md)
  A list of known folders that the domain can replicate.
- [struct NSFileProviderKnownFolders](../nsfileproviderknownfolders.md)
  Constants that identify known folders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/replicatedknownfolders)*