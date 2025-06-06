# shading

**Framework**: SwiftUI  
**Kind**: property

The shading to fill uncolored text regions with.

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
var shading: GraphicsContext.Shading
```

#### Discussion

This value defaults to the [`foreground`](graphicscontext/shading/foreground.md) shading.

## See Also

- [func firstBaseline(in: CGSize) -> CGFloat](graphicscontext/resolvedtext/firstbaseline(in:).md)
  Gets the distance from the first line’s ascender to its baseline.
- [func lastBaseline(in: CGSize) -> CGFloat](graphicscontext/resolvedtext/lastbaseline(in:).md)
  Gets the distance from the first line’s ascender to the last line’s baseline.
- [func measure(in: CGSize) -> CGSize](graphicscontext/resolvedtext/measure(in:).md)
  Measures the size of the resolved text for a given area into which the text should be placed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedtext/shading)*