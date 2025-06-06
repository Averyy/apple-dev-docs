# UIGraphicsPushContext(_:)

**Framework**: UIKit  
**Kind**: func

Makes the specified graphics context the current context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsPushContext(_ context: CGContext)
```

#### Discussion

You can use this function to save the previous graphics state and make the specified context the current context. You must balance calls to this function with matching calls to the [`UIGraphicsPopContext()`](uigraphicspopcontext().md) function.

This function may be called from any thread of your app.

## Parameters

- `context`: The graphics context to make the current context.

## See Also

- [func UIGraphicsGetCurrentContext() -> CGContext?](uigraphicsgetcurrentcontext().md)
  Returns the current graphics context.
- [func UIGraphicsPopContext()](uigraphicspopcontext().md)
  Removes the current graphics context from the top of the stack, restoring the previous context.
- [func UIGraphicsBeginImageContextWithOptions(CGSize, Bool, CGFloat)](uigraphicsbeginimagecontextwithoptions(_:_:_:).md)
  Creates a bitmap-based graphics context with the specified options.
- [func UIRectClip(CGRect)](uirectclip(_:).md)
  Modifies the current clipping path by intersecting it with the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspushcontext(_:))*