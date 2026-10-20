# present(from:in:animated:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func present(from rect: CGRect, in view: UIView, animated: Bool, completionHandler completion: UIPrintInteractionController.CompletionHandler? = nil) -> Bool
```

```objc
- (BOOL) presentFromRect:(CGRect) rect inView:(UIView *) view animated:(BOOL) animated completionHandler:(UIPrintInteractionCompletionHandler) completion;
```

#### Discussion

It is valid to call this method for applications on iPad devices. Calling this method on an iPhone or iPod touch with `animated` set to [`true`](../../Swift/true.md) causes the printing options view to animate upward from the bottom of the screen.

If you call this method when the printing options are already displayed, `UIPrintInteractionController` hides the printing-options popover view. You must call the method again to display the options.

## Parameters

- `rect`: A rectangle that defines the area from which the printing popover view is animated.
- `view`: The view providing the coordinate system for `rect`.
- `animated`: [`true`](../../Swift/true.md) to animate the printing popover view from `item`, [`false`](../../Swift/false.md) to display it immediately.
- `completion`: A block of type [`UIPrintInteractionController.CompletionHandler`](./completionhandler.md) that you implement to handle the conclusion of the print job (for instance, to reset state) and to handle any errors encountered in printing.

## See Also

### Presenting the printing user interface
- [func present(animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](./present%28animated,completionhandler%29.md)
  Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.
- [func present(from: UIBarButtonItem, animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](./present%28from,animated,completionhandler%29.md)
  Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.
- [func dismiss(animated: Bool)](./dismiss%28animated%29.md)
  Dismisses the printing-options sheet or popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/present(from:in:animated:completionhandler:))*