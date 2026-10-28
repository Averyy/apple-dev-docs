# immediatelyAvailableMetadataOnly

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specify this constant if you want to read an item’s metadata without triggering a download.

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
static var immediatelyAvailableMetadataOnly: NSFileCoordinator.ReadingOptions { get }
```

```c
NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly
```

## Discussion

Specifying this option grants the coordinated read immediately (barring any conflicts with other readers, writers or file presenters on the same system), instead of waiting for the system to download the file’s contents and any additional metadata (for example, conflicting versions or thumbnails).

Attempting to actually read the item’s contents during this coordinated read may give unexpected results or fail.

## See Also

### Constants
- [static var withoutChanges: NSFileCoordinator.ReadingOptions](./withoutchanges.md)
- [static var resolvesSymbolicLink: NSFileCoordinator.ReadingOptions](./resolvessymboliclink.md)
- [static var forUploading: NSFileCoordinator.ReadingOptions](./foruploading.md)
  Specify this content when reading an item for the purpose of uploading its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly)*