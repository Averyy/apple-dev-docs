# UIGraphicsPopContext()

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Removes the current graphics context from the top of the stack, restoring the previous context.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsPopContext()
```

```c
extern void UIGraphicsPopContext();
```

## Discussion

Use this function to balance calls to the [`UIGraphicsPushContext(_:)`](./uigraphicspushcontext%28_%29.md) function.

This function may be called from any thread of your app.

## See Also

### Graphics context primitives
- [func UIGraphicsGetCurrentContext() -> CGContext?](./uigraphicsgetcurrentcontext%28%29.md)
  Returns the current graphics context.
- [func UIGraphicsPushContext(CGContext)](./uigraphicspushcontext%28_%29.md)
  Makes the specified graphics context the current context.
- [func UIRectClip(CGRect)](./uirectclip%28_%29.md)
  Modifies the current clipping path by intersecting it with the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspopcontext())*