# present(animated:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func present(animated: Bool, completionHandler completion: UIPrintInteractionController.CompletionHandler? = nil) -> Bool
```

```objc
- (BOOL) presentAnimated:(BOOL) animated completionHandler:(UIPrintInteractionCompletionHandler) completion;
```

## Discussion

It is valid to call this method for applications on iPhone and iPod touch devices. Calling this method on an iPad with `animated` set to [`true`](../../Swift/true.md) causes the printing options view to animate from the window frame.

If you call this method when the printing options are already displayed, `UIPrintInteractionController` hides the printing-options sheet. You must call the method again to display the options.

## Parameters

- `animated`: [`true`](../../Swift/true.md) to animate the display of the sheet, [`false`](../../Swift/false.md) to display the sheet immediately.
- `completion`: A block of type [`UIPrintInteractionController.CompletionHandler`](./completionhandler.md) that you implement to handle the conclusion of the print job (for instance, to reset state) and to handle any errors encountered in printing.

## See Also

### Presenting the printing user interface
- [func present(from: UIBarButtonItem, animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](./present%28from,animated,completionhandler%29.md)
  Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.
- [func present(from: CGRect, in: UIView, animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](./present%28from,in,animated,completionhandler%29.md)
  Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.
- [func dismiss(animated: Bool)](./dismiss%28animated%29.md)
  Dismisses the printing-options sheet or popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/present(animated:completionhandler:))*