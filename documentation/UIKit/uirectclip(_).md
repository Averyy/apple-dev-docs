# UIRectClip(_:)

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Modifies the current clipping path by intersecting it with the specified rectangle.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
func UIRectClip(_ rect: CGRect)
```

```c
extern void UIRectClip(CGRect rect);
```

#### Discussion

Each call to this function permanently shrinks the clipping path of the current graphics context using the specified rectangle. You cannot use this function to expand the clipping region path. If the current graphics context is `nil`, this function does nothing.

If you need to return the clipping path to its original shape in your drawing code, you should save the current graphics context before calling this function. To save the current state of the graphics context, call the [`saveGState()`](../CoreGraphics/cgcontext/savegstate%28%29.md) function before making your modifications. When you are ready to restore the original clipping region, you can then use the [`restoreGState()`](../CoreGraphics/cgcontext/restoregstate%28%29.md) function to restore the previous graphics state.

This function may be called from any thread of your app.

## Parameters

- `rect`: The rectangle to intersect with the clipping region. If the width or height of the rectangle are less than 0, this function does not change the clipping path.

## See Also

### Graphics context primitives
- [func UIGraphicsGetCurrentContext() -> CGContext?](./uigraphicsgetcurrentcontext%28%29.md)
  Returns the current graphics context.
- [func UIGraphicsPushContext(CGContext)](./uigraphicspushcontext%28_%29.md)
  Makes the specified graphics context the current context.
- [func UIGraphicsPopContext()](./uigraphicspopcontext%28%29.md)
  Removes the current graphics context from the top of the stack, restoring the previous context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectclip(_:))*