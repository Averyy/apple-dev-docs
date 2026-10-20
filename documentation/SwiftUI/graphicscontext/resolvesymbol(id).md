# resolveSymbol(id:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Gets the identified child view as a resolved symbol, if the view exists.

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
func resolveSymbol<ID>(id: ID) -> GraphicsContext.ResolvedSymbol? where ID : Hashable
```

#### Return Value

The resolved symbol, or `nil` if SwiftUI can’t find a child view with the given `id`.

## Parameters

- `id`: The value that you used to tag the view when you define it in the `symbols` parameter of the [`Canvas`](../canvas.md) initializer [`init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)`](../canvas/init%28opaque,colormode,rendersasynchronously,renderer,symbols%29.md).

## See Also

### Resolving a drawn entity
- [func resolve(_:)](./resolve%28_%29.md)
  Gets a version of an image that’s fixed with the current values of the graphics context’s environment.
- [GraphicsContext.ResolvedSymbol](./resolvedsymbol.md)
  A static sequence of drawing operations that may be drawn multiple times, preserving their resolution independence.
- [GraphicsContext.ResolvedImage](./resolvedimage.md)
  An image resolved to a particular environment.
- [GraphicsContext.ResolvedText](./resolvedtext.md)
  A text view resolved to a particular environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/resolvesymbol(id:))*