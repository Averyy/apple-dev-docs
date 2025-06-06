# present(from:in:permittedArrowDirections:animated:)

**Framework**: UIKit  
**Kind**: method

Displays the popover and anchors it to the specified location in the view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func present(from rect: CGRect, in view: UIView, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated: Bool)
```

## Parameters

- `rect`: The rectangle in view at which to anchor the popover window.
- `view`: The view containing the anchor rectangle for the popover.
- `arrowDirections`: The arrow directions the popover is permitted to use. You can use this value to force the popover to be positioned on a specific side of the rectangle. However, it is generally better to specify   and let the popover decide the best placement. You must not specify   for this parameter.
- `animated`: Specify   to animate the presentation of the popover or   to display it immediately.

## See Also

- [func present(from: UIBarButtonItem, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](uipopovercontroller/present(from:permittedarrowdirections:animated:).md)
  Displays the popover and anchors it to the specified bar button item.
- [func dismiss(animated: Bool)](uipopovercontroller/dismiss(animated:).md)
  Dismisses the popover programmatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/present(from:in:permittedarrowdirections:animated:))*