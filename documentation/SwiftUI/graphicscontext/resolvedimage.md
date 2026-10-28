# GraphicsContext.ResolvedImage

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An image resolved to a particular environment.

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
struct ResolvedImage
```

## Overview

You resolve an [`Image`](../image.md) in preparation for drawing it into a context, either manually by calling [`resolve(_:)`](./resolve%28_%29-898z6.md), or automatically when calling [`draw(_:in:style:)`](./draw%28_,in,style%29-blhz.md) or [`draw(_:at:anchor:)`](./draw%28_,at,anchor%29-1z5wt.md). The resolved image takes into account environment values like the display resolution and current color scheme.

## Topics

### Getting the image properties
- [var size: CGSize](./resolvedimage/size.md)
  The size of the image.
- [let baseline: CGFloat](./resolvedimage/baseline.md)
  The distance from the top of the image to its baseline.
- [var shading: GraphicsContext.Shading?](./resolvedimage/shading.md)
  An optional shading to fill the image with.

## See Also

### Resolving a drawn entity
- [func resolve(_:)](./resolve%28_%29.md)
  Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol?](./resolvesymbol%28id%29.md)
  Gets the identified child view as a resolved symbol, if the view exists.
- [GraphicsContext.ResolvedSymbol](./resolvedsymbol.md)
  A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.
- [GraphicsContext.ResolvedText](./resolvedtext.md)
  A text view resolved to a particular environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvedimage)*