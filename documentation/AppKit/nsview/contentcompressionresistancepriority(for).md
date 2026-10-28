# contentCompressionResistancePriority(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the priority with which a view resists being made smaller than its intrinsic size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func contentCompressionResistancePriority(for orientation: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority
```

```objc
- (NSLayoutPriority) contentCompressionResistancePriorityForOrientation:(NSLayoutConstraintOrientation) orientation;
```

## Return Value

The priority with which the view should resist being compressed from its intrinsic size in the specified orientation.

## Discussion

The constraint-based layout system uses these priorities when determining the best layout for views that are encountering constraints that would require them to be smaller than their intrinsic size.

Subclasses should not override this method. Instead, custom views should set default values for their content on creation, typically to [`defaultLow`](../nslayoutconstraint/priority-swift.struct/defaultlow.md) or [`defaultHigh`](../nslayoutconstraint/priority-swift.struct/defaulthigh.md).

## Parameters

- `orientation`: The orientation of the dimension of the view that might be reduced.

## See Also

### Measuring in Auto Layout
- [var fittingSize: NSSize](./fittingsize.md)
  The minimum size of the view that satisfies the constraints it holds.
- [var intrinsicContentSize: NSSize](./intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](./invalidateintrinsiccontentsize%28%29.md)
  Invalidates the view’s intrinsic content size.
- [func setContentCompressionResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./setcontentcompressionresistancepriority%28_,for%29.md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](./contenthuggingpriority%28for%29.md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./setcontenthuggingpriority%28_,for%29.md)
  Sets the priority with which a view resists being made larger than its intrinsic size.
- [class let noIntrinsicMetric: CGFloat](./nointrinsicmetric.md)
  A value that tells the layout system to ignore the intrinsic size value for a given dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/contentcompressionresistancepriority(for:))*