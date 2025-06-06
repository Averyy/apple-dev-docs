# resolve(_:)

**Framework**: SwiftUI  
**Kind**: method

Gets a version of an image that’s fixed with the current values of the graphics context’s environment.

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
func resolve(_ image: Image) -> GraphicsContext.ResolvedImage
```

#### Return Value

An image that’s resolved into the current context’s environment, taking into account environment values like the display resolution and current color scheme.

#### Discussion

You can measure the resolved image by looking at its [`size`](graphicscontext/resolvedimage/size.md) and [`baseline`](graphicscontext/resolvedimage/baseline.md) properties. You can draw the resolved image with the context’s [`draw(_:in:style:)`](graphicscontext/draw(_:in:style:)-7rvee.md) or [`draw(_:at:anchor:)`](graphicscontext/draw(_:at:anchor:)-1z5wt.md) method.

## Parameters

- `image`: The   to resolve.

## See Also

- [func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?](graphicscontext/resolvesymbol(id:).md)
  Gets the identified child view as a resolved symbol, if the view exists.
- [GraphicsContext.ResolvedSymbol](graphicscontext/resolvedsymbol.md)
  A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.
- [GraphicsContext.ResolvedImage](graphicscontext/resolvedimage.md)
  An image resolved to a particular environment.
- [GraphicsContext.ResolvedText](graphicscontext/resolvedtext.md)
  A text view resolved to a particular environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolve(_:))*