# printerPickerControllerWillDismiss(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the printer picker is about to be dismissed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printerPickerControllerWillDismiss(_ printerPickerController: UIPrinterPickerController)
```

#### Discussion

Use this method to perform any tasks associated with displaying the printer picker controller.

This method is called when the user dismisses the picker, either by selecting a printer or by canceling the picker interface. This method is not called when you dismiss the picker programmatically using the [`dismiss(animated:)`](uiprinterpickercontroller/dismiss(animated:).md) method.

## Parameters

- `printerPickerController`: The printer picker controller object being dismissed.

## See Also

- [func printerPickerControllerParentViewController(UIPrinterPickerController) -> UIViewController?](uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(_:).md)
  Asks the delegate to provide the view controller to act as the parent of the printer picker.
- [func printerPickerControllerWillPresent(UIPrinterPickerController)](uiprinterpickercontrollerdelegate/printerpickercontrollerwillpresent(_:).md)
  Tells the delegate that the printer picker is about to be displayed.
- [func printerPickerControllerDidPresent(UIPrinterPickerController)](uiprinterpickercontrollerdelegate/printerpickercontrollerdidpresent(_:).md)
  Tells the delegate that the printer picker was displayed and is now visible.
- [func printerPickerControllerDidDismiss(UIPrinterPickerController)](uiprinterpickercontrollerdelegate/printerpickercontrollerdiddismiss(_:).md)
  Tells the delegate that the printer picker was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerwilldismiss(_:))*