# forMerging

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var forMerging: NSFileCoordinator.WritingOptions { get }
```

```c
NSFileCoordinatorWritingForMerging
```

## Discussion

When this constant is specified, the file coordinator calls the [`savePresentedItemChanges(completionHandler:)`](../../nsfilepresenter/savepresenteditemchanges%28completionhandler%29.md) method of relevant file presenters to give them a chance to save their changes before your code makes its changes.

## See Also

### Constants
- [static var forDeleting: NSFileCoordinator.WritingOptions](./fordeleting.md)
- [static var forMoving: NSFileCoordinator.WritingOptions](./formoving.md)
- [static var forReplacing: NSFileCoordinator.WritingOptions](./forreplacing.md)
- [static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions](./contentindependentmetadataonly.md)
  Select this option when writing to change the file’s metadata only and not its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/formerging)*