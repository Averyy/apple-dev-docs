# exportToFiles

**Framework**: BrowserKit  
**Kind**: property

A Boolean value that indicates whether to export to files.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var exportToFiles: Bool { get }
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Discussion

If the value of this property is `false`, call [`exportBrowserData(_:)`](bebrowserdataexportmanager/exportbrowserdata(_:).md) to send the browser data directly to the browser that the person chooses in the browsing-data transfer sheet.

If the value of this property is `true`, the system cancels the browser-to-browser data exchange. Instead of streaming export data through [`exportBrowserData(_:)`](bebrowserdataexportmanager/exportbrowserdata(_:).md), export the browsing data to disk using a file format of your choosing.

## See Also

- [var dataTypes: BEExportOptions.DataTypes](beexportoptions/datatypes-swift.property.md)
  The set of data types to include in the export.
- [BEExportOptions.DataTypes](beexportoptions/datatypes-swift.struct.md)
  Types of exported browser data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportoptions/exporttofiles)*