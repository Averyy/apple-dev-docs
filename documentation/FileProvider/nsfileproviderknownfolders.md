# NSFileProviderKnownFolders

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Constants that identify known folders.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct NSFileProviderKnownFolders
```

```c
enum NSFileProviderKnownFolders : NSUInteger;
```

## Topics

### Identifying known folders
- [static var desktop: NSFileProviderKnownFolders](./nsfileproviderknownfolders/desktop.md)
- [static var documents: NSFileProviderKnownFolders](./nsfileproviderknownfolders/documents.md)
### Creating a known-folder identifier
- [init(rawValue: UInt)](./nsfileproviderknownfolders/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Syncing Desktop and Documents folders
- [var replicatedKnownFolders: NSFileProviderKnownFolders](./nsfileproviderdomain/replicatedknownfolders.md)
  A list of known folders that the domain currently replicates.
- [var supportedKnownFolders: NSFileProviderKnownFolders](./nsfileproviderdomain/supportedknownfolders.md)
  A list of known folders that the domain can replicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfolders)*