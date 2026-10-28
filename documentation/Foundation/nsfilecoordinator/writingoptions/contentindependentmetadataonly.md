# contentIndependentMetadataOnly

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Select this option when writing to change the file’s metadata only and not its contents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions { get }
```

```c
NSFileCoordinatorWritingContentIndependentMetadataOnly
```

## Discussion

Any changes written to the item’s contents during this coordinated write may not be preserved or may fail. Changing metadata that is related to the item’s content is also not supported, and those changes may not be preserved. For example, changing the value of [`tagNamesKey`](../../urlresourcekey/tagnameskey.md) is supported, but changing the value of [`contentModificationDateKey`](../../urlresourcekey/contentmodificationdatekey.md) is not.

## See Also

### Constants
- [static var forDeleting: NSFileCoordinator.WritingOptions](./fordeleting.md)
- [static var forMoving: NSFileCoordinator.WritingOptions](./formoving.md)
- [static var forMerging: NSFileCoordinator.WritingOptions](./formerging.md)
- [static var forReplacing: NSFileCoordinator.WritingOptions](./forreplacing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions/contentindependentmetadataonly)*