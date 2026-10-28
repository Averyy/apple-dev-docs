# hasEqualSpacing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.

**Availability**:
- macOS 10.9+ - Deprecated in 10.11

> **Deprecated**: Set [`distribution`](./distribution-swift.property.md) to [`NSStackView.Distribution.equalSpacing`](./distribution-swift.enum/equalspacing.md) instead.

## Declaration

```swift
var hasEqualSpacing: Bool { get set }
```

```objc
@property BOOL hasEqualSpacing;
```

## Discussion

The distances between adjacent views in a stack view are either constrained to equal each other or settable to custom spacings using the [`setCustomSpacing(_:after:)`](./setcustomspacing%28_,after%29.md) method. The default value for the [`hasEqualSpacing`](./hasequalspacing.md) property is [`false`](../../Swift/false.md), which enables custom spacing. To require equal spacing, set this property to [`true`](../../Swift/true.md), which disables the [`setCustomSpacing(_:after:)`](./setcustomspacing%28_,after%29.md) method.

With [`hasEqualSpacing`](./hasequalspacing.md) set to [`false`](../../Swift/false.md) (the default), the Auto Layout constraints for spacing between views in a gravity area are as shown in the table of the [`spacing`](./spacing.md) property.

If you specify equal spacing, the system changes these constraints to the values shown in the table below.

| Constraint | Value for constraint priority |
| --- | --- |
| inter-view spacing `==` the [`spacing`](./spacing.md) property | hugging priority |
| inter-view spacing `≥` the [`spacing`](./spacing.md) property | NSLayoutPriorityRequired |
| Equal inter-view spacing | NSLayoutPriorityDefaultLow |

Stack view hugging priority, identified as the constraint value in row 1, has the default value [`defaultLow`](../nslayoutconstraint/priority-swift.struct/defaultlow.md). You can adjust hugging priority by using the [`setHuggingPriority(_:for:)`](./sethuggingpriority%28_,for%29.md) method.

## See Also

### Related Documentation
- [func setHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./sethuggingpriority%28_,for%29.md)
  Sets the Auto Layout priority for the stack view to minimize its size, for a specified user interface axis.
### Configuring the Stack View Layout
- [var orientation: NSUserInterfaceLayoutOrientation](./orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [enum NSUserInterfaceLayoutOrientation](../nsuserinterfacelayoutorientation.md)
  The stack view layout directions, and user interface axes for hugging priority and clipping resistance.
- [var alignment: NSLayoutConstraint.Attribute](./alignment.md)
  The view alignment within the stack view.
- [var spacing: CGFloat](./spacing.md)
  The minimum spacing, in points, between adjacent views in the stack view.
- [class let useDefaultSpacing: CGFloat](./usedefaultspacing.md)
- [var edgeInsets: NSEdgeInsets](./edgeinsets.md)
  The geometric padding, in points, inside the stack view, surrounding its views.
- [var distribution: NSStackView.Distribution](./distribution-swift.property.md)
  The spacing and sizing distribution of stacked views along the primary axis.
- [NSStackView.Distribution](./distribution-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/hasequalspacing)*