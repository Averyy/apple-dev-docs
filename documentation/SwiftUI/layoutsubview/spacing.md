# spacing

**Framework**: SwiftUI  
**Kind**: property

The subviews’s preferred spacing values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var spacing: ViewSpacing { get }
```

#### Discussion

This [`ViewSpacing`](viewspacing.md) instance indicates how much space a subview in a custom layout prefers to have between it and the next view. It contains preferences for all edges, and might take into account the type of both this and the adjacent view. If your [`Layout`](layout.md) type places subviews based on spacing preferences, use this instance to compute a distance between this subview and the next. See [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) for an example.

You can also merge this instance with instances from other subviews to construct a new instance that’s suitable for the subviews’ container. See [`spacing(subviews:cache:)`](layout/spacing(subviews:cache:).md).

## See Also

- [func dimensions(in: ProposedViewSize) -> ViewDimensions](layoutsubview/dimensions(in:).md)
  Asks the subview for its dimensions and alignment guides.
- [func sizeThatFits(ProposedViewSize) -> CGSize](layoutsubview/sizethatfits(_:).md)
  Asks the subview for its size.
- [var priority: Double](layoutsubview/priority.md)
  The layout priority of the subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubview/spacing)*