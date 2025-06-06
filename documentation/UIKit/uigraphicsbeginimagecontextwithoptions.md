# UIGraphicsBeginImageContextWithOptions(_:_:_:)

**Framework**: UIKit  
**Kind**: func

Creates a bitmap-based graphics context with the specified options.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsBeginImageContextWithOptions(_ size: CGSize, _ opaque: Bool, _ scale: CGFloat)
```

#### Discussion

You use this function to configure the drawing environment for rendering into a bitmap. The format for the bitmap is a ARGB 32-bit integer pixel format using host-byte order. If the opaque parameter is [`true`](https://developer.apple.com/documentation/swift/true), the alpha channel is ignored and the bitmap is treated as fully opaque ([`CGImageAlphaInfo.noneSkipFirst`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/noneSkipFirst) | [`kCGBitmapByteOrder32Host`](https://developer.apple.com/documentation/CoreGraphics/kCGBitmapByteOrder32Host)). Otherwise, each pixel uses a premultipled ARGB format ([`CGImageAlphaInfo.premultipliedFirst`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/premultipliedFirst) | [`kCGBitmapByteOrder32Host`](https://developer.apple.com/documentation/CoreGraphics/kCGBitmapByteOrder32Host)).

The environment also uses the default coordinate system for UIKit views, where the origin is in the upper-left corner and the positive axes extend down and to the right of the origin. The supplied scale factor is also applied to the coordinate system and resulting images. The drawing environment is pushed onto the graphics context stack immediately.

While the context created by this function is the current context, you can call the [`UIGraphicsGetImageFromCurrentImageContext()`](uigraphicsgetimagefromcurrentimagecontext().md) function to retrieve an image object based on the current contents of the context. When you are done modifying the context, you must call the [`UIGraphicsEndImageContext()`](uigraphicsendimagecontext().md) function to clean up the bitmap drawing environment and remove the graphics context from the top of the context stack. You should not use the [`UIGraphicsPopContext()`](uigraphicspopcontext().md) function to remove this type of context from the stack.

In most other respects, the graphics context created by this function behaves like any other graphics context. You can change the context by pushing and popping other graphics contexts. You can also get the bitmap context using the [`UIGraphicsGetCurrentContext()`](uigraphicsgetcurrentcontext().md) function.

This function may be called from any thread of your app.

## Parameters

- `size`: The size (measured in points) of the new bitmap context. This represents the size of the image returned by the   function. To get the size of the bitmap in pixels, you must multiply the width and height values by the value in the   parameter.
- `opaque`: A Boolean flag indicating whether the bitmap is opaque. If you know the bitmap is fully opaque, specify   to ignore the alpha channel and optimize the bitmap’s storage. Specifying   means that the bitmap must include an alpha channel to handle any partially transparent pixels.
- `scale`: The scale factor to apply to the bitmap. If you specify a value of  , the scale factor is set to the scale factor of the device’s main screen.

## See Also

- [func UIGraphicsEndImageContext()](uigraphicsendimagecontext().md)
  Removes the current bitmap-based graphics context from the top of the stack.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](uigraphicsgetimagefromcurrentimagecontext().md)
  Returns an image from the contents of the current bitmap-based graphics context.
- [func UIGraphicsGetCurrentContext() -> CGContext?](uigraphicsgetcurrentcontext().md)
  Returns the current graphics context.
- [func UIGraphicsPushContext(CGContext)](uigraphicspushcontext(_:).md)
  Makes the specified graphics context the current context.
- [func UIGraphicsPopContext()](uigraphicspopcontext().md)
  Removes the current graphics context from the top of the stack, restoring the previous context.
- [func UIRectClip(CGRect)](uirectclip(_:).md)
  Modifies the current clipping path by intersecting it with the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsbeginimagecontextwithoptions(_:_:_:))*