# present(from:animated:completionHandler:)

**Framework**: UIKit  
**Kind**: method

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

#### Discussion

It is valid to call this method for applications on iPad devices. Calling this method on an iPhone or iPod touch with `animated` set to [`true`](https://developer.apple.com/documentation/swift/true) causes the printing options view to animate upward from the bottom of the screen.

If you call this method when the printing options are already displayed, `UIPrintInteractionController` hides the printing-options popover view. You must call the method again to display the options.

## Parameters

- `item`: The [`UIBarButtonItem`](uibarbuttonitem.md) object that the user tapped for printing. You are encouraged to use the constant [`UIBarButtonItem.SystemItem.action`](uibarbuttonitem/systemitem/action.md) when creating a bar-button item for this purpose.
- `animated`: [`true`](https://developer.apple.com/documentation/swift/true) to animate the printing popover view from `item`, [`false`](https://developer.apple.com/documentation/swift/false) to display it immediately.
- `completion`: A block of type [`UIPrintInteractionController.CompletionHandler`](uiprintinteractioncontroller/completionhandler.md) that you implement to handle the conclusion of the print job (for instance, to reset state) and to handle any errors encountered in printing.

## See Also

- [func present(animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](uiprintinteractioncontroller/present(animated:completionhandler:).md)
  Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.
- [func present(from: CGRect, in: UIView, animated: Bool, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](uiprintinteractioncontroller/present(from:in:animated:completionhandler:).md)
  Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.
- [func dismiss(animated: Bool)](uiprintinteractioncontroller/dismiss(animated:).md)
  Dismisses the printing-options sheet or popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/present(from:animated:completionhandler:))*