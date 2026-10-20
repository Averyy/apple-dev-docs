# init(rawValue:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a value for a file replacement operation.

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
init(rawValue: UInt)
```

## Parameters

- `rawValue`: An initial value for the structure composed as the bitwise OR of zero or more of the valid values.

## See Also

### Using File Replacement Options
- [static var usingNewMetadataOnly: FileManager.ItemReplacementOptions](./usingnewmetadataonly.md)
  Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).
- [static var withoutDeletingBackupItem: FileManager.ItemReplacementOptions](./withoutdeletingbackupitem.md)
  The backup item remains in place after a successful replacement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions/init(rawvalue:))*