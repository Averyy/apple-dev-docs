# UIPrinter.JobTypes

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum UIPrinterJobTypes : NSInteger;
```

## Topics

### Constants
- [static var unknown: UIPrinter.JobTypes](./jobtypes/unknown.md)
  The printer support is unknown.
- [static var document: UIPrinter.JobTypes](./jobtypes/document.md)
  The printer supports standard document printing.
- [static var envelope: UIPrinter.JobTypes](./jobtypes/envelope.md)
  The printer supports printing on envelopes.
- [static var label: UIPrinter.JobTypes](./jobtypes/label.md)
  The printer supports printing on cut labels.
- [static var photo: UIPrinter.JobTypes](./jobtypes/photo.md)
  The printer supports printing with photographic print quality.
- [static var receipt: UIPrinter.JobTypes](./jobtypes/receipt.md)
  The printer supports printing receipts on a continuous roll of paper.
- [static var roll: UIPrinter.JobTypes](./jobtypes/roll.md)
  The printer supports printing documents or photos on a continuous roll of paper.
- [static var largeFormat: UIPrinter.JobTypes](./jobtypes/largeformat.md)
  The printer supports printing larger than the ISO A3 size.
- [static var postcard: UIPrinter.JobTypes](./jobtypes/postcard.md)
  The printer supports printing on postcards.
### Initializers
- [init(rawValue: Int)](./jobtypes/init%28rawvalue%29.md)

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

### Getting the printer information
- [var displayName: String](./displayname.md)
  The human-readable printer name.
- [var displayLocation: String?](./displaylocation.md)
  The human-readable text that describes the location of the printer.
- [var makeAndModel: String?](./makeandmodel.md)
  A string that contains the manufacturer’s name and the model name of the printer.
- [var supportedJobTypes: UIPrinter.JobTypes](./supportedjobtypes.md)
  The capabilities of the printer.
- [var supportsColor: Bool](./supportscolor.md)
  A Boolean value that indicates whether the printer supports color printing.
- [var supportsDuplex: Bool](./supportsduplex.md)
  A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/jobtypes)*