# GraphicsContext.ResolvedText

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A text view resolved to a particular environment.

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
struct ResolvedText
```

#### Overview

You resolve a [`Text`](../text.md) view in preparation for drawing it into a context, either manually by calling [`resolve(_:)`](./resolve%28_%29-4dx65.md) or automatically when calling [`draw(_:in:)`](./draw%28_,in%29-5opqf.md) or [`draw(_:at:anchor:)`](./draw%28_,at,anchor%29-5dgmd.md). The resolved text view takes into account environment values like the display resolution and current color scheme.

## Topics

### Getting the text properties
- [func firstBaseline(in: CGSize) -> CGFloat](./resolvedtext/firstbaseline%28in%29.md)
  Gets the distance from the first line’s ascender to its baseline.
- [func lastBaseline(in: CGSize) -> CGFloat](./resolvedtext/lastbaseline%28in%29.md)
  Gets the distance from the first line’s ascender to the last line’s baseline.
- [func measure(in: CGSize) -> CGSize](./resolvedtext/measure%28in%29.md)
  Measures the size of the resolved text for a given area into which the text should be placed.
- [var shading: GraphicsContext.Shading](./resolvedtext/shading.md)
  The shading to fill uncolored text regions with.

## See Also

### Resolving a drawn entity
- [func resolve(_:)](./resolve%28_%29.md)
  Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?](./resolvesymbol%28id%29.md)
  Gets the identified child view as a resolved symbol, if the view exists.
- [GraphicsContext.ResolvedSymbol](./resolvedsymbol.md)
  A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.
- [GraphicsContext.ResolvedImage](./resolvedimage.md)
  An image resolved to a particular environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedtext)*