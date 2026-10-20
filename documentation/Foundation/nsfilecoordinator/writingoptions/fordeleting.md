# forDeleting

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
static var forDeleting: NSFileCoordinator.WritingOptions { get }
```

```c
NSFileCoordinatorWritingForDeleting
```

#### Discussion

When this constant is specified, the file coordinator calls the [`accommodatePresentedItemDeletion(completionHandler:)`](../../nsfilepresenter/accommodatepresenteditemdeletion%28completionhandler%29.md) or [`accommodatePresentedSubitemDeletion(at:completionHandler:)`](../../nsfilepresenter/accommodatepresentedsubitemdeletion%28at,completionhandler%29.md) method of relevant file presenters to give them a chance to make adjustments before the item is deleted.

## See Also

### Constants
- [static var forMoving: NSFileCoordinator.WritingOptions](./formoving.md)
- [static var forMerging: NSFileCoordinator.WritingOptions](./formerging.md)
- [static var forReplacing: NSFileCoordinator.WritingOptions](./forreplacing.md)
- [static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions](./contentindependentmetadataonly.md)
  Select this option when writing to change the file’s metadata only and not its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/fordeleting)*