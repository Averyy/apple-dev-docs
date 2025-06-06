# init(bitmapImageRep:)

**Framework**: AppKit  
**Kind**: init

Creates a new graphics context using the specified bitmap image representation object as the context destination.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(bitmapImageRep bitmapRep: NSBitmapImageRep)
```

#### Return Value

The created [`NSGraphicsContext`](nsgraphicscontext.md) object, or `nil` if the object could not be created.

#### Discussion

This method accepts only single plane [`NSBitmapImageRep`](nsbitmapimagerep.md) instances. It is the equivalent of using [`init(attributes:)`](nsgraphicscontext/init(attributes:).md) and passing `bitmapRep` as the value for the dictionary’s [`destination`](nsgraphicscontext/attributekey/destination.md) key.

## Parameters

- `bitmapRep`: The   object to use as the destination.

## See Also

- [init?(attributes: [NSGraphicsContext.AttributeKey : Any])](nsgraphicscontext/init(attributes:).md)
  Creates a graphics context using the specified attributes.
- [init(cgContext: CGContext, flipped: Bool)](nsgraphicscontext/init(cgcontext:flipped:).md)
  Creates a new graphics context from the specified Core Graphics context and the initial flipped state.
- [init(window: NSWindow)](nsgraphicscontext/init(window:).md)
  Creates a new graphics context for drawing into a window.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](nsgraphicscontext/init(graphicsport:flipped:).md)
  Creates a new graphics context from the specified graphics port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(bitmapimagerep:))*