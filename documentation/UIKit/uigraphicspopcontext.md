# UIGraphicsPopContext()

**Framework**: UIKit  
**Kind**: func

Removes the current graphics context from the top of the stack, restoring the previous context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsPopContext()
```

#### Discussion

Use this function to balance calls to the [`UIGraphicsPushContext(_:)`](uigraphicspushcontext(_:).md) function.

This function may be called from any thread of your app.

## See Also

- [func UIGraphicsGetCurrentContext() -> CGContext?](uigraphicsgetcurrentcontext().md)
  Returns the current graphics context.
- [func UIGraphicsPushContext(CGContext)](uigraphicspushcontext(_:).md)
  Makes the specified graphics context the current context.
- [func UIGraphicsBeginImageContextWithOptions(CGSize, Bool, CGFloat)](uigraphicsbeginimagecontextwithoptions(_:_:_:).md)
  Creates a bitmap-based graphics context with the specified options.
- [func UIRectClip(CGRect)](uirectclip(_:).md)
  Modifies the current clipping path by intersecting it with the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspopcontext())*