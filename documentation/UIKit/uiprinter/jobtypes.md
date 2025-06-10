# UIPrinter.JobTypes

**Framework**: UIKit  
**Kind**: struct

Constants that indicate the types of jobs that the printer supports.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct JobTypes
```

## Topics

### Constants
- [static var unknown: UIPrinter.JobTypes](uiprinter/jobtypes/unknown.md)
  The printer support is unknown.
- [static var document: UIPrinter.JobTypes](uiprinter/jobtypes/document.md)
  The printer supports standard document printing.
- [static var envelope: UIPrinter.JobTypes](uiprinter/jobtypes/envelope.md)
  The printer supports printing on envelopes.
- [static var label: UIPrinter.JobTypes](uiprinter/jobtypes/label.md)
  The printer supports printing on cut labels.
- [static var photo: UIPrinter.JobTypes](uiprinter/jobtypes/photo.md)
  The printer supports printing with photographic print quality.
- [static var receipt: UIPrinter.JobTypes](uiprinter/jobtypes/receipt.md)
  The printer supports printing receipts on a continuous roll of paper.
- [static var roll: UIPrinter.JobTypes](uiprinter/jobtypes/roll.md)
  The printer supports printing documents or photos on a continuous roll of paper.
- [static var largeFormat: UIPrinter.JobTypes](uiprinter/jobtypes/largeformat.md)
  The printer supports printing larger than the ISO A3 size.
- [static var postcard: UIPrinter.JobTypes](uiprinter/jobtypes/postcard.md)
  The printer supports printing on postcards.
### Initializers
- [init(rawValue: Int)](uiprinter/jobtypes/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var displayName: String](uiprinter/displayname.md)
  The human-readable printer name.
- [var displayLocation: String?](uiprinter/displaylocation.md)
  The human-readable text that describes the location of the printer.
- [var makeAndModel: String?](uiprinter/makeandmodel.md)
  A string that contains the manufacturer’s name and the model name of the printer.
- [var supportedJobTypes: UIPrinter.JobTypes](uiprinter/supportedjobtypes.md)
  The capabilities of the printer.
- [var supportsColor: Bool](uiprinter/supportscolor.md)
  A Boolean value that indicates whether the printer supports color printing.
- [var supportsDuplex: Bool](uiprinter/supportsduplex.md)
  A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes)*