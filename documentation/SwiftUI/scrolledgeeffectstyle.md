# ScrollEdgeEffectStyle

**Framework**: SwiftUI  
**Kind**: struct

A structure that defines the style of pocket a scroll view will have.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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
  A soft-edged scroll edge effect.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](view/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollEdgeEffectDisabled(Bool, for: Edge.Set) -> some View](view/scrolledgeeffectdisabled(_:for:).md)
  Disables any scroll edge effects for scroll views within this hierarchy.
- [func safeAreaBar(edge:alignment:spacing:content:)](view/safeareabar(edge:alignment:spacing:content:).md)
  Renders the provided content appropriately to be displayed as a custom bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle)*