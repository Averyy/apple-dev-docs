# init(graphicsPort:flipped:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new graphics context from the specified graphics port.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use [`init(cgContext:flipped:)`](./init%28cgcontext,flipped%29-9cbad.md) instead.

## Declaration

```swift
init(graphicsPort: UnsafeMutableRawPointer, flipped initialFlippedState: Bool)
```

```objc
+ (NSGraphicsContext *) graphicsContextWithGraphicsPort:(void *) graphicsPort flipped:(BOOL) initialFlippedState;
```

#### Return Value

The created [`NSGraphicsContext`](../nsgraphicscontext.md) object, or `nil` if the object could not be created.

## Parameters

- `graphicsPort`: The graphics port used to create the graphics-context object. Typically `graphicsPort` is a [`CGContext`](../../CoreGraphics/cgcontext.md) (opaque type) object.
- `initialFlippedState`: Specifies the receiver’s initial flipped state. This is the value returned by [`isFlipped`](./isflipped.md) when no view has focus.

## See Also

### Deprecated methods
- [init(window: NSWindow)](./init%28window%29.md)
  Creates a new graphics context for drawing into a window.
- [class func setGraphicsState(Int)](./setgraphicsstate%28_%29.md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(graphicsport:flipped:))*