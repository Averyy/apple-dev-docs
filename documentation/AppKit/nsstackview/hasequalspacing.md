# hasEqualSpacing

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var hasEqualSpacing: Bool { get set }
```

#### Discussion

The distances between adjacent views in a stack view are either constrained to equal each other or settable to custom spacings using the [`setCustomSpacing(_:after:)`](nsstackview/setcustomspacing(_:after:).md) method. The default value for the [`hasEqualSpacing`](nsstackview/hasequalspacing.md) property is [`false`](https://developer.apple.com/documentation/swift/false), which enables custom spacing. To require equal spacing, set this property to [`true`](https://developer.apple.com/documentation/swift/true), which disables the [`setCustomSpacing(_:after:)`](nsstackview/setcustomspacing(_:after:).md) method.

With [`hasEqualSpacing`](nsstackview/hasequalspacing.md) set to [`false`](https://developer.apple.com/documentation/swift/false) (the default), the Auto Layout constraints for spacing between views in a gravity area are as shown in the table of the [`spacing`](nsstackview/spacing.md) property.

If you specify equal spacing, the system changes these constraints to the values shown in the table below.

| Constraint | Value for constraint priority |
| --- | --- |
| inter-view spacing `==` the [`spacing`](nsstackview/spacing.md) property | hugging priority |
| inter-view spacing `≥` the [`spacing`](nsstackview/spacing.md) property | NSLayoutPriorityRequired |
| Equal inter-view spacing | NSLayoutPriorityDefaultLow |

Stack view hugging priority, identified as the constraint value in row 1, has the default value [`defaultLow`](nslayoutconstraint/priority-swift.struct/defaultlow.md). You can adjust hugging priority by using the [`setHuggingPriority(_:for:)`](nsstackview/sethuggingpriority(_:for:).md) method.

## See Also

- [func setHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/sethuggingpriority(_:for:).md)
  Sets the Auto Layout priority for the stack view to minimize its size, for a specified user interface axis.
- [var orientation: NSUserInterfaceLayoutOrientation](nsstackview/orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [enum NSUserInterfaceLayoutOrientation](nsuserinterfacelayoutorientation.md)
  The stack view layout directions, and user interface axes for hugging priority and clipping resistance.
- [var alignment: NSLayoutConstraint.Attribute](nsstackview/alignment.md)
  The view alignment within the stack view.
- [var spacing: CGFloat](nsstackview/spacing.md)
  The minimum spacing, in points, between adjacent views in the stack view.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)
- [var edgeInsets: NSEdgeInsets](nsstackview/edgeinsets.md)
  The geometric padding, in points, inside the stack view, surrounding its views.
- [var distribution: NSStackView.Distribution](nsstackview/distribution-swift.property.md)
- [NSStackView.Distribution](nsstackview/distribution-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/hasequalspacing)*