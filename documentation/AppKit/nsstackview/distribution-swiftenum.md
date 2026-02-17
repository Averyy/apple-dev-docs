# NSStackView.Distribution

**Framework**: AppKit  
**Kind**: enum

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum Distribution
```

## Topics

### Constants
- [NSStackView.Distribution.equalCentering](nsstackview/distribution-swift.enum/equalcentering.md)
  Equal center-to-center spacing of the items is maintained as much as possible while still maintaining the minimum spacing between each view.
- [NSStackView.Distribution.equalSpacing](nsstackview/distribution-swift.enum/equalspacing.md)
  The space separating stacked views along the stacking axis are maintained to be equal as much as possible while still maintaining the minimum spacing.
- [NSStackView.Distribution.fill](nsstackview/distribution-swift.enum/fill.md)
  The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`, causing the stacked views to tightly fill the container along the stacking axis.
- [NSStackView.Distribution.fillEqually](nsstackview/distribution-swift.enum/fillequally.md)
  Stacked views will have sizes maintained to be equal as much as possible along the stacking axis. The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`.
- [NSStackView.Distribution.fillProportionally](nsstackview/distribution-swift.enum/fillproportionally.md)
  Stacked views will have sizes maintained to be equal, proportionally to their `intrinsicContentSize`s, as much as possible. The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`.
- [NSStackView.Distribution.gravityAreas](nsstackview/distribution-swift.enum/gravityareas.md)
  Stacked views will not have any special distribution behavior, relying on behavior described by gravity areas and set hugging priorities along the stacking axis.
### Initializers
- [init?(rawValue: Int)](nsstackview/distribution-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var edgeInsets: NSEdgeInsets](nsstackview/edgeinsets.md)
  The geometric padding, in points, inside the stack view, surrounding its views.
- [var hasEqualSpacing: Bool](nsstackview/hasequalspacing.md)
  A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.
- [var distribution: NSStackView.Distribution](nsstackview/distribution-swift.property.md)
  The spacing and sizing distribution of stacked views along the primary axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/distribution-swift.enum)*