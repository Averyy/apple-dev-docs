# huggingPriority(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the Auto Layout priority for the stack view to minimize its size to fit its contained views as closely as possible, for a specified user interface axis.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func huggingPriority(for orientation: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority
```

```objc
- (NSLayoutPriority) huggingPriorityForOrientation:(NSLayoutConstraintOrientation) orientation;
```

## Return Value

The Auto Layout priority for the stack view to minimize its size.

## Parameters

- `orientation`: The user interface axis (horizontal or vertical) whose hugging priority you want to get from the stack view. Valid values are those in the [`NSUserInterfaceLayoutOrientation`](../nsuserinterfacelayoutorientation.md) enumeration.

## See Also

### Related Documentation
- [func setHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./sethuggingpriority%28_,for%29.md)
  Sets the Auto Layout priority for the stack view to minimize its size, for a specified user interface axis.
### Inspecting a Stack View
- [var views: [NSView]](./views.md)
  The array of views owned by the stack view.
- [func views(in: NSStackView.Gravity) -> [NSView]](./views%28in%29.md)
  Returns the array of views in the specified gravity area in the stack view.
- [var detachedViews: [NSView]](./detachedviews.md)
  An array that contains the detached views from all the stack view’s gravity areas.
- [func clippingResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](./clippingresistancepriority%28for%29.md)
  Returns the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/huggingpriority(for:))*