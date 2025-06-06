# init(window:)

**Framework**: AppKit  
**Kind**: init

Creates a new graphics context for drawing into a window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init(window: NSWindow)
```

#### Return Value

The created [`NSGraphicsContext`](nsgraphicscontext.md) object, or `nil` if the object could not be created.

## Parameters

- `window`: The window object representing the window to use for drawing.

## See Also

- [init?(attributes: [NSGraphicsContext.AttributeKey : Any])](nsgraphicscontext/init(attributes:).md)
  Creates a graphics context using the specified attributes.
- [init?(bitmapImageRep: NSBitmapImageRep)](nsgraphicscontext/init(bitmapimagerep:).md)
  Creates a new graphics context using the specified bitmap image representation object as the context destination.
- [init(cgContext: CGContext, flipped: Bool)](nsgraphicscontext/init(cgcontext:flipped:).md)
  Creates a new graphics context from the specified Core Graphics context and the initial flipped state.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](nsgraphicscontext/init(graphicsport:flipped:).md)
  Creates a new graphics context from the specified graphics port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(window:))*