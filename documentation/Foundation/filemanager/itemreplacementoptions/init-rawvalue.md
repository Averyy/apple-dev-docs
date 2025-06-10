# init(rawValue:)

**Framework**: Foundation  
**Kind**: init

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

- [static var usingNewMetadataOnly: FileManager.ItemReplacementOptions](filemanager/itemreplacementoptions/usingnewmetadataonly.md)
  Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).
- [static var withoutDeletingBackupItem: FileManager.ItemReplacementOptions](filemanager/itemreplacementoptions/withoutdeletingbackupitem.md)
  The backup item remains in place after a successful replacement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions/init(rawvalue:))*