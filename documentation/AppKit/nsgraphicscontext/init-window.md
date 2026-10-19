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

- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](nsgraphicscontext/init(graphicsport:flipped:).md)
  Creates a new graphics context from the specified graphics port.
- [class func setGraphicsState(Int)](nsgraphicscontext/setgraphicsstate(_:).md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(window:))*