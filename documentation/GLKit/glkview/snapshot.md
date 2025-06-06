# snapshot

**Framework**: GLKit  
**Kind**: property

Draws the contents of the view and returns them as a new image object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
var snapshot: UIImage { get }
```

#### Return Value

An image object.

#### Discussion

When this method is called, the view sets up a drawing environment and calls your drawing method. However, instead of presenting the view’s contents on screen, they are returned to your application as an image instead. This method should be called whenever your application explicitly needs the contents of the view; never attempt to directly read the contents of the underlying framebuffer using OpenGL ES functions.

Never call this method inside your drawing function.

## See Also

- [var context: EAGLContext](glkview/context.md)
  The OpenGL ES context used when drawing the view’s contents.
- [func bindDrawable()](glkview/binddrawable.md)
  Binds the underlying framebuffer object to OpenGL ES.
- [var enableSetNeedsDisplay: Bool](glkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.
- [func display()](glkview/display.md)
  Redraws the view’s contents immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/snapshot)*