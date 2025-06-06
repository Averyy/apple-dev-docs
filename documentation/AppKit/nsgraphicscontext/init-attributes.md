# init(attributes:)

**Framework**: AppKit  
**Kind**: init

Creates a graphics context using the specified attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(attributes: [NSGraphicsContext.AttributeKey : Any] = [:])
```

#### Return Value

A new [`NSGraphicsContext`](nsgraphicscontext.md) object, or `nil` if the object could not be created.

#### Discussion

Use this method to create a graphics context for a window or bitmap destination. If you want to create a graphics context for a PDF or PostScript destination, do not use this method; instead, use the [`NSPrintOperation`](nsprintoperation.md) class to set up the printing environment needed to generate that type of information.

## Parameters

- `attributes`: A dictionary of values associated with the keys described in  . The attributes specify such things as representation format and destination.

## See Also

- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)
- [init?(bitmapImageRep: NSBitmapImageRep)](nsgraphicscontext/init(bitmapimagerep:).md)
  Creates a new graphics context using the specified bitmap image representation object as the context destination.
- [init(cgContext: CGContext, flipped: Bool)](nsgraphicscontext/init(cgcontext:flipped:).md)
  Creates a new graphics context from the specified Core Graphics context and the initial flipped state.
- [init(window: NSWindow)](nsgraphicscontext/init(window:).md)
  Creates a new graphics context for drawing into a window.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](nsgraphicscontext/init(graphicsport:flipped:).md)
  Creates a new graphics context from the specified graphics port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(attributes:))*