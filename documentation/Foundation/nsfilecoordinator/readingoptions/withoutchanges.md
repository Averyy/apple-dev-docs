# withoutChanges

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
static var withoutChanges: NSFileCoordinator.ReadingOptions { get }
```

```c
NSFileCoordinatorReadingWithoutChanges
```

## Discussion

Specify this constant if your code does not need other objects to save changes first. If you do *not* specify this constant, the [`savePresentedItemChanges(completionHandler:)`](../../nsfilepresenter/savepresenteditemchanges%28completionhandler%29.md) method of relevant file presenters is called before your code reads the item.

## See Also

### Constants
- [static var resolvesSymbolicLink: NSFileCoordinator.ReadingOptions](./resolvessymboliclink.md)
- [static var immediatelyAvailableMetadataOnly: NSFileCoordinator.ReadingOptions](./immediatelyavailablemetadataonly.md)
  Specify this constant if you want to read an item’s metadata without triggering a download.
- [static var forUploading: NSFileCoordinator.ReadingOptions](./foruploading.md)
  Specify this content when reading an item for the purpose of uploading its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/withoutchanges)*