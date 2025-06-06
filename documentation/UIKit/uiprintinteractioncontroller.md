# UIPrintInteractionController

**Framework**: UIKit  
**Kind**: class

A user interface that manages the printing of documents, images, and other printable content in iOS.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPrintInteractionController
```

#### Overview

[`UIPrintInteractionController`](uiprintinteractioncontroller.md) is the central class for printing in iOS. The shared instance of it represents a print job. A print job includes the content to print and information and options related to its printing, such as output type, job name, paper size, and orientation.

[`UIPrintInteractionController`](uiprintinteractioncontroller.md) has four mutually exclusive properties for giving it the content to print:

- [`printingItem`](uiprintinteractioncontroller/printingitem.md) takes a single print-ready object.
- [`printingItems`](uiprintinteractioncontroller/printingitems.md) takes an array of print-ready objects.
- [`printFormatter`](uiprintinteractioncontroller/printformatter.md) takes a print formatter, an object that knows how to lay out content of a certain type.
- [`printPageRenderer`](uiprintinteractioncontroller/printpagerenderer.md) takes a page renderer, a custom object that draws the content for printing.

If the [`showsPageRange`](uiprintinteractioncontroller/showspagerange.md) property is [`true`](https://developer.apple.com/documentation/swift/true), the number of pages is more than 1, and you assign an object to any of these properties except for the [`printingItems`](uiprintinteractioncontroller/printingitems.md) property, the printing options include a control that allows users to select a page range.

When users tap a print button on the app’s user interface, a controller object of the app should respond to the action message by obtaining the shared instance of [`UIPrintInteractionController`](uiprintinteractioncontroller.md) and preparing it for the print job. When the app calls one of the `present...` methods (for example, [`present(animated:completionHandler:)`](uiprintinteractioncontroller/present(animated:completionhandler:).md)), [`UIPrintInteractionController`](uiprintinteractioncontroller.md) displays a view containing printing options. This interface is simple, allowing users to select a printer, specify the number of copies and possibly a range of pages, and choose single-sided or double-sided printing (if the printer supports duplex printing). When users make their selections and tap Print, the print job begins.

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/system-capabilities/printing/).

## Topics

### Getting the shared controller instance
- [class var shared: UIPrintInteractionController](uiprintinteractioncontroller/shared.md)
  The shared print-interaction controller object.
### Assigning the delegate
- [var delegate: (any UIPrintInteractionControllerDelegate)?](uiprintinteractioncontroller/delegate.md)
  The delegate of the print-interaction controller.
- [protocol UIPrintInteractionControllerDelegate](uiprintinteractioncontrollerdelegate.md)
  An optional set of methods that the delegate of the shared print-interaction controller implements.
### Determining printability
- [class var isPrintingAvailable: Bool](uiprintinteractioncontroller/isprintingavailable.md)
  A Boolean value that indicates whether the device supports printing.
- [class func canPrint(Data) -> Bool](uiprintinteractioncontroller/canprint(_:)-4e0bs.md)
  Returns a Boolean value that indicates whether UIKit can print the contents of a data object.
- [class func canPrint(URL) -> Bool](uiprintinteractioncontroller/canprint(_:)-364vj.md)
  Returns a Boolean value that indicates whether UIKit can print the file that the specified URL references.
- [class var printableUTIs: Set<String>](uiprintinteractioncontroller/printableutis.md)
  Returns a set of the Uniform Type Identifiers for the types of data that UIKit can print.
### Providing the source of printable content
- [var printingItem: Any?](uiprintinteractioncontroller/printingitem.md)
  A single ready-to-print object.
- [var printingItems: [Any]?](uiprintinteractioncontroller/printingitems.md)
  An array of ready-to-print objects.
- [var printPageRenderer: UIPrintPageRenderer?](uiprintinteractioncontroller/printpagerenderer.md)
  An object that draws pages of printable content when UIKit requests it.
- [var printFormatter: UIPrintFormatter?](uiprintinteractioncontroller/printformatter.md)
  An object that lays out the content of pages according to the kind of content.
### Presenting the printing user interface
- [func present(animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](uiprintinteractioncontroller/present(animated:completionhandler:).md)
  Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.
- [func present(from: UIBarButtonItem, animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](uiprintinteractioncontroller/present(from:animated:completionhandler:).md)
  Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.
- [func present(from: CGRect, in: UIView, animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](uiprintinteractioncontroller/present(from:in:animated:completionhandler:).md)
  Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.
- [func dismiss(animated: Bool)](uiprintinteractioncontroller/dismiss(animated:).md)
  Dismisses the printing-options sheet or popover.
### Printing directly to a printer
- [func print(to: UIPrinter, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](uiprintinteractioncontroller/print(to:completionhandler:).md)
  Prints directly to the specified printer.
- [UIPrintInteractionController.CompletionHandler](uiprintinteractioncontroller/completionhandler.md)
  A completion handler for responding to the completion of a print job or for handling printing errors.
### Accessing print-job information
- [var printInfo: UIPrintInfo?](uiprintinteractioncontroller/printinfo.md)
  An object that encapsulates information about the print job.
- [var printPaper: UIPrintPaper?](uiprintinteractioncontroller/printpaper.md)
  An object that represents the paper size and printing area for the print job.
- [var showsNumberOfCopies: Bool](uiprintinteractioncontroller/showsnumberofcopies.md)
  A Boolean value that determines whether the printing options include the number of copies.
- [var showsPaperSelectionForLoadedPapers: Bool](uiprintinteractioncontroller/showspaperselectionforloadedpapers.md)
  A Boolean value that determines whether the paper selection menu displays.
- [var showsPaperOrientation: Bool](uiprintinteractioncontroller/showspaperorientation.md)
  A Boolean value that indicates whether the printing options include the paper-orientation control.
- [var showsPageRange: Bool](uiprintinteractioncontroller/showspagerange.md)
  A Boolean value that determines whether the printing options include a page-range control.
### Handling printing errors
- [let UIPrintErrorDomain: String](uiprinterrordomain.md)
  The string constant that defines the UIKit printing error domain.
- [struct UIPrintError](uiprinterror.md)
  A structure that contains information about a printing error.
- [UIPrintError.Code](uiprinterror/code.md)
  Constants that specify the print error code.

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

- [class UIPrinterPickerController](uiprinterpickercontroller.md)
  A view controller that displays the standard interface for selecting a printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller)*