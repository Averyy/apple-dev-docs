# printerPickerControllerDidDismiss(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the printer picker was dismissed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func printerPickerControllerDidDismiss(_ printerPickerController: UIPrinterPickerController)
```

```objc
- (void) printerPickerControllerDidDismiss:(UIPrinterPickerController *) printerPickerController;
```

#### Discussion

Use this method to perform any tasks associated with displaying the printer picker controller.

This method is called when the user dismisses the picker, either by selecting a printer or by canceling the picker interface. This method is not called when you dismiss the picker programmatically using the [`dismiss(animated:)`](../uiprinterpickercontroller/dismiss%28animated%29.md) method.

## Parameters

- `printerPickerController`: The printer picker controller object that was dismissed.

## See Also

### Responding to Printer Picker Events
- [func printerPickerControllerParentViewController(UIPrinterPickerController) -> UIViewController?](./printerpickercontrollerparentviewcontroller%28_%29.md)
  Asks the delegate to provide the view controller to act as the parent of the printer picker.
- [func printerPickerControllerWillPresent(UIPrinterPickerController)](./printerpickercontrollerwillpresent%28_%29.md)
  Tells the delegate that the printer picker is about to be displayed.
- [func printerPickerControllerDidPresent(UIPrinterPickerController)](./printerpickercontrollerdidpresent%28_%29.md)
  Tells the delegate that the printer picker was displayed and is now visible.
- [func printerPickerControllerWillDismiss(UIPrinterPickerController)](./printerpickercontrollerwilldismiss%28_%29.md)
  Tells the delegate that the printer picker is about to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerdiddismiss(_:))*