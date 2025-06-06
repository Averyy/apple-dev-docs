# makeAndModel

**Framework**: UIKit  
**Kind**: property

A string that contains the manufacturer’s name and the model name of the printer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var makeAndModel: String? { get }
```

#### Discussion

The string in this property is provided by the printer and usually consists of the manufacturer’s name, the model name of the printer, and the model number of the printer.

For printers you create yourself using the [`init(url:)`](uiprinter/init(url:).md) method, the value of this property is `nil` until you successfully connect to the printer using the [`contactPrinter(_:)`](uiprinter/contactprinter(_:).md) method.

## See Also

- [var displayName: String](uiprinter/displayname.md)
  The human-readable printer name.
- [var displayLocation: String?](uiprinter/displaylocation.md)
  The human-readable text that describes the location of the printer.
- [var supportedJobTypes: UIPrinter.JobTypes](uiprinter/supportedjobtypes.md)
  The capabilities of the printer.
- [UIPrinter.JobTypes](uiprinter/jobtypes.md)
  Constants that indicate the types of jobs that the printer supports.
- [var supportsColor: Bool](uiprinter/supportscolor.md)
  A Boolean value that indicates whether the printer supports color printing.
- [var supportsDuplex: Bool](uiprinter/supportsduplex.md)
  A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/makeandmodel)*