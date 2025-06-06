# noIntrinsicMetric

**Framework**: AppKit  
**Kind**: property

A value that tells the layout system to ignore the intrinsic size value for a given dimension.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class let noIntrinsicMetric: CGFloat
```

#### Discussion

Specify this value if a view doesn’t have an intrinsic height or width. For example, a horizontal slider has an intrinsic height but might have no intrinsic width.

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
- [func contentHuggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](nsview/contenthuggingpriority(for:).md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsview/setcontenthuggingpriority(_:for:).md)
  Sets the priority with which a view resists being made larger than its intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/nointrinsicmetric)*