# measure(in:)

**Framework**: SwiftUI  
**Kind**: method

Measures the size of the resolved text for a given area into which the text should be placed.

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
func measure(in size: CGSize) -> CGSize
```

## Parameters

- `size`: The area to place the   view in.

## See Also

- [func firstBaseline(in: CGSize) -> CGFloat](graphicscontext/resolvedtext/firstbaseline(in:).md)
  Gets the distance from the first line’s ascender to its baseline.
- [func lastBaseline(in: CGSize) -> CGFloat](graphicscontext/resolvedtext/lastbaseline(in:).md)
  Gets the distance from the first line’s ascender to the last line’s baseline.
- [var shading: GraphicsContext.Shading](graphicscontext/resolvedtext/shading.md)
  The shading to fill uncolored text regions with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedtext/measure(in:))*