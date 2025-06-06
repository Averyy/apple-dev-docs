# monochrome

**Framework**: SwiftUI  
**Kind**: property

A mode that renders symbols as a single layer filled with the foreground style.

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
static let monochrome: SymbolRenderingMode
```

#### Discussion

For example, you can render a filled exclamation mark triangle in purple:

```swift
Image(systemName: "exclamationmark.triangle.fill")
    .symbolRenderingMode(.monochrome)
    .foregroundStyle(Color.purple)
```

## See Also

- [static let hierarchical: SymbolRenderingMode](symbolrenderingmode/hierarchical.md)
  A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.
- [static let multicolor: SymbolRenderingMode](symbolrenderingmode/multicolor.md)
  A mode that renders symbols as multiple layers with their inherit styles.
- [static let palette: SymbolRenderingMode](symbolrenderingmode/palette.md)
  A mode that renders symbols as multiple layers, with different styles applied to the layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolrenderingmode/monochrome)*