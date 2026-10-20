# FileManager.ItemReplacementOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSFileManagerItemReplacementOptions : NSUInteger;
```

#### Overview

These options are used by [`replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)`](./replaceitem%28at,withitemat,backupitemname,options,resultingitemurl%29.md).

## Topics

### Using File Replacement Options
- [init(rawValue: UInt)](./itemreplacementoptions/init%28rawvalue%29.md)
  Creates a value for a file replacement operation.
- [static var usingNewMetadataOnly: FileManager.ItemReplacementOptions](./itemreplacementoptions/usingnewmetadataonly.md)
  Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).
- [static var withoutDeletingBackupItem: FileManager.ItemReplacementOptions](./itemreplacementoptions/withoutdeletingbackupitem.md)
  The backup item remains in place after a successful replacement.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Replacing items
- [func replaceItemAt(URL, withItemAt: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions) throws -> URL?](./replaceitemat%28_,withitemat,backupitemname,options%29.md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [func replaceItem(at: URL, withItemAt: URL, backupItemName: String?, options: FileManager.ItemReplacementOptions, resultingItemURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws](./replaceitem%28at,withitemat,backupitemname,options,resultingitemurl%29.md)
  Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions)*