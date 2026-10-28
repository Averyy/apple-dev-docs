# printerPickerControllerWillPresent(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the printer picker is about to be displayed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func printerPickerControllerWillPresent(_ printerPickerController: UIPrinterPickerController)
```

```objc
- (void) printerPickerControllerWillPresent:(UIPrinterPickerController *) printerPickerController;
```

## Discussion

Use this method to perform any tasks associated with displaying the printer picker controller.

## Parameters

- `printerPickerController`: The printer picker controller object being displayed.

## See Also

### Responding to Printer Picker Events
- [func printerPickerControllerParentViewController(UIPrinterPickerController) -> UIViewController?](./printerpickercontrollerparentviewcontroller%28_%29.md)
  Asks the delegate to provide the view controller to act as the parent of the printer picker.
- [func printerPickerControllerDidPresent(UIPrinterPickerController)](./printerpickercontrollerdidpresent%28_%29.md)
  Tells the delegate that the printer picker was displayed and is now visible.
- [func printerPickerControllerWillDismiss(UIPrinterPickerController)](./printerpickercontrollerwilldismiss%28_%29.md)
  Tells the delegate that the printer picker is about to be dismissed.
- [func printerPickerControllerDidDismiss(UIPrinterPickerController)](./printerpickercontrollerdiddismiss%28_%29.md)
  Tells the delegate that the printer picker was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerwillpresent(_:))*