# init(graphicsPort:flipped:)

**Framework**: AppKit  
**Kind**: init

Creates a new graphics context from the specified graphics port.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init(graphicsPort: UnsafeMutableRawPointer, flipped initialFlippedState: Bool)
```

#### Return Value

The created [`NSGraphicsContext`](nsgraphicscontext.md) object, or `nil` if the object could not be created.

## Parameters

- `graphicsPort`: The graphics port used to create the graphics-context object. Typically `graphicsPort` is a [`CGContext`](https://developer.apple.com/documentation/coregraphics/cgcontext) (opaque type) object.
- `initialFlippedState`: Specifies the receiver’s initial flipped state. This is the value returned by [`isFlipped`](nsgraphicscontext/isflipped.md) when no view has focus.

## See Also

- [init(window: NSWindow)](nsgraphicscontext/init(window:).md)
  Creates a new graphics context for drawing into a window.
- [class func setGraphicsState(Int)](nsgraphicscontext/setgraphicsstate(_:).md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(graphicsport:flipped:))*