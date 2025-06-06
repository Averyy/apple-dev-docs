# view

**Framework**: AppKit  
**Kind**: property

Returns the OpenGL context’s view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
weak var view: NSView? { get set }
```

#### Return Value

The view, or `nil` if the receiver has no drawable object, is in full-screen mode, or is in offscreen mode.

## See Also

- [func clearDrawable()](nsopenglcontext/cleardrawable.md)
  Disassociates the OpenGL context from its viewport.
- [func update()](nsopenglcontext/update.md)
  Updates the OpenGL context’s drawable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/view)*