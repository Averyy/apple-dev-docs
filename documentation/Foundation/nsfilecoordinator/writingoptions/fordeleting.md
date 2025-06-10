# forDeleting

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

When this constant is specified, the file coordinator calls the [`accommodatePresentedItemDeletion(completionHandler:)`](nsfilepresenter/accommodatepresenteditemdeletion(completionhandler:).md) or [`accommodatePresentedSubitemDeletion(at:completionHandler:)`](nsfilepresenter/accommodatepresentedsubitemdeletion(at:completionhandler:).md) method of relevant file presenters to give them a chance to make adjustments before the item is deleted.

## See Also

- [static var forMoving: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/formoving.md)
- [static var forMerging: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/formerging.md)
- [static var forReplacing: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/forreplacing.md)
- [static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/contentindependentmetadataonly.md)
  Select this option when writing to change the file’s metadata only and not its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/fordeleting)*