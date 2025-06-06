# sizeThatFits(_:)

**Framework**: SwiftUI  
**Kind**: method

Asks the subview for its size.

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
func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize
```

#### Return Value

The size that the subview chooses for itself, given the proposal from its container view.

#### Discussion

Use this method as a convenience to get the [`width`](viewdimensions/width.md) and [`height`](viewdimensions/height.md) properties of the [`ViewDimensions`](viewdimensions.md) instance returned by the [`dimensions(in:)`](layoutsubview/dimensions(in:).md) method, reported as a [`CGSize`](https://developer.apple.com/documentation/CoreFoundation/CGSize) instance.

## Parameters

- `proposal`: A proposed size for the subview. In SwiftUI,   views choose their own size, but can take a size proposal from   their parent view into account when doing so.

## See Also

- [func dimensions(in: ProposedViewSize) -> ViewDimensions](layoutsubview/dimensions(in:).md)
  Asks the subview for its dimensions and alignment guides.
- [var spacing: ViewSpacing](layoutsubview/spacing.md)
  The subviews’s preferred spacing values.
- [var priority: Double](layoutsubview/priority.md)
  The layout priority of the subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubview/sizethatfits(_:))*