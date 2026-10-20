# insertView(_:at:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a view to a stack view gravity area at a specified index position.

**Availability**:
- macOS

## Declaration

```swift
func insertView(_ view: NSView, at index: Int, in gravity: NSStackView.Gravity)
```

```objc
- (void) insertView:(NSView *) view atIndex:(NSUInteger) index inGravity:(NSStackViewGravity) gravity;
```

#### Discussion

Calling this method updates the stack view’s layout, which can change the stack view size. As a result, views could detach or clip according to the clipping resistance of the stack view and the visibility priorities of its views.

A view in a detached state is not present in the stack view’s view hierarchy, but it still consumes memory. To respond to detachment and reattachment of views, implement an [`NSStackViewDelegate`](../nsstackviewdelegate.md) object and assign it to the [`delegate`](./delegate.md) property.

## Parameters

- `view`: The view to add to the specified gravity area.
- `index`: The index position, within the gravity area, for the new view. The position of index `0` depends on the stack view layout direction and, for a horizontal stack view, on the user interface layout direction:

  - *Horizontal*: The `0` index for a gravity area is at the leading side, as determined by the value of the inherited [`userInterfaceLayoutDirection`](../nsview/userinterfacelayoutdirection.md) property of the stack view. For a left to right language, index `0` is at the left of the gravity area.
  - *Vertical*: The `0` index for a gravity area is at the top.

  See the [`userInterfaceLayoutDirection`](../nsapplication/userinterfacelayoutdirection.md) property and the [`userInterfaceLayoutDirection`](../nsview/userinterfacelayoutdirection.md) method.

  > ❗ **Important**:  If you specify an out-of-bounds value for the `index` parameter, the system raises an [`rangeException`](../../Foundation/nsexceptionname/rangeexception.md) exception.
- `gravity`: The gravity area that you are adding the specified view to. Valid values are those in the [`NSStackView.Gravity`](./gravity.md) enumeration.

## See Also

### Related Documentation
- [func setVisibilityPriority(NSStackView.VisibilityPriority, for: NSView)](./setvisibilitypriority%28_,for%29.md)
  Sets the Auto Layout priority for a view to remain attached to the stack view when Auto Layout reduces the stack view’s size.
- [var orientation: NSUserInterfaceLayoutOrientation](./orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [func setClippingResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./setclippingresistancepriority%28_,for%29.md)
  Sets the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
### Managing Views in Gravity Areas
- [func addView(NSView, in: NSStackView.Gravity)](./addview%28_,in%29.md)
  Adds a view to the end of the stack view gravity area.
- [func setViews([NSView], in: NSStackView.Gravity)](./setviews%28_,in%29.md)
  Specifies an array of views for a specified gravity area in the stack view, replacing any previous views in that area.
- [func removeView(NSView)](./removeview%28_%29.md)
  Removes a specified view from the stack view.
- [NSStackView.Gravity](./gravity.md)
  The gravity areas available in a stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/insertview(_:at:in:))*