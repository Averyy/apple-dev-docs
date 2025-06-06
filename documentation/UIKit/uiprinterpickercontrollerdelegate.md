# UIPrinterPickerControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods for managing the presentation and dismissal of a printer picker interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIPrinterPickerControllerDelegate : NSObjectProtocol
```

#### Overview

You also use the methods of this protocol to influence the content displayed in the picker and to respond when the user selects a printer. Implement the methods of this protocol in your own custom object and assign that object to the delegate property of your [`UIPrinterPickerController`](uiprinterpickercontroller.md) object before presenting it. When you present the picker, it calls the methods of your delegate at appropriate times to ask for information or provide you with information about the state of the picker interface. For more information about presenting a printer picker interface, see [`UIPrinterPickerController`](uiprinterpickercontroller.md).

## Topics

### Filtering the List of Printers
- [func printerPickerController(UIPrinterPickerController, shouldShow: UIPrinter) -> Bool](uiprinterpickercontrollerdelegate/printerpickercontroller(_:shouldshow:).md)
  Asks the delegate if the specified printer should be included in the picker.
### Handling the Printer Selection
- [func printerPickerControllerDidSelectPrinter(UIPrinterPickerController)](uiprinterpickercontrollerdelegate/printerpickercontrollerdidselectprinter(_:).md)
  Tells the delegate that a printer was selected.
### Responding to Printer Picker Events
- [func printerPickerControllerParentViewController(UIPrinterPickerController) -> UIViewController?](uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(_:).md)
  Asks the delegate to provide the view controller to act as the parent of the printer picker.
- [func printerPickerControllerWillPresent(UIPrinterPickerController)](uiprinterpickercontrollerdelegate/printerpickercontrollerwillpresent(_:).md)
  Tells the delegate that the printer picker is about to be displayed.
- [func printerPickerControllerDidPresent(UIPrinterPickerController)](uiprinterpickercontrollerdelegate/printerpickercontrollerdidpresent(_:).md)
  Tells the delegate that the printer picker was displayed and is now visible.
- [func printerPickerControllerWillDismiss(UIPrinterPickerController)](uiprinterpickercontrollerdelegate/printerpickercontrollerwilldismiss(_:).md)
  Tells the delegate that the printer picker is about to be dismissed.
- [func printerPickerControllerDidDismiss(UIPrinterPickerController)](uiprinterpickercontrollerdelegate/printerpickercontrollerdiddismiss(_:).md)
  Tells the delegate that the printer picker was dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UIPrinterPickerControllerDelegate)?](uiprinterpickercontroller/delegate.md)
  The delegate for the printer picker controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate)*