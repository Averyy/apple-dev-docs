# NSUserInterfaceLayoutOrientation

**Framework**: AppKit  
**Kind**: enum

The stack view layout directions, and user interface axes for hugging priority and clipping resistance.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum NSUserInterfaceLayoutOrientation
```

## Topics

### Constants
- [NSUserInterfaceLayoutOrientation.horizontal](nsuserinterfacelayoutorientation/horizontal.md)
  The horizontal orientation.
- [NSUserInterfaceLayoutOrientation.vertical](nsuserinterfacelayoutorientation/vertical.md)
  The vertical orientation.
### Initializers
- [init?(rawValue: Int)](nsuserinterfacelayoutorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var orientation: NSUserInterfaceLayoutOrientation](nsstackview/orientation.md)
  The horizontal or vertical layout direction of the stack view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacelayoutorientation)*