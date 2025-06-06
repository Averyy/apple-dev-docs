# UIGraphicsGetCurrentContext()

**Framework**: UIKit  
**Kind**: func

Returns the current graphics context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsGetCurrentContext() -> CGContext?
```

#### Return Value

The current graphics context.

#### Discussion

The current graphics context is `nil` by default. Prior to calling its `drawRect:` method, view objects push a valid context onto the stack, making it current. If you are not using a `UIView` object to do your drawing, however, you must push a valid context onto the stack manually using the [`UIGraphicsPushContext(_:)`](uigraphicspushcontext(_:).md) function.

This function may be called from any thread of your app.

## See Also

- [func UIGraphicsPushContext(CGContext)](uigraphicspushcontext(_:).md)
  Makes the specified graphics context the current context.
- [func UIGraphicsPopContext()](uigraphicspopcontext().md)
  Removes the current graphics context from the top of the stack, restoring the previous context.
- [func UIGraphicsBeginImageContextWithOptions(CGSize, Bool, CGFloat)](uigraphicsbeginimagecontextwithoptions(_:_:_:).md)
  Creates a bitmap-based graphics context with the specified options.
- [func UIRectClip(CGRect)](uirectclip(_:).md)
  Modifies the current clipping path by intersecting it with the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsgetcurrentcontext())*