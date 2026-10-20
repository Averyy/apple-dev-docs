# supportedKnownFolders

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A list of known folders that the domain can replicate.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var supportedKnownFolders: NSFileProviderKnownFolders { get set }
```

```objc
@property (assign, readwrite) NSFileProviderKnownFolders supportedKnownFolders;
```

## See Also

### Syncing Desktop and Documents folders
- [var replicatedKnownFolders: NSFileProviderKnownFolders](./replicatedknownfolders.md)
  A list of known folders that the domain currently replicates.
- [struct NSFileProviderKnownFolders](../nsfileproviderknownfolders.md)
  Constants that identify known folders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain/supportedknownfolders)*