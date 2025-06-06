# UIRectClip(_:)

**Framework**: UIKit  
**Kind**: func

Modifies the current clipping path by intersecting it with the specified rectangle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
func UIRectClip(_ rect: CGRect)
```

#### Discussion

Each call to this function permanently shrinks the clipping path of the current graphics context using the specified rectangle. You cannot use this function to expand the clipping region path. If the current graphics context is `nil`, this function does nothing.

If you need to return the clipping path to its original shape in your drawing code, you should save the current graphics context before calling this function. To save the current state of the graphics context, call the [`saveGState()`](https://developer.apple.com/documentation/CoreGraphics/CGContext/saveGState()) function before making your modifications. When you are ready to restore the original clipping region, you can then use the [`restoreGState()`](https://developer.apple.com/documentation/CoreGraphics/CGContext/restoreGState()) function to restore the previous graphics state.

This function may be called from any thread of your app.

## Parameters

- `rect`: The rectangle to intersect with the clipping region. If the width or height of the rectangle are less than 0, this function does not change the clipping path.

## See Also

- [func UIGraphicsGetCurrentContext() -> CGContext?](uigraphicsgetcurrentcontext().md)
  Returns the current graphics context.
- [func UIGraphicsPushContext(CGContext)](uigraphicspushcontext(_:).md)
  Makes the specified graphics context the current context.
- [func UIGraphicsPopContext()](uigraphicspopcontext().md)
  Removes the current graphics context from the top of the stack, restoring the previous context.
- [func UIGraphicsBeginImageContextWithOptions(CGSize, Bool, CGFloat)](uigraphicsbeginimagecontextwithoptions(_:_:_:).md)
  Creates a bitmap-based graphics context with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectclip(_:))*