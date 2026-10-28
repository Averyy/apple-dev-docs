# snapshot

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

Draws the contents of the view and returns them as a new image object.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var snapshot: UIImage { get }
```

```objc
@property (strong, readonly) UIImage * snapshot;
```

## Return Value

An image object.

## Discussion

When this method is called, the view sets up a drawing environment and calls your drawing method. However, instead of presenting the view’s contents on screen, they are returned to your application as an image instead. This method should be called whenever your application explicitly needs the contents of the view; never attempt to directly read the contents of the underlying framebuffer using OpenGL ES functions.

Never call this method inside your drawing function.

## See Also

### Drawing Your View’s Contents
- [var context: EAGLContext](./context.md)
  The OpenGL ES context used when drawing the view’s contents.
- [func bindDrawable()](./binddrawable%28%29.md)
  Binds the underlying framebuffer object to OpenGL ES.
- [var enableSetNeedsDisplay: Bool](./enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.
- [func display()](./display%28%29.md)
  Redraws the view’s contents immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/snapshot)*