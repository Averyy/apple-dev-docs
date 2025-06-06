# contentHuggingPriority(for:)

**Framework**: AppKit  
**Kind**: method

Returns the priority with which a view resists being made larger than its intrinsic size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func contentHuggingPriority(for orientation: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority
```

#### Return Value

The priority with which the view should resist being enlarged from its intrinsic size in the specified orientation.

#### Discussion

The constraint-based layout system uses these priorities when determining the best layout for views that are encountering constraints that would require them to be larger than their intrinsic size.

Subclasses should not override this method. Instead, custom views should set default values for their content on creation, typically to [`defaultLow`](nslayoutconstraint/priority-swift.struct/defaultlow.md) or [`defaultHigh`](nslayoutconstraint/priority-swift.struct/defaulthigh.md).

## Parameters

- `orientation`: The orientation of the dimension of the view that might be enlarged.

## See Also

- [var fittingSize: NSSize](nsview/fittingsize.md)
  The minimum size of the view that satisfies the constraints it holds.
- [var intrinsicContentSize: NSSize](nsview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](nsview/invalidateintrinsiccontentsize.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsview/contentcompressionresistancepriority(for:).md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsview/setcontentcompressionresistancepriority(_:for:).md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsview/setcontenthuggingpriority(_:for:).md)
  Sets the priority with which a view resists being made larger than its intrinsic size.
- [class let noIntrinsicMetric: CGFloat](nsview/nointrinsicmetric.md)
  A value that tells the layout system to ignore the intrinsic size value for a given dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/contenthuggingpriority(for:))*