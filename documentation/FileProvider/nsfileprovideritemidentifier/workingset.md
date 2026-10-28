# workingSet

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

The persistent identifier representing the working set of documents and directories.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let workingSet: NSFileProviderItemIdentifier
```

```c
extern NSFileProviderItemIdentifier const NSFileProviderWorkingSetContainerItemIdentifier;
```

## Mentions

- [Synchronizing the File Provider Extension](../synchronizing-the-file-provider-extension.md)
- [Defining Your File Provider’s Content](../defining-your-file-provider-s-content.md)

## Discussion

For more information about the working set, see  [Create the Working Set and Enumerate its Content](../defining-your-file-provider-s-content.md#Create-the-Working-Set-and-Enumerate-its-Content).

## See Also

### Constants
- [static let rootContainer: NSFileProviderItemIdentifier](./rootcontainer.md)
  The persistent identifier for the root directory of the file provider’s shared file hierarchy.
- [static let trashContainer: NSFileProviderItemIdentifier](./trashcontainer.md)
  The persistent identifier for the parent of all trashed items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemidentifier/workingset)*