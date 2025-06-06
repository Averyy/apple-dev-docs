# ColorRenderingMode

**Framework**: SwiftUI  
**Kind**: enum

The set of possible working color spaces for color-compositing operations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum ColorRenderingMode
```

#### Overview

Each color space guarantees the preservation of a particular range of color values.

## Topics

### Getting rendering modes
- [ColorRenderingMode.extendedLinear](colorrenderingmode/extendedlinear.md)
  The extended linear sRGB working color space.
- [ColorRenderingMode.linear](colorrenderingmode/linear.md)
  The linear sRGB working color space.
- [ColorRenderingMode.nonLinear](colorrenderingmode/nonlinear.md)
  The non-linear sRGB working color space.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func blendMode(BlendMode) -> some View](view/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](view/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](view/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [enum BlendMode](blendmode.md)
  Modes for compositing a view with overlapping content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/colorrenderingmode)*