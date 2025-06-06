# setContentCompressionResistancePriority(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the priority with which a view resists being made smaller than its intrinsic size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func setContentCompressionResistancePriority(_ priority: NSLayoutConstraint.Priority, for orientation: NSLayoutConstraint.Orientation)
```

#### Discussion

Custom views should set default values for both orientations on creation, based on their content, typically to [`defaultLow`](nslayoutconstraint/priority-swift.struct/defaultlow.md) or [`defaultHigh`](nslayoutconstraint/priority-swift.struct/defaulthigh.md). When creating user interfaces, the layout designer can modify these priorities for specific views when the overall layout design requires different tradeoffs than the natural priorities of the views being used in the interface.

Subclasses should not override this method.

## Parameters

- `priority`: The new priority.
- `orientation`: The orientation for which the compression resistance priority should be set.

## See Also

- [var fittingSize: NSSize](nsview/fittingsize.md)
  The minimum size of the view that satisfies the constraints it holds.
- [var intrinsicContentSize: NSSize](nsview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](nsview/invalidateintrinsiccontentsize.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsview/contentcompressionresistancepriority(for:).md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsview/contenthuggingpriority(for:).md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsview/setcontenthuggingpriority(_:for:).md)
  Sets the priority with which a view resists being made larger than its intrinsic size.
- [class let noIntrinsicMetric: CGFloat](nsview/nointrinsicmetric.md)
  A value that tells the layout system to ignore the intrinsic size value for a given dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setcontentcompressionresistancepriority(_:for:))*