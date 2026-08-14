# BEExportOptions

**Framework**: BrowserKit  
**Kind**: class

Options that identify data to export.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEExportOptions
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Overview

This class identifies the selected types of items to export, including bookmarks, page visit history, reading list items, and browser extensions. People make their selections in the framework-provided transfer sheet. When someone dismisses the sheet, the system returns an instance of this class. For more information, see [`Transferring browsing data to another browser`](transferring-browsing-data-to-another-browser.md).

This class’s [`exportToFiles`](beexportoptions/exporttofiles.md) property is `true` when someone chooses to export to files. In this case, the system cancels the browser-to-browser data transfer, and your app exports the browsing data to disk using a file format of your choosing.

## Topics

### Creating export options
- [init?(coder: NSCoder)](beexportoptions/init(coder:).md)
  Initializes exports from a decoder.
- [init(exportToFiles: Bool, dataTypes: BEExportOptions.DataTypes)](beexportoptions/init(exporttofiles:datatypes:).md)
  Initializes exports with file information and data types.
### Configuring export preferences
- [var dataTypes: BEExportOptions.DataTypes](beexportoptions/datatypes-swift.property.md)
  The set of data types to include in the export.
- [BEExportOptions.DataTypes](beexportoptions/datatypes-swift.struct.md)
  Types of exported browser data.
- [var exportToFiles: Bool](beexportoptions/exporttofiles.md)
  A Boolean value that indicates whether to export to files.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class BEBrowserDataExportManager](bebrowserdataexportmanager.md)
  A class that handles exporting browsing data to other browsers.
- [class BEExportMetadata](beexportmetadata.md)
  Metadata that describes available browser data for export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportoptions)*