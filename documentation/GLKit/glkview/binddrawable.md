# bindDrawable()

**Framework**: GLKit  
**Kind**: method

Binds the underlying framebuffer object to OpenGL ES.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func bindDrawable()
```

#### Discussion

Before calling your drawing method, the view binds the underlying framebuffer object to the context so that rendering commands are automatically drawn into it. However, some rendering strategies require you to change the target of your rendering commands to another framebuffer object, such as when you need to render to a texture first. If your application changed the framebuffer object bound to OpenGL ES, it calls this method to rebind the view’s framebuffer object to OpenGL ES.

## See Also

- [var context: EAGLContext](glkview/context.md)
  The OpenGL ES context used when drawing the view’s contents.
- [var enableSetNeedsDisplay: Bool](glkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.
- [func display()](glkview/display.md)
  Redraws the view’s contents immediately.
- [var snapshot: UIImage](glkview/snapshot.md)
  Draws the contents of the view and returns them as a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/binddrawable())*