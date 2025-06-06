# delegate

**Framework**: UIKit  
**Kind**: property

The delegate for the printer picker controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIPrinterPickerControllerDelegate)? { get set }
```

#### Discussion

Use the delegate object to filter out printers from the displayed list and to respond to events that occur during the presentation of the printer picker. The object you assign to this property must conform to the [`UIPrinterPickerControllerDelegate`](uiprinterpickercontrollerdelegate.md) protocol.

## See Also

- [protocol UIPrinterPickerControllerDelegate](uiprinterpickercontrollerdelegate.md)
  A set of methods for managing the presentation and dismissal of a printer picker interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/delegate)*