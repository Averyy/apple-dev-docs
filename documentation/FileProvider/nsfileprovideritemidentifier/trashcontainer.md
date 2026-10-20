# trashContainer

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

The persistent identifier for the parent of all trashed items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let trashContainer: NSFileProviderItemIdentifier
```

```c
extern NSFileProviderItemIdentifier const NSFileProviderTrashContainerItemIdentifier;
```

#### Discussion

When the user moves an item to the trash, the system sets its [`parentItemIdentifier`](../nsfileprovideritemprotocol/parentitemidentifier.md) to [`trashContainer`](./trashcontainer.md). Your extension must enumerate all trashed items on request.

## See Also

### Constants
- [static let rootContainer: NSFileProviderItemIdentifier](./rootcontainer.md)
  The persistent identifier for the root directory of the file provider’s shared file hierarchy.
- [static let workingSet: NSFileProviderItemIdentifier](./workingset.md)
  The persistent identifier representing the working set of documents and directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemidentifier/trashcontainer)*