# dataTypes

**Framework**: BrowserKit  
**Kind**: property  
**Role**: Instance Property

The set of data types to include in the export.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var dataTypes: BEExportOptions.DataTypes { get }
```

```objc
@property (nonatomic, readonly) BEExportDataTypes dataTypes;
```

## Mentions

- [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md)

#### Discussion

This property identifies the person’s choice of data to include in the export, as specified in the framework-provided sheet.

## See Also

### Configuring export preferences
- [BEExportOptions.DataTypes](./datatypes-swift.struct.md)
  Types of exported browser data.
- [var exportToFiles: Bool](./exporttofiles.md)
  A Boolean value that indicates whether to export to files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportoptions/datatypes-swift.property)*