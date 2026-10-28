# dismiss(animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the popover programmatically.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
func dismiss(animated: Bool)
```

```objc
- (void) dismissPopoverAnimated:(BOOL) animated;
```

## Discussion

You can use this method to dismiss the popover programmatically in response to taps inside the popover window. Taps outside of the popover’s contents automatically dismiss the popover.

## Parameters

- `animated`: Specify [`true`](../../Swift/true.md) to animate the dismissal of the popover or [`false`](../../Swift/false.md) to dismiss it immediately.

## See Also

### Presenting and dismissing the popover
- [func present(from: CGRect, in: UIView, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](./present%28from,in,permittedarrowdirections,animated%29.md)
  Displays the popover and anchors it to the specified location in the view.
- [func present(from: UIBarButtonItem, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](./present%28from,permittedarrowdirections,animated%29.md)
  Displays the popover and anchors it to the specified bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/dismiss(animated:))*