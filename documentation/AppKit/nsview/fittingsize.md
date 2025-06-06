# fittingSize

**Framework**: AppKit  
**Kind**: property

The minimum size of the view that satisfies the constraints it holds.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var fittingSize: NSSize { get }
```

#### Discussion

AppKit sets this property to the best size available for the view, considering all of the constraints it and its subviews hold and satisfying a preference to make the view as small as possible. The size values in this property are never negative.

## See Also

- [var intrinsicContentSize: NSSize](nsview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](nsview/invalidateintrinsiccontentsize.md)
  Invalidates the view’s intrinsic content size.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/fittingsize)*