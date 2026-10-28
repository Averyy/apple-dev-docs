# bindDrawable()

**Framework**: GLKit  
**Kind**: method  
**Role**: Instance Method

Binds the underlying framebuffer object to OpenGL ES.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func bindDrawable()
```

```objc
- (void) bindDrawable;
```

## Discussion

Before calling your drawing method, the view binds the underlying framebuffer object to the context so that rendering commands are automatically drawn into it. However, some rendering strategies require you to change the target of your rendering commands to another framebuffer object, such as when you need to render to a texture first. If your application changed the framebuffer object bound to OpenGL ES, it calls this method to rebind the view’s framebuffer object to OpenGL ES.

## See Also

### Drawing Your View’s Contents
- [var context: EAGLContext](./context.md)
  The OpenGL ES context used when drawing the view’s contents.
- [var enableSetNeedsDisplay: Bool](./enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.
- [func display()](./display%28%29.md)
  Redraws the view’s contents immediately.
- [var snapshot: UIImage](./snapshot.md)
  Draws the contents of the view and returns them as a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/binddrawable())*