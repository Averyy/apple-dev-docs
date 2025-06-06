# context

**Framework**: GLKit  
**Kind**: property

The OpenGL ES context used when drawing the view’s contents.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var context: EAGLContext { get set }
```

#### Discussion

The view uses this context as the place to create its underlying framebuffer object and it also sets the context before calling your drawing method. Never change the context from inside your drawing method.

## See Also

- [func bindDrawable()](glkview/binddrawable.md)
  Binds the underlying framebuffer object to OpenGL ES.
- [var enableSetNeedsDisplay: Bool](glkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.
- [func display()](glkview/display.md)
  Redraws the view’s contents immediately.
- [var snapshot: UIImage](glkview/snapshot.md)
  Draws the contents of the view and returns them as a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/context)*