# display()

**Framework**: GLKit  
**Kind**: method

Redraws the view’s contents immediately.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func display()
```

#### Discussion

This method causes your drawing method to be called immediately and then presents the rendered image to the screen. Your application typically calls this method inside of a rendering loop, such as the one provided by the [`GLKViewController`](glkviewcontroller.md) class, in order to provide a continuous smooth animation.

Never call this method inside your drawing function.

## See Also

- [var context: EAGLContext](glkview/context.md)
  The OpenGL ES context used when drawing the view’s contents.
- [func bindDrawable()](glkview/binddrawable.md)
  Binds the underlying framebuffer object to OpenGL ES.
- [var enableSetNeedsDisplay: Bool](glkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.
- [var snapshot: UIImage](glkview/snapshot.md)
  Draws the contents of the view and returns them as a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/display())*