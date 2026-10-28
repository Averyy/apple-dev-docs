# intrinsicContentSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The natural size for the receiving view, considering only properties of the view itself.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var intrinsicContentSize: NSSize { get }
```

```objc
@property (readonly) NSSize intrinsicContentSize;
```

## Return Value

A size indicating the natural size for the receiving view based on its intrinsic properties.

## Discussion

The default width and height values of this property are set to [`noIntrinsicMetric`](./nointrinsicmetric.md). For a custom view, you can override this property and use it to communicate what size you would like your view to be based on its content. You might do this in cases where the layout system cannot determine the size of the view based solely on its current constraints. For example, a text field might override this method and return an intrinsic size based on the text it contains. The intrinsic size you supply must be independent of the content frame, because there’s no way to dynamically communicate a changed width to the layout system based on a changed height. If your custom view has no intrinsic size for a given dimension, you can set the corresponding dimension to the [`noIntrinsicMetric`](./nointrinsicmetric.md).

## See Also

### Measuring in Auto Layout
- [var fittingSize: NSSize](./fittingsize.md)
  The minimum size of the view that satisfies the constraints it holds.
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
- [class let noIntrinsicMetric: CGFloat](./nointrinsicmetric.md)
  A value that tells the layout system to ignore the intrinsic size value for a given dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/intrinsiccontentsize)*