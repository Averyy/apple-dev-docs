# multicolor

**Framework**: SwiftUI  
**Kind**: property

A mode that renders symbols as multiple layers with their inherit styles.

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
static let multicolor: SymbolRenderingMode
```

#### Discussion

The layers may be filled with their own inherent styles, or the foreground style. For example, you can render a filled exclamation mark triangle in its inherent colors, with yellow for the triangle and white for the exclamation mark:

```swift
Image(systemName: "exclamationmark.triangle.fill")
    .symbolRenderingMode(.multicolor)
```

## See Also

- [static let hierarchical: SymbolRenderingMode](symbolrenderingmode/hierarchical.md)
  A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.
- [static let monochrome: SymbolRenderingMode](symbolrenderingmode/monochrome.md)
  A mode that renders symbols as a single layer filled with the foreground style.
- [static let palette: SymbolRenderingMode](symbolrenderingmode/palette.md)
  A mode that renders symbols as multiple layers, with different styles applied to the layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolrenderingmode/multicolor)*