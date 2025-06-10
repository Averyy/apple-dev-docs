# forMerging

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
static var forMerging: NSFileCoordinator.WritingOptions { get }
```

#### Discussion

When this constant is specified, the file coordinator calls the [`savePresentedItemChanges(completionHandler:)`](nsfilepresenter/savepresenteditemchanges(completionhandler:).md) method of relevant file presenters to give them a chance to save their changes before your code makes its changes.

## See Also

- [static var forDeleting: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/fordeleting.md)
- [static var forMoving: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/formoving.md)
- [static var forReplacing: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/forreplacing.md)
- [static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/contentindependentmetadataonly.md)
  Select this option when writing to change the file’s metadata only and not its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/formerging)*