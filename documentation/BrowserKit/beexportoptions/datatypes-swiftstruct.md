# BEExportOptions.DataTypes

**Framework**: BrowserKit  
**Kind**: struct

Types of exported browser data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct DataTypes
```

## Topics

### Creating a browser data type
- [init(rawValue: UInt)](beexportoptions/datatypes-swift.struct/init(rawvalue:).md)
  Initializes a browser data export option with a value that represents the underlying type.
### Identifying browser data types
- [static var bookmarks: BEExportOptions.DataTypes](beexportoptions/datatypes-swift.struct/bookmarks.md)
  A data type for webpage bookmarks.
- [static var extensions: BEExportOptions.DataTypes](beexportoptions/datatypes-swift.struct/extensions.md)
  A data type for browser extensions.
- [static var history: BEExportOptions.DataTypes](beexportoptions/datatypes-swift.struct/history.md)
  A data type for page visit history.
- [static var readingList: BEExportOptions.DataTypes](beexportoptions/datatypes-swift.struct/readinglist.md)
  A data type for the person’s reading list.
- [static var none: BEExportOptions.DataTypes](beexportoptions/datatypes-swift.struct/none.md)
  A browser data type that indicates the person chooses to export no data.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var dataTypes: BEExportOptions.DataTypes](beexportoptions/datatypes-swift.property.md)
  The set of data types to include in the export.
- [var exportToFiles: Bool](beexportoptions/exporttofiles.md)
  A Boolean value that indicates whether to export to files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportoptions/datatypes-swift.struct)*