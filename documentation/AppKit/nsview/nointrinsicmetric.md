# noIntrinsicMetric

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A value that tells the layout system to ignore the intrinsic size value for a given dimension.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class let noIntrinsicMetric: CGFloat
```

```c
extern const CGFloat NSViewNoIntrinsicMetric;
```

#### Discussion

Specify this value if a view doesn’t have an intrinsic height or width. For example, a horizontal slider has an intrinsic height but might have no intrinsic width.

## See Also

### Measuring in Auto Layout
- [var fittingSize: NSSize](./fittingsize.md)
  The minimum size of the view that satisfies the constraints it holds.
- [var intrinsicContentSize: NSSize](./intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [func invalidateIntrinsicContentSize()](./invalidateintrinsiccontentsize%28%29.md)
  Invalidates the view’s intrinsic content size.
- [func contentCompressionResistancePriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](./contentcompressionresistancepriority%28for%29.md)
  Returns the priority with which a view resists being made smaller than its intrinsic size.
- [func setContentCompressionResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./setcontentcompressionresistancepriority%28_,for%29.md)
  Sets the priority with which a view resists being made smaller than its intrinsic size.
- [func contentHuggingPriority(for: NSLayoutConstraint.Orientation) -> NSLayoutConstraint.Priority](./contenthuggingpriority%28for%29.md)
  Returns the priority with which a view resists being made larger than its intrinsic size.
- [func setContentHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./setcontenthuggingpriority%28_,for%29.md)
  Sets the priority with which a view resists being made larger than its intrinsic size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/nointrinsicmetric)*