# present(from:permittedArrowDirections:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays the popover and anchors it to the specified bar button item.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
func present(from item: UIBarButtonItem, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated: Bool)
```

```objc
- (void) presentPopoverFromBarButtonItem:(UIBarButtonItem *) item permittedArrowDirections:(UIPopoverArrowDirection) arrowDirections animated:(BOOL) animated;
```

#### Discussion

When presenting the popover, this method adds the toolbar that owns the button to the popover’s list of passthrough views. Thus, taps in the toolbar result in the action methods of the corresponding toolbar items being called. If you want the popover to be dismissed when a different toolbar item is tapped, you must implement that behavior in your action handler methods.

## Parameters

- `item`: The bar button item on which to anchor the popover.
- `arrowDirections`: The arrow directions the popover is permitted to use. You can use this value to force the popover to be positioned on a specific side of the bar button item. However, it is generally better to specify [`any`](../uipopoverarrowdirection/any.md) and let the popover decide the best placement. You must not specify [`unknown`](../uipopoverarrowdirection/unknown.md) for this parameter.
- `animated`: Specify [`true`](../../Swift/true.md) to animate the presentation of the popover or [`false`](../../Swift/false.md) to display it immediately.

## See Also

### Presenting and dismissing the popover
- [func present(from: CGRect, in: UIView, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](./present%28from,in,permittedarrowdirections,animated%29.md)
  Displays the popover and anchors it to the specified location in the view.
- [func dismiss(animated: Bool)](./dismiss%28animated%29.md)
  Dismisses the popover programmatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/present(from:permittedarrowdirections:animated:))*