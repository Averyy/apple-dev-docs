# withoutDeletingBackupItem

**Framework**: Foundation  
**Kind**: property

The backup item remains in place after a successful replacement.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var withoutDeletingBackupItem: FileManager.ItemReplacementOptions { get }
```

## See Also

- [init(rawValue: UInt)](filemanager/itemreplacementoptions/init(rawvalue:).md)
  Creates a value for a file replacement operation.
- [static var usingNewMetadataOnly: FileManager.ItemReplacementOptions](filemanager/itemreplacementoptions/usingnewmetadataonly.md)
  Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions/withoutdeletingbackupitem)*