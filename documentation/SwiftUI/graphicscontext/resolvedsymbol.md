# GraphicsContext.ResolvedSymbol

**Framework**: SwiftUI  
**Kind**: struct

A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.

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
struct ResolvedSymbol
```

#### Overview

You resolve a child view in preparation for drawing it into a context by calling [`resolveSymbol(id:)`](graphicscontext/resolvesymbol(id:).md). The resolved view takes into account environment values like the display resolution and current color scheme.

## Topics

### Getting the symbol properties
- [var size: CGSize](graphicscontext/resolvedsymbol/size.md)
  The dimensions of the resolved symbol.

## See Also

- [func resolve(_:)](graphicscontext/resolve(_:).md)
  Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?](graphicscontext/resolvesymbol(id:).md)
  Gets the identified child view as a resolved symbol, if the view exists.
- [GraphicsContext.ResolvedImage](graphicscontext/resolvedimage.md)
  An image resolved to a particular environment.
- [GraphicsContext.ResolvedText](graphicscontext/resolvedtext.md)
  A text view resolved to a particular environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedsymbol)*