# NSStackView.Distribution

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum Distribution
```

```c
enum NSStackViewDistribution : NSInteger;
```

## Topics

### Constants
- [NSStackView.Distribution.equalCentering](./distribution-swift.enum/equalcentering.md)
  Equal center-to-center spacing of the items is maintained as much as possible while still maintaining the minimum spacing between each view.
- [NSStackView.Distribution.equalSpacing](./distribution-swift.enum/equalspacing.md)
  The space separating stacked views along the stacking axis are maintained to be equal as much as possible while still maintaining the minimum spacing.
- [NSStackView.Distribution.fill](./distribution-swift.enum/fill.md)
  The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`, causing the stacked views to tightly fill the container along the stacking axis.
- [NSStackView.Distribution.fillEqually](./distribution-swift.enum/fillequally.md)
  Stacked views will have sizes maintained to be equal as much as possible along the stacking axis. The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`.
- [NSStackView.Distribution.fillProportionally](./distribution-swift.enum/fillproportionally.md)
  Stacked views will have sizes maintained to be equal, proportionally to their `intrinsicContentSize`s, as much as possible. The effective hugging priority in the stacking axis is `NSLayoutPriorityRequired`.
- [NSStackView.Distribution.gravityAreas](./distribution-swift.enum/gravityareas.md)
  Stacked views will not have any special distribution behavior, relying on behavior described by gravity areas and set hugging priorities along the stacking axis.
### Initializers
- [init?(rawValue: Int)](./distribution-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

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
- [var hasEqualSpacing: Bool](./hasequalspacing.md)
  A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/distribution-swift.enum)*