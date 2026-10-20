# present(from:in:permittedArrowDirections:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays the popover and anchors it to the specified location in the view.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
func present(from rect: CGRect, in view: UIView, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated: Bool)
```

```objc
- (void) presentPopoverFromRect:(CGRect) rect inView:(UIView *) view permittedArrowDirections:(UIPopoverArrowDirection) arrowDirections animated:(BOOL) animated;
```

## Parameters

- `rect`: The rectangle in view at which to anchor the popover window.
- `view`: The view containing the anchor rectangle for the popover.
- `arrowDirections`: The arrow directions the popover is permitted to use. You can use this value to force the popover to be positioned on a specific side of the rectangle. However, it is generally better to specify [`any`](../uipopoverarrowdirection/any.md) and let the popover decide the best placement. You must not specify [`unknown`](../uipopoverarrowdirection/unknown.md) for this parameter.
- `animated`: Specify [`true`](../../Swift/true.md) to animate the presentation of the popover or [`false`](../../Swift/false.md) to display it immediately.

## See Also

### Presenting and dismissing the popover
- [func present(from: UIBarButtonItem, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](./present%28from,permittedarrowdirections,animated%29.md)
  Displays the popover and anchors it to the specified bar button item.
- [func dismiss(animated: Bool)](./dismiss%28animated%29.md)
  Dismisses the popover programmatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/present(from:in:permittedarrowdirections:animated:))*