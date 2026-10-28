# init(window:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new graphics context for drawing into a window.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Add instances of NSView to display content in a window

## Declaration

```swift
init(window: NSWindow)
```

```objc
+ (NSGraphicsContext *) graphicsContextWithWindow:(NSWindow *) window;
```

## Return Value

The created [`NSGraphicsContext`](../nsgraphicscontext.md) object, or `nil` if the object could not be created.

## Parameters

- `window`: The window object representing the window to use for drawing.

## See Also

### Deprecated methods
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](./init%28graphicsport,flipped%29.md)
  Creates a new graphics context from the specified graphics port.
- [class func setGraphicsState(Int)](./setgraphicsstate%28_%29.md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.
- [- focusStack](./focusstack.md)
  Returns the object used by the context to track the hierarchy of views with locked focus.
- [- setFocusStack:](./setfocusstack_.md)
  Sets the object used by the receiver to track the hierarchy of views with locked focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/init(window:))*