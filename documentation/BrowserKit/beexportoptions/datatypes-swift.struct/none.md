# none

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Type Property

A browser data type that indicates the person chooses to export no data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
static var none: BEExportOptions.DataTypes { get }
```

```c
BEExportDataTypesNone
```

#### Discussion

When [`dataTypes`](../datatypes-swift.property.md) contains this option, don’t proceed with the export.

## See Also

### Identifying browser data types
- [static var bookmarks: BEExportOptions.DataTypes](./bookmarks.md)
  A data type for webpage bookmarks.
- [static var extensions: BEExportOptions.DataTypes](./extensions.md)
  A data type for browser extensions.
- [static var history: BEExportOptions.DataTypes](./history.md)
  A data type for page visit history.
- [static var readingList: BEExportOptions.DataTypes](./readinglist.md)
  A data type for the person’s reading list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportoptions/datatypes-swift.struct/none)*