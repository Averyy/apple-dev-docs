# UIPrinter

**Framework**: UIKit  
**Kind**: class

A printer on the network.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPrinter
```

#### Overview

You use a printer object to obtain information about a printer so that you can display that information in your app’s interface. You do not use printer objects to communicate with the printer directly.

Most of the time, you use a [`UIPrinterPickerController`](uiprinterpickercontroller.md) object to retrieve a printer object representing the printer selected by the user. If you already have a URL containing the address of a printer—perhaps one that was previously selected by the user—you can use that URL to create a printer object directly. When creating your own printer objects, you must connect to the printer using the [`contactPrinter(_:)`](uiprinter/contactprinter(_:).md) method before retrieving any of the printer’s attributes.

## Topics

### Creating a printer object
- [init(url: URL)](uiprinter/init(url:).md)
  Creates and returns a printer with the specified location.
### Getting the printer’s address
- [var url: URL](uiprinter/url.md)
  The full address of the printer.
### Getting the printer information
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
- [var supportsColor: Bool](uiprinter/supportscolor.md)
  A Boolean value that indicates whether the printer supports color printing.
- [var supportsDuplex: Bool](uiprinter/supportsduplex.md)
  A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.
### Connecting to the printer
- [func contactPrinter(((Bool) -> Void)?)](uiprinter/contactprinter(_:).md)
  Connects to the printer and gathers information about its capabilities.
### Constants
- [UIPrinter.CutterBehavior](uiprinter/cutterbehavior.md)
  Constants that specify the cutter behavior of a roll-fed printer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPrintInfo](uiprintinfo.md)
  Information about a print job that the system uses when it prints.
- [class UIPrintPaper](uiprintpaper.md)
  The size of paper for a print job and the rectangular area that the content prints within.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter)*