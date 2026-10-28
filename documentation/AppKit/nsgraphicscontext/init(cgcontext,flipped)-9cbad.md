# init(cgContext:flipped:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new graphics context from the specified Core Graphics context and the initial flipped state.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(cgContext graphicsPort: CGContext, flipped initialFlippedState: Bool)
```

```objc
+ (NSGraphicsContext *) graphicsContextWithCGContext:(CGContextRef) graphicsPort flipped:(BOOL) initialFlippedState;
```

## Return Value

The created [`NSGraphicsContext`](../nsgraphicscontext.md) object, or `nil` if the object could not be created.

## Parameters

- `graphicsPort`: The graphics port used to create the graphics-context object, as a [`CGContext`](../../CoreGraphics/cgcontext.md) (opaque type) object.
- `initialFlippedState`: Specifies the receiver’s initial flipped state. This is the value returned by [`isFlipped`](./isflipped.md) when no view has focus.

## See Also

### Creating a Graphics Context
- [init?(attributes: [NSGraphicsContext.AttributeKey : Any])](./init%28attributes%29.md)
  Creates a graphics context using the specified attributes.
- [init?(bitmapImageRep: NSBitmapImageRep)](./init%28bitmapimagerep%29.md)
  Creates a new graphics context using the specified bitmap image representation object as the context destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(cgcontext:flipped:)-9cbad)*