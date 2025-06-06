# UIPrinterPickerController

**Framework**: UIKit  
**Kind**: class

A view controller that displays the standard interface for selecting a printer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPrinterPickerController
```

#### Overview

You can use a printer picker controller to display a list of printers to the user prior to printing a document, photo, or other content. Printer pickers display all pickers normally but you can filter out printers by assigning an appropriate delegate object to the picker before displaying it.

A printer picker controller coordinates the presentation and dismissal of its interface with its associated delegate object. The delegate object is an object that you provide and that conforms to the [`UIPrinterPickerControllerDelegate`](uiprinterpickercontrollerdelegate.md) protocol. When the user selects a printer, the picker also notifies the delegate of the selection.

A printer picker controller isn’t a view controller, so you don’t present it the way you do other view controllers. You present the picker using one of the presentation methods of this class. Those methods work with the picker’s delegate object to determine the most appropriate way to present the picker. If the delegate implements the [`printerPickerControllerParentViewController(_:)`](uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(_:).md) method, the picker presents itself using the view controller returned by that method. Some presentation methods may present the picker using a popover instead.

For more information about the picker delegate methods, see [`UIPrinterPickerControllerDelegate`](uiprinterpickercontrollerdelegate.md).

## Topics

### Creating a picker controller
- [init(initiallySelectedPrinter: UIPrinter?)](uiprinterpickercontroller/init(initiallyselectedprinter:).md)
  Creates and returns a printer picker with an initially selected printer object.
### Managing the printer picker interface
- [var delegate: (any UIPrinterPickerControllerDelegate)?](uiprinterpickercontroller/delegate.md)
  The delegate for the printer picker controller.
- [protocol UIPrinterPickerControllerDelegate](uiprinterpickercontrollerdelegate.md)
  A set of methods for managing the presentation and dismissal of a printer picker interface.
### Presenting and dismissing the picker
- [func present(animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](uiprinterpickercontroller/present(animated:completionhandler:).md)
  Presents the picker from a view controller of your app.
- [func present(from: UIBarButtonItem, animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](uiprinterpickercontroller/present(from:animated:completionhandler:).md)
  Presents the picker in a popover that anchors to the specified bar button item.
- [func present(from: CGRect, in: UIView, animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](uiprinterpickercontroller/present(from:in:animated:completionhandler:).md)
  Presents the picker in a popover that anchors to a rectangle in the specified view.
- [func dismiss(animated: Bool)](uiprinterpickercontroller/dismiss(animated:).md)
  Dismisses the picker.
### Getting the selected printer
- [var selectedPrinter: UIPrinter?](uiprinterpickercontroller/selectedprinter.md)
  The selected printer.
### Constants
- [UIPrinterPickerController.CompletionHandler](uiprinterpickercontroller/completionhandler.md)
  The completion handler to execute when dismissing a printer picker controller.

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

- [class UIPrintInteractionController](uiprintinteractioncontroller.md)
  A user interface that manages the printing of documents, images, and other printable content in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller)*