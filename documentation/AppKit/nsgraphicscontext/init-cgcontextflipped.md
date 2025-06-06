# init(cgContext:flipped:)

**Framework**: AppKit  
**Kind**: init

Creates a new graphics context from the specified Core Graphics context and the initial flipped state.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(cgContext graphicsPort: CGContext, flipped initialFlippedState: Bool)
```

#### Return Value

The created [`NSGraphicsContext`](nsgraphicscontext.md) object, or `nil` if the object could not be created.

## Parameters

- `graphicsPort`: The graphics port used to create the graphics-context object, as a   (opaque type) object.
- `initialFlippedState`: Specifies the receiver’s initial flipped state. This is the value returned by   when no view has focus.

## See Also

- [init?(attributes: [NSGraphicsContext.AttributeKey : Any])](nsgraphicscontext/init(attributes:).md)
  Creates a graphics context using the specified attributes.
- [init?(bitmapImageRep: NSBitmapImageRep)](nsgraphicscontext/init(bitmapimagerep:).md)
  Creates a new graphics context using the specified bitmap image representation object as the context destination.
- [init(window: NSWindow)](nsgraphicscontext/init(window:).md)
  Creates a new graphics context for drawing into a window.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](nsgraphicscontext/init(graphicsport:flipped:).md)
  Creates a new graphics context from the specified graphics port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(cgcontext:flipped:))*