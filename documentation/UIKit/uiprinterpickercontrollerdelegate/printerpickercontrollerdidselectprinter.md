# printerPickerControllerDidSelectPrinter(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that a printer was selected.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func printerPickerControllerDidSelectPrinter(_ printerPickerController: UIPrinterPickerController)
```

#### Discussion

Implement this method if you want your delegate to be notified of the selected printer. The selected printer can be either one that the user selected or the initially selected printer that you specified when creating your [`UIPrinterPickerController`](uiprinterpickercontroller.md) object.

## Parameters

- `printerPickerController`: The printer picker controller that is providing your delegate with information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontrollerdelegate/printerpickercontrollerdidselectprinter(_:))*