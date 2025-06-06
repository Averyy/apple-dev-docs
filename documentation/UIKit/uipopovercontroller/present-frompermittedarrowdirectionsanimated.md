# present(from:permittedArrowDirections:animated:)

**Framework**: UIKit  
**Kind**: method

Displays the popover and anchors it to the specified bar button item.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func present(from item: UIBarButtonItem, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated: Bool)
```

#### Discussion

When presenting the popover, this method adds the toolbar that owns the button to the popover’s list of passthrough views. Thus, taps in the toolbar result in the action methods of the corresponding toolbar items being called. If you want the popover to be dismissed when a different toolbar item is tapped, you must implement that behavior in your action handler methods.

## Parameters

- `item`: The bar button item on which to anchor the popover.
- `arrowDirections`: The arrow directions the popover is permitted to use. You can use this value to force the popover to be positioned on a specific side of the bar button item. However, it is generally better to specify   and let the popover decide the best placement. You must not specify   for this parameter.
- `animated`: Specify   to animate the presentation of the popover or   to display it immediately.

## See Also

- [func present(from: CGRect, in: UIView, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](uipopovercontroller/present(from:in:permittedarrowdirections:animated:).md)
  Displays the popover and anchors it to the specified location in the view.
- [func dismiss(animated: Bool)](uipopovercontroller/dismiss(animated:).md)
  Dismisses the popover programmatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/present(from:permittedarrowdirections:animated:))*