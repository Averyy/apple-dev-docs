# dismiss(animated:)

**Framework**: UIKit  
**Kind**: method

Dismisses the popover programmatically.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func dismiss(animated: Bool)
```

#### Discussion

You can use this method to dismiss the popover programmatically in response to taps inside the popover window. Taps outside of the popover’s contents automatically dismiss the popover.

## Parameters

- `animated`: Specify   to animate the dismissal of the popover or   to dismiss it immediately.

## See Also

- [func present(from: CGRect, in: UIView, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](uipopovercontroller/present(from:in:permittedarrowdirections:animated:).md)
  Displays the popover and anchors it to the specified location in the view.
- [func present(from: UIBarButtonItem, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](uipopovercontroller/present(from:permittedarrowdirections:animated:).md)
  Displays the popover and anchors it to the specified bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/dismiss(animated:))*