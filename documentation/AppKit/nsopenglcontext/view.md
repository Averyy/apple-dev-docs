# view

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the OpenGL context’s view.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

## Declaration

```swift
@MainActor
weak var view: NSView? { get set }
```

```objc
@property (weak, nullable) NSView * view;
```

#### Return Value

The view, or `nil` if the receiver has no drawable object, is in full-screen mode, or is in offscreen mode.

## See Also

### Managing the Drawable Object
- [func clearDrawable()](./cleardrawable%28%29.md)
  Disassociates the OpenGL context from its viewport.
- [func update()](./update%28%29.md)
  Updates the OpenGL context’s drawable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/view)*