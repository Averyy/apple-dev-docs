# NSFileProviderKnownFolders

**Framework**: File Provider  
**Kind**: struct

Constants that identify known folders.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct NSFileProviderKnownFolders
```

## Topics

### Identifying known folders
- [static var desktop: NSFileProviderKnownFolders](nsfileproviderknownfolders/desktop.md)
- [static var documents: NSFileProviderKnownFolders](nsfileproviderknownfolders/documents.md)
### Creating a known-folder identifier
- [init(rawValue: UInt)](nsfileproviderknownfolders/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var replicatedKnownFolders: NSFileProviderKnownFolders](nsfileproviderdomain/replicatedknownfolders.md)
  A list of known folders that the domain currently replicates.
- [var supportedKnownFolders: NSFileProviderKnownFolders](nsfileproviderdomain/supportedknownfolders.md)
  A list of known folders that the domain can replicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfolders)*