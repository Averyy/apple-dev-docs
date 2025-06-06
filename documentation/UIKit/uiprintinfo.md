# UIPrintInfo

**Framework**: UIKit  
**Kind**: class

Information about a print job that the system uses when it prints.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPrintInfo
```

#### Overview

A [`UIPrintInfo`](uiprintinfo.md) object encapsulates information about a print job, including printer identifier, job name, output type (photo, normal, grayscale), orientation (portrait or landscape), and any selected duplex mode.

Typically, you create a [`UIPrintInfo`](uiprintinfo.md) object and assign it to the [`printInfo`](uiprintinteractioncontroller/printinfo.md) property of the shared [`UIPrintInteractionController`](uiprintinteractioncontroller.md) instance. However, it isn’t necessary to create a [`UIPrintInfo`](uiprintinfo.md) object for a print job; UIKit assumes certain defaults. In the printing-options user interface, users can select the printer, single-sided or double-sided printing for duplex printers, and (if the app allows it) a range of pages to print.

## Topics

### Creating a print info object
- [class func printInfo() -> UIPrintInfo](uiprintinfo/printinfo.md)
  Returns a print-information object initialized with default values.
- [init(dictionary: [AnyHashable : Any]?)](uiprintinfo/init(dictionary:).md)
  Returns a print-information object that is initialized with the data in the passed-in dictionary.
- [var dictionaryRepresentation: [AnyHashable : Any]](uiprintinfo/dictionaryrepresentation.md)
  A dictionary representation of a print-information object.
- [init?(coder: NSCoder)](uiprintinfo/init(coder:).md)
  Creates a print info object from data in an unarchiver.
### Managing print-job attributes
- [var duplex: UIPrintInfo.Duplex](uiprintinfo/duplex-swift.property.md)
  The duplex mode to use for the print job.
- [UIPrintInfo.Duplex](uiprintinfo/duplex-swift.enum.md)
  Constants that describe the duplex mode of a selected printer.
- [var jobName: String](uiprintinfo/jobname.md)
  The name of the print job.
- [var orientation: UIPrintInfo.Orientation](uiprintinfo/orientation-swift.property.md)
  The orientation of the printed content, portrait or landscape.
- [UIPrintInfo.Orientation](uiprintinfo/orientation-swift.enum.md)
  Constants that describe the orientation of printing on a page.
- [var outputType: UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.property.md)
  The kind of printable content.
- [UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.enum.md)
  Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [var printerID: String?](uiprintinfo/printerid.md)
  An identifier of the printer to use for the print job.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPrinter](uiprinter.md)
  A printer on the network.
- [class UIPrintPaper](uiprintpaper.md)
  The size of paper for a print job and the rectangular area that the content prints within.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo)*