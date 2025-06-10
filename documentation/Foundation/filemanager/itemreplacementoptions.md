# FileManager.ItemReplacementOptions

**Framework**: Foundation  
**Kind**: struct

Options for specifying the behavior of file replacement operations.

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
struct ItemReplacementOptions
```

#### Overview

These options are used by [`replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)`](filemanager/replaceitem(at:withitemat:backupitemname:options:resultingitemurl:).md).

## Topics

### Using File Replacement Options
- [init(rawValue: UInt)](filemanager/itemreplacementoptions/init(rawvalue:).md)
  Creates a value for a file replacement operation.
- [static var usingNewMetadataOnly: FileManager.ItemReplacementOptions](filemanager/itemreplacementoptions/usingnewmetadataonly.md)
  Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).
- [static var withoutDeletingBackupItem: FileManager.ItemReplacementOptions](filemanager/itemreplacementoptions/withoutdeletingbackupitem.md)
  The backup item remains in place after a successful replacement.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func replaceItemAt(URL, withItemAt: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> URL?](filemanager/replaceitemat(_:withitemat:backupitemname:options:)-4210g.md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [func replaceItem(at: URL, withItemAt: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws](filemanager/replaceitem(at:withitemat:backupitemname:options:resultingitemurl:).md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions)*