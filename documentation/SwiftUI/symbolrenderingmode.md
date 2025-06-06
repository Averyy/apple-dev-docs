# SymbolRenderingMode

**Framework**: SwiftUI  
**Kind**: struct

A symbol rendering mode.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SymbolRenderingMode
```

## Topics

### Getting symbol rendering modes
- [static let hierarchical: SymbolRenderingMode](symbolrenderingmode/hierarchical.md)
  A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.
- [static let monochrome: SymbolRenderingMode](symbolrenderingmode/monochrome.md)
  A mode that renders symbols as a single layer filled with the foreground style.
- [static let multicolor: SymbolRenderingMode](symbolrenderingmode/multicolor.md)
  A mode that renders symbols as multiple layers with their inherit styles.
- [static let palette: SymbolRenderingMode](symbolrenderingmode/palette.md)
  A mode that renders symbols as multiple layers, with different styles applied to the layers.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](view/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [var symbolRenderingMode: SymbolRenderingMode?](environmentvalues/symbolrenderingmode.md)
  The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolrenderingmode)*