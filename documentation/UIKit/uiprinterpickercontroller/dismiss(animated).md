# dismiss(animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the picker.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func dismiss(animated: Bool)
```

```objc
- (void) dismissAnimated:(BOOL) animated;
```

## Discussion

This method dismisses a picker that you previously presented. When using this method to dismiss a picker, the picker does not call the [`printerPickerControllerWillDismiss(_:)`](../uiprinterpickercontrollerdelegate/printerpickercontrollerwilldismiss%28_%29.md) or [`printerPickerControllerDidDismiss(_:)`](../uiprinterpickercontrollerdelegate/printerpickercontrollerdiddismiss%28_%29.md) methods of your delegate object.

User interactions with the picker can also dismiss the picker automatically. For example, if the user selects a printer or cancels the picker, the picker dismisses itself automatically. Use this method to dismiss a picker programmatically in response to other events in your app.

## Parameters

- `animated`: [`true`](../../Swift/true.md) to animate the dismissal of the picker or [`false`](../../Swift/false.md) to remove it without animations.

## See Also

### Presenting and dismissing the picker
- [func present(animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](./present%28animated,completionhandler%29.md)
  Presents the picker from a view controller of your app.
- [func present(from: UIBarButtonItem, animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](./present%28from,animated,completionhandler%29.md)
  Presents the picker in a popover that anchors to the specified bar button item.
- [func present(from: CGRect, in: UIView, animated: Bool, completionHandler: UIPrinterPickerController.CompletionHandler?) -> Bool](./present%28from,in,animated,completionhandler%29.md)
  Presents the picker in a popover that anchors to a rectangle in the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/dismiss(animated:))*