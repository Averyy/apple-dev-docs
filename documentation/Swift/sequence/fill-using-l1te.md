# fill(using:)

**Framework**: Swift  
**Kind**: method

Fills this list of rects in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.

**Availability**:
- macOS 10.9+
- Swift 4.0+

## Declaration

```swift
func fill(using operation: NSCompositingOperation = NSGraphicsContext.current?.compositingOperation ?? .sourceOver)
```

#### Discussion

> **Note**: There must be a set current NSGraphicsContext.

There must be a set current NSGraphicsContext.

## See Also

- [func fill(using: NSCompositingOperation)](sequence/fill(using:)-45en6.md)
  Fills this list of rects in the current NSGraphicsContext with that rect’s associated color The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
- [func clip()](sequence/clip.md)
  Modifies the current graphics context clipping path by intersecting it with the graphical union of this list of rects This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/fill(using:)-l1te)*