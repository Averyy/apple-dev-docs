# enableSetNeedsDisplay

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var enableSetNeedsDisplay: Bool { get set }
```

```objc
@property (nonatomic) BOOL enableSetNeedsDisplay;
```

## Discussion

By default, a `GLKView` object respects the standard view drawing cycle for a [`UIView`](../../UIKit/uiview.md) object. However, many OpenGL ES applications need to update their contents explicitly in an animation rendering loop. When updating your contents in a rendering loop, the normal on-demand mechanism for view updates can be disabled by setting the value of this property to [`false`](../../Swift/false.md). If your application uses a [`GLKViewController`](../glkviewcontroller.md) object to drive the rendering loop, the view controller automatically sets this property to [`false`](../../Swift/false.md).

## See Also

### Drawing Your View’s Contents
- [var context: EAGLContext](./context.md)
  The OpenGL ES context used when drawing the view’s contents.
- [func bindDrawable()](./binddrawable%28%29.md)
  Binds the underlying framebuffer object to OpenGL ES.
- [func display()](./display%28%29.md)
  Redraws the view’s contents immediately.
- [var snapshot: UIImage](./snapshot.md)
  Draws the contents of the view and returns them as a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/enablesetneedsdisplay)*