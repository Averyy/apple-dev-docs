# exportToFiles

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to export to files.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var exportToFiles: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL exportToFiles;
```

## Mentions

- [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md)

#### Discussion

If the value of this property is `false`, call [`exportBrowserData(_:)`](../bebrowserdataexportmanager/exportbrowserdata%28_%29.md) to send the browser data directly to the browser that the person chooses in the browsing-data transfer sheet.

If the value of this property is `true`, the system cancels the browser-to-browser data exchange. Instead of streaming export data through [`exportBrowserData(_:)`](../bebrowserdataexportmanager/exportbrowserdata%28_%29.md), export the browsing data to disk using a file format of your choosing.

## See Also

### Configuring export preferences
- [var dataTypes: BEExportOptions.DataTypes](./datatypes-swift.property.md)
  The set of data types to include in the export.
- [BEExportOptions.DataTypes](./datatypes-swift.struct.md)
  Types of exported browser data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportoptions/exporttofiles)*