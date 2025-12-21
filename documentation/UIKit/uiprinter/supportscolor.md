# supportsColor

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the printer supports color printing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var supportsColor: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the printer supports color printing or [`false`](https://developer.apple.com/documentation/Swift/false) if it does not. For printers you create yourself using the [`init(url:)`](uiprinter/init(url:).md) method, the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) until you successfully connect to the printer using the [`contactPrinter(_:)`](uiprinter/contactprinter(_:).md) method.

## See Also

- [var displayName: String](uiprinter/displayname.md)
  The human-readable printer name.
- [var displayLocation: String?](uiprinter/displaylocation.md)
  The human-readable text that describes the location of the printer.
- [var makeAndModel: String?](uiprinter/makeandmodel.md)
  A string that contains the manufacturer’s name and the model name of the printer.
- [var supportedJobTypes: UIPrinter.JobTypes](uiprinter/supportedjobtypes.md)
  The capabilities of the printer.
- [UIPrinter.JobTypes](uiprinter/jobtypes.md)
  Constants that indicate the types of jobs that the printer supports.
- [var supportsDuplex: Bool](uiprinter/supportsduplex.md)
  A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/supportscolor)*