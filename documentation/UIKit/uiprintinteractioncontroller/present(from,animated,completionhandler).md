# present(from:animated:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func present(from item: UIBarButtonItem, animated: Bool, completionHandler completion: UIPrintInteractionController.CompletionHandler? = nil) -> Bool
```

```objc
- (BOOL) presentFromBarButtonItem:(UIBarButtonItem *) item animated:(BOOL) animated completionHandler:(UIPrintInteractionCompletionHandler) completion;
```

## Discussion

It is valid to call this method for applications on iPad devices. Calling this method on an iPhone or iPod touch with `animated` set to [`true`](../../Swift/true.md) causes the printing options view to animate upward from the bottom of the screen.

If you call this method when the printing options are already displayed, `UIPrintInteractionController` hides the printing-options popover view. You must call the method again to display the options.

## Parameters

- `item`: The [`UIBarButtonItem`](../uibarbuttonitem.md) object that the user tapped for printing. You are encouraged to use the constant [`UIBarButtonItem.SystemItem.action`](../uibarbuttonitem/systemitem/action.md) when creating a bar-button item for this purpose.
- `animated`: [`true`](../../Swift/true.md) to animate the printing popover view from `item`, [`false`](../../Swift/false.md) to display it immediately.
- `completion`: A block of type [`UIPrintInteractionController.CompletionHandler`](./completionhandler.md) that you implement to handle the conclusion of the print job (for instance, to reset state) and to handle any errors encountered in printing.

## See Also

### Presenting the printing user interface
- [func present(animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](./present%28animated,completionhandler%29.md)
  Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.
- [func present(from: CGRect, in: UIView, animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](./present%28from,in,animated,completionhandler%29.md)
  Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.
- [func dismiss(animated: Bool)](./dismiss%28animated%29.md)
  Dismisses the printing-options sheet or popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/present(from:animated:completionhandler:))*