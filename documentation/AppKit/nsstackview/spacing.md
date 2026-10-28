# spacing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum spacing, in points, between adjacent views in the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var spacing: CGFloat { get set }
```

```objc
@property CGFloat spacing;
```

## Discussion

A stack view uses this property to define the minimum distance between views within a gravity area and between neighboring views in adjacent gravity areas. The default value for the [`spacing`](./spacing.md) property is `8.0` points.

The automatically applied Auto Layout constraints for [`spacing`](./spacing.md) are shown in the table below.

| Constraint | Value for constraint priority |
| --- | --- |
| inter-view spacing `==` the [`spacing`](./spacing.md) property value | max (NSLayoutPriorityDefaultHigh, hugging priority) |
| inter-gravity-area spacing `==` the [`spacing`](./spacing.md) property value | hugging priority |
| inter-view spacing `≥` the [`spacing`](./spacing.md) property value | NSLayoutPriorityRequired |

The first row indicates that inter-view spacing is constrained to equal the value of the [`spacing`](./spacing.md) property with a priority of at least [`defaultHigh`](../nslayoutconstraint/priority-swift.struct/defaulthigh.md); you can increase this by setting a higher stack view hugging priority with the [`setHuggingPriority(_:for:)`](./sethuggingpriority%28_,for%29.md) method.

The second row indicates that the spacing between adjacent views in neighboring gravity areas is constrained to equal the value of the [`spacing`](./spacing.md) property with the priority of the stack view’s hugging priority.

The third row indicates that inter-view spacing is allowed to grow larger than the value of the [`spacing`](./spacing.md) property with a priority of NSLayoutPriorityRequired.

In combination, these constraints result in the following typical stack view behavior: In a stack view whose [`hasEqualSpacing`](./hasequalspacing.md) property is set to [`false`](../../Swift/false.md) (the default) and whose hugging priority is left at [`defaultLow`](../nslayoutconstraint/priority-swift.struct/defaultlow.md) (the default), views within a gravity area remain a fixed distance from each other (equal to the value of the [`spacing`](./spacing.md) property), and the distance between gravity areas grows and shrinks as the stack view grows and shrinks along its layout direction axis. If you set the [`hasEqualSpacing`](./hasequalspacing.md) property to [`true`](../../Swift/true.md) and use the default hugging priority, then the distance between all adjacent views, including adjacent views in neighboring gravity areas, grows and shrinks as the stack view grows and shrinks.

## See Also

### Configuring the Stack View Layout
- [var orientation: NSUserInterfaceLayoutOrientation](./orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [enum NSUserInterfaceLayoutOrientation](../nsuserinterfacelayoutorientation.md)
  The stack view layout directions, and user interface axes for hugging priority and clipping resistance.
- [var alignment: NSLayoutConstraint.Attribute](./alignment.md)
  The view alignment within the stack view.
- [class let useDefaultSpacing: CGFloat](./usedefaultspacing.md)
- [var edgeInsets: NSEdgeInsets](./edgeinsets.md)
  The geometric padding, in points, inside the stack view, surrounding its views.
- [var distribution: NSStackView.Distribution](./distribution-swift.property.md)
  The spacing and sizing distribution of stacked views along the primary axis.
- [NSStackView.Distribution](./distribution-swift.enum.md)
- [var hasEqualSpacing: Bool](./hasequalspacing.md)
  A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/spacing)*