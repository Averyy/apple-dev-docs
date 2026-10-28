# present(from:animated:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents the picker in a popover that anchors to the specified bar button item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func present(from item: UIBarButtonItem, animated: Bool, completionHandler completion: UIPrinterPickerController.CompletionHandler? = nil) -> Bool
```

```objc
- (BOOL) presentFromBarButtonItem:(UIBarButtonItem *) item animated:(BOOL) animated completionHandler:(UIPrinterPickerCompletionHandler) completion;
```

## Return Value

[`true`](../../Swift/true.md) if the picker was displayed or [`false`](../../Swift/false.md) if the picker was already visible.

## Discussion

This method presents the picker from a popover or from the view controller you specify using your delegate object. If you provide a delegate object and that object implements the [`printerPickerControllerParentViewController(_:)`](../uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller%28_%29.md) method, UIKit presents the picker using the view controller you specify. If you do not provide a delegate, or your delegate object does not implement the [`printerPickerControllerParentViewController(_:)`](../uiprinterpickercontrollerdelegate/printerpickercontrollerparentviewcontroller%28_%29.md) method, UIKit presents the picker using a popover attached the bar button you specified in the `item` parameter.

After presenting the picker, the picker interface runs until the user or your app dismisses it. The picker interface provides ways for the user to cancel printing directly, all of which dismiss the picker. You can also dismiss the printer picker programmatically by calling the [`dismiss(animated:)`](./dismiss%28animated%29.md) method.

Calling this method while the picker is currently displayed in a popover dismisses the popover.

## Parameters

- `item`: The bar button item to use as the anchor for the popover.
- `animated`: [`true`](../../Swift/true.md) to animate the display of the picker or [`false`](../../Swift/false.md) to display it without animations.
- `completion`: A block to execute when the picker is dismissed. Use this block to receive information about the selected printer or information about any errors that occurred.

## See Also

### Presenting and dismissing the picker
- [func present(animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](./present%28animated,completionhandler%29.md)
  Presents the picker from a view controller of your app.
- [func present(from: CGRect, in: UIView, animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](./present%28from,in,animated,completionhandler%29.md)
  Presents the picker in a popover that anchors to a rectangle in the specified view.
- [func dismiss(animated: Bool)](./dismiss%28animated%29.md)
  Dismisses the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/present(from:animated:completionhandler:))*