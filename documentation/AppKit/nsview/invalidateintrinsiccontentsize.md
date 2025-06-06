# invalidateIntrinsicContentSize()

**Framework**: AppKit  
**Kind**: method

Invalidates the view’s intrinsic content size.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func invalidateIntrinsicContentSize()
```

#### Discussion

Call this when something changes in your custom view that invalidates its intrinsic content size. This allows the constraint-based layout system to take the new intrinsic content size into account in its next layout pass.

## See Also

- [var fittingSize: NSSize](nsview/fittingsize.md)
  The minimum size of the view that satisfies the constraints it holds.
- [var intrinsicContentSize: NSSize](nsview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsview/contentcompressionresistancepriority(for:).md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsview/setcontentcompressionresistancepriority(_:for:).md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsview/contenthuggingpriority(for:).md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsview/setcontenthuggingpriority(_:for:).md)
  Sets the priority with which a view resists being made larger than its intrinsic size.
- [class let noIntrinsicMetric: CGFloat](nsview/nointrinsicmetric.md)
  A value that tells the layout system to ignore the intrinsic size value for a given dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidateintrinsiccontentsize())*