# alignment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view alignment within the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var alignment: NSLayoutConstraint.Attribute { get set }
```

```objc
@property NSLayoutAttribute alignment;
```

## Discussion

The default value for this property depends on whether the stack view is horizontal or vertical:

- *Horizontal*: The default value is [`NSLayoutConstraint.Attribute.centerY`](../../UIKit/nslayoutconstraint/attribute/centery.md).
- *Vertical*: The default value is [`NSLayoutConstraint.Attribute.centerX`](../../UIKit/nslayoutconstraint/attribute/centerx.md).

These constants are described as part of the [`NSLayoutConstraint.Attribute`](../../UIKit/nslayoutconstraint/attribute.md) enumeration in [`NSLayoutConstraint`](../../UIKit/nslayoutconstraint.md); see that enumeration for the other possible alignment values.

> **Note**:  Using certain values in this property can result in unexpected behavior:
>
> - Specifying the [`NSLayoutConstraint.Attribute.notAnAttribute`](../../UIKit/nslayoutconstraint/attribute/notanattribute.md) constant can result in an ambiguous layout.
> - A value inappropriate for the layout direction is ignored; for example, the system ignores a value of [`NSLayoutConstraint.Attribute.centerX`](../../UIKit/nslayoutconstraint/attribute/centerx.md) for the horizontal layout.

## See Also

### Configuring the Stack View Layout
- [var orientation: NSUserInterfaceLayoutOrientation](./orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [enum NSUserInterfaceLayoutOrientation](../nsuserinterfacelayoutorientation.md)
  The stack view layout directions, and user interface axes for hugging priority and clipping resistance.
- [var spacing: CGFloat](./spacing.md)
  The minimum spacing, in points, between adjacent views in the stack view.
- [class let useDefaultSpacing: CGFloat](./usedefaultspacing.md)
- [var edgeInsets: NSEdgeInsets](./edgeinsets.md)
  The geometric padding, in points, inside the stack view, surrounding its views.
- [var distribution: NSStackView.Distribution](./distribution-swift.property.md)
  The spacing and sizing distribution of stacked views along the primary axis.
- [NSStackView.Distribution](./distribution-swift.enum.md)
- [var hasEqualSpacing: Bool](./hasequalspacing.md)
  A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/alignment)*