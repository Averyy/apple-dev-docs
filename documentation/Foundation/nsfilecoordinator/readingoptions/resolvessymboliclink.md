# resolvesSymbolicLink

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
static var resolvesSymbolicLink: NSFileCoordinator.ReadingOptions { get }
```

#### Discussion

Specify this constant if you want an item that might be a symbolic link to resolve to the file pointed to by that link (instead of to the link itself). When you use this option, the system provides the resolved URL to the accessor block in place of the original URL.

> **Note**:  This option cannot be used with the [`prepare(forReadingItemsAt:options:writingItemsAt:options:error:byAccessor:)`](nsfilecoordinator/prepare(forreadingitemsat:options:writingitemsat:options:error:byaccessor:).md) method.

## See Also

- [static var withoutChanges: NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions/withoutchanges.md)
- [static var immediatelyAvailableMetadataOnly: NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly.md)
  Specify this constant if you want to read an item’s metadata without triggering a download.
- [static var forUploading: NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions/foruploading.md)
  Specify this content when reading an item for the purpose of uploading its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/resolvessymboliclink)*