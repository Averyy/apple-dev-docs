# present(from:animated:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Presents the picker in a popover that anchors to the specified bar button item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func present(from item: UIBarButtonItem, animated: Bool, completionHandler completion: UIPrinterPickerController.CompletionHandler? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the picker was displayed or [`false`](https://developer.apple.com/documentation/Swift/false) if the picker was already visible.

#### Discussion

This method presents the picker from a popover or from the view controller you specify using your delegate object. If you provide a delegate object and that object implements the [`printerPickerControllerParentViewController(_:)`](uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(_:).md) method, UIKit presents the picker using the view controller you specify. If you do not provide a delegate, or your delegate object does not implement the [`printerPickerControllerParentViewController(_:)`](uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller(_:).md) method, UIKit presents the picker using a popover attached the bar button you specified in the `item` parameter.

After presenting the picker, the picker interface runs until the user or your app dismisses it. The picker interface provides ways for the user to cancel printing directly, all of which dismiss the picker. You can also dismiss the printer picker programmatically by calling the [`dismiss(animated:)`](uiprinterpickercontroller/dismiss(animated:).md) method.

Calling this method while the picker is currently displayed in a popover dismisses the popover.

## Parameters

- `item`: The bar button item to use as the anchor for the popover.
- `animated`:   to animate the display of the picker or   to display it without animations.
- `completion`: A block to execute when the picker is dismissed. Use this block to receive information about the selected printer or information about any errors that occurred.

## See Also

- [func present(animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](uiprinterpickercontroller/present(animated:completionhandler:).md)
  Presents the picker from a view controller of your app.
- [func present(from: CGRect, in: UIView, animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](uiprinterpickercontroller/present(from:in:animated:completionhandler:).md)
  Presents the picker in a popover that anchors to a rectangle in the specified view.
- [func dismiss(animated: Bool)](uiprinterpickercontroller/dismiss(animated:).md)
  Dismisses the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/present(from:animated:completionhandler:))*