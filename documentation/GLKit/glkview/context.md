# context

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The OpenGL ES context used when drawing the view’s contents.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var context: EAGLContext { get set }
```

```objc
@property (nonatomic, retain) EAGLContext * context;
```

## Discussion

The view uses this context as the place to create its underlying framebuffer object and it also sets the context before calling your drawing method. Never change the context from inside your drawing method.

## See Also

### Drawing Your View’s Contents
- [func bindDrawable()](./binddrawable%28%29.md)
  Binds the underlying framebuffer object to OpenGL ES.
- [var enableSetNeedsDisplay: Bool](./enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.
- [func display()](./display%28%29.md)
  Redraws the view’s contents immediately.
- [var snapshot: UIImage](./snapshot.md)
  Draws the contents of the view and returns them as a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/context)*