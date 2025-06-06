# edgeInsets

**Framework**: AppKit  
**Kind**: property

The geometric padding, in points, inside the stack view, surrounding its views.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var edgeInsets: NSEdgeInsets { get set }
```

#### Discussion

The default value is `(0, 0, 0, 0)`. Edge insets remain as they are if you change the value of a stack view’s [`orientation`](nsstackview/orientation.md) property or the value of its inherited [`userInterfaceLayoutDirection`](nsview/userinterfacelayoutdirection.md) property.

## See Also

- [var orientation: NSUserInterfaceLayoutOrientation](nsstackview/orientation.md)
  The horizontal or vertical layout direction of the stack view.
- [enum NSUserInterfaceLayoutOrientation](nsuserinterfacelayoutorientation.md)
  The stack view layout directions, and user interface axes for hugging priority and clipping resistance.
- [var alignment: NSLayoutConstraint.Attribute](nsstackview/alignment.md)
  The view alignment within the stack view.
- [var spacing: CGFloat](nsstackview/spacing.md)
  The minimum spacing, in points, between adjacent views in the stack view.
- [class let useDefaultSpacing: CGFloat](nsstackview/usedefaultspacing.md)
- [var hasEqualSpacing: Bool](nsstackview/hasequalspacing.md)
  A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.
- [var distribution: NSStackView.Distribution](nsstackview/distribution-swift.property.md)
- [NSStackView.Distribution](nsstackview/distribution-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/edgeinsets)*