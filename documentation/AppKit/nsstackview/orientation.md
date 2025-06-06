# orientation

**Framework**: AppKit  
**Kind**: property

The horizontal or vertical layout direction of the stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var orientation: NSUserInterfaceLayoutOrientation { get set }
```

#### Discussion

Default value is [`NSUserInterfaceLayoutOrientation.horizontal`](nsuserinterfacelayoutorientation/horizontal.md). For values that apply to this property, see [`NSUserInterfaceLayoutOrientation`](nsuserinterfacelayoutorientation.md).

## See Also

- [enum NSUserInterfaceLayoutOrientation](nsuserinterfacelayoutorientation.md)
  The stack view layout directions, and user interface axes for hugging priority and clipping resistance.
- [var alignment: NSLayoutConstraint.Attribute](nsstackview/alignment.md)
  The view alignment within the stack view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/orientation)*