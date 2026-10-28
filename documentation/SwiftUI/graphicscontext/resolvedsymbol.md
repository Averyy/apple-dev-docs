# GraphicsContext.ResolvedSymbol

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

You resolve a child view in preparation for drawing it into a context by calling [`resolveSymbol(id:)`](./resolvesymbol%28id%29.md). The resolved view takes into account environment values like the display resolution and current color scheme.

## Topics

### Getting the symbol properties
- [var size: CGSize](./resolvedsymbol/size.md)
  The dimensions of the resolved symbol.

## See Also

### Resolving a drawn entity
- [func resolve(_:)](./resolve%28_%29.md)
  Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?](./resolvesymbol%28id%29.md)
  Gets the identified child view as a resolved symbol, if the view exists.
- [GraphicsContext.ResolvedImage](./resolvedimage.md)
  An image resolved to a particular environment.
- [GraphicsContext.ResolvedText](./resolvedtext.md)
  A text view resolved to a particular environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedsymbol)*