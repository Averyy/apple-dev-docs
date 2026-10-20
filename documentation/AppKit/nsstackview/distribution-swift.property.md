# distribution

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The spacing and sizing distribution of stacked views along the primary axis.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var distribution: NSStackView.Distribution { get set }
```

```objc
@property NSStackViewDistribution distribution;
```

#### Discussion

The default value is `gravityAreas`.

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
- [NSStackView.Distribution](./distribution-swift.enum.md)
- [var hasEqualSpacing: Bool](./hasequalspacing.md)
  A Boolean value that indicates whether the spacing between adjacent views should be equal to each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/distribution-swift.property)*