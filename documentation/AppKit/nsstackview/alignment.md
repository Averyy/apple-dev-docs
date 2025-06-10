# alignment

**Framework**: AppKit  
**Kind**: property

The view alignment within the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var alignment: NSLayoutConstraint.Attribute { get set }
```

#### Discussion

The default value for this property depends on whether the stack view is horizontal or vertical:

- : The default value is [`NSLayoutConstraint.Attribute.centerY`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/centerY).
- : The default value is [`NSLayoutConstraint.Attribute.centerX`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/centerX).

These constants are described as part of the [`NSLayoutConstraint.Attribute`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute) enumeration in [`NSLayoutConstraint`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint); see that enumeration for the other possible alignment values.

> **Note**:  Using certain values in this property can result in unexpected behavior: - Specifying the [`NSLayoutConstraint.Attribute.notAnAttribute`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/notAnAttribute) constant can result in an ambiguous layout.
- A value inappropriate for the layout direction is ignored; for example, the system ignores a value of [`NSLayoutConstraint.Attribute.centerX`](https://developer.apple.com/documentation/UIKit/NSLayoutConstraint/Attribute/centerX) for the horizontal layout.

## See Also

- [var orientation: NSUserInterfaceLayoutOrientation](nsstackview/orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [enum NSUserInterfaceLayoutOrientation](nsuserinterfacelayoutorientation.md)
  The stack view layout directions, and user interface axes for hugging priority and clipping resistance.
- [var spacing: CGFloat](nsstackview/spacing.md)
  The minimum spacing, in points, between adjacent views in the stack view.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)
- [var edgeInsets: NSEdgeInsets](nsstackview/edgeinsets.md)
  The geometric padding, in points, inside the stack view, surrounding its views.
- [var hasEqualSpacing: Bool](nsstackview/hasequalspacing.md)
  A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.
- [var distribution: NSStackView.Distribution](nsstackview/distribution-swift.property.md)
- [NSStackView.Distribution](nsstackview/distribution-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/alignment)*