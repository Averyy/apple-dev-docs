# BEExportOptions.DataTypes

**Framework**: BrowserKit  
**Kind**: struct  
**Role**: Structure

Types of exported browser data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct DataTypes
```

```c
enum BEExportDataTypes : NSUInteger;
```

## Topics

### Creating a browser data type
- [init(rawValue: UInt)](./datatypes-swift.struct/init%28rawvalue%29.md)
  Initializes a browser data export option with a value that represents the underlying type.
### Identifying browser data types
- [static var bookmarks: BEExportOptions.DataTypes](./datatypes-swift.struct/bookmarks.md)
  A data type for webpage bookmarks.
- [static var extensions: BEExportOptions.DataTypes](./datatypes-swift.struct/extensions.md)
  A data type for browser extensions.
- [static var history: BEExportOptions.DataTypes](./datatypes-swift.struct/history.md)
  A data type for page visit history.
- [static var readingList: BEExportOptions.DataTypes](./datatypes-swift.struct/readinglist.md)
  A data type for the person’s reading list.
- [static var none: BEExportOptions.DataTypes](./datatypes-swift.struct/none.md)
  A browser data type that indicates the person chooses to export no data.

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

### Configuring export preferences
- [var dataTypes: BEExportOptions.DataTypes](./datatypes-swift.property.md)
  The set of data types to include in the export.
- [var exportToFiles: Bool](./exporttofiles.md)
  A Boolean value that indicates whether to export to files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportoptions/datatypes-swift.struct)*