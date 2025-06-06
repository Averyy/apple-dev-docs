# enableSetNeedsDisplay

**Framework**: GLKit  
**Kind**: property

A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var enableSetNeedsDisplay: Bool { get set }
```

#### Discussion

By default, a `GLKView` object respects the standard view drawing cycle for a [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) object. However, many OpenGL ES applications need to update their contents explicitly in an animation rendering loop. When updating your contents in a rendering loop, the normal on-demand mechanism for view updates can be disabled by setting the value of this property to [`false`](https://developer.apple.com/documentation/swift/false). If your application uses a [`GLKViewController`](glkviewcontroller.md) object to drive the rendering loop, the view controller automatically sets this property to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var context: EAGLContext](glkview/context.md)
  The OpenGL ES context used when drawing the view’s contents.
- [func bindDrawable()](glkview/binddrawable.md)
  Binds the underlying framebuffer object to OpenGL ES.
- [func display()](glkview/display.md)
  Redraws the view’s contents immediately.
- [var snapshot: UIImage](glkview/snapshot.md)
  Draws the contents of the view and returns them as a new image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/enablesetneedsdisplay)*