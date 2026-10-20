# rootContainer

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

The persistent identifier for the root directory of the file provider’s shared file hierarchy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let rootContainer: NSFileProviderItemIdentifier
```

```c
extern NSFileProviderItemIdentifier const NSFileProviderRootContainerItemIdentifier;
```

## Mentions

- [Defining Your File Provider’s Content](../defining-your-file-provider-s-content.md)

## See Also

### Constants
- [static let workingSet: NSFileProviderItemIdentifier](./workingset.md)
  The persistent identifier representing the working set of documents and directories.
- [static let trashContainer: NSFileProviderItemIdentifier](./trashcontainer.md)
  The persistent identifier for the parent of all trashed items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemidentifier/rootcontainer)*