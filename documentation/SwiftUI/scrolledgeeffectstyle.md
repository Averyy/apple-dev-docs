# ScrollEdgeEffectStyle

**Framework**: SwiftUI  
**Kind**: struct

A structure that defines the style of pocket a scroll view will have.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ScrollEdgeEffectStyle
```

## Topics

### Type Properties
- [static var automatic: ScrollEdgeEffectStyle](scrolledgeeffectstyle/automatic.md)
  The automatic scroll pocket style.
- [static var hard: ScrollEdgeEffectStyle](scrolledgeeffectstyle/hard.md)
  A scroll edge effect with a hard cutoff and dividing line.
- [static var soft: ScrollEdgeEffectStyle](scrolledgeeffectstyle/soft.md)
  A scroll edge effect with a soft edge.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](view/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollEdgeEffectHidden(Bool, for: Edge.Set) -> some View](view/scrolledgeeffecthidden(_:for:).md)
  Hides any scroll edge effects for scroll views within this hierarchy.
- [func safeAreaBar(edge:alignment:spacing:content:)](view/safeareabar(edge:alignment:spacing:content:).md)
  Shows the specified content as a custom bar beside the modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle)*