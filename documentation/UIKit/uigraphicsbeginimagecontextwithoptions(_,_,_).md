# UIGraphicsBeginImageContextWithOptions(_:_:_:)

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Creates a bitmap-based graphics context with the specified options.

**Availability**:
- iOS 4.0+ - Deprecated in 27.0
- iPadOS 4.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`UIGraphicsImageRenderer`](./uigraphicsimagerenderer.md) instead.

## Declaration

```swift
func UIGraphicsBeginImageContextWithOptions(_ size: CGSize, _ opaque: Bool, _ scale: CGFloat)
```

```c
extern void UIGraphicsBeginImageContextWithOptions(CGSize size, BOOL opaque, CGFloat scale);
```

## Discussion

You use this function to configure the drawing environment for rendering into a bitmap. The format for the bitmap is a ARGB 32-bit integer pixel format using host-byte order. If the opaque parameter is [`true`](../Swift/true.md), the alpha channel is ignored and the bitmap is treated as fully opaque ([`CGImageAlphaInfo.noneSkipFirst`](../CoreGraphics/cgimagealphainfo/noneskipfirst.md) | [`kCGBitmapByteOrder32Host`](../CoreGraphics/kcgbitmapbyteorder32host.md)). Otherwise, each pixel uses a premultipled ARGB format ([`CGImageAlphaInfo.premultipliedFirst`](../CoreGraphics/cgimagealphainfo/premultipliedfirst.md) | [`kCGBitmapByteOrder32Host`](../CoreGraphics/kcgbitmapbyteorder32host.md)).

The environment also uses the default coordinate system for UIKit views, where the origin is in the upper-left corner and the positive axes extend down and to the right of the origin. The supplied scale factor is also applied to the coordinate system and resulting images. The drawing environment is pushed onto the graphics context stack immediately.

While the context created by this function is the current context, you can call the [`UIGraphicsGetImageFromCurrentImageContext()`](./uigraphicsgetimagefromcurrentimagecontext%28%29.md) function to retrieve an image object based on the current contents of the context. When you are done modifying the context, you must call the [`UIGraphicsEndImageContext()`](./uigraphicsendimagecontext%28%29.md) function to clean up the bitmap drawing environment and remove the graphics context from the top of the context stack. You should not use the [`UIGraphicsPopContext()`](./uigraphicspopcontext%28%29.md) function to remove this type of context from the stack.

In most other respects, the graphics context created by this function behaves like any other graphics context. You can change the context by pushing and popping other graphics contexts. You can also get the bitmap context using the [`UIGraphicsGetCurrentContext()`](./uigraphicsgetcurrentcontext%28%29.md) function.

This function may be called from any thread of your app.

## Parameters

- `size`: The size (measured in points) of the new bitmap context. This represents the size of the image returned by the [`UIGraphicsGetImageFromCurrentImageContext()`](./uigraphicsgetimagefromcurrentimagecontext%28%29.md) function. To get the size of the bitmap in pixels, you must multiply the width and height values by the value in the `scale` parameter.
- `opaque`: A Boolean flag indicating whether the bitmap is opaque. If you know the bitmap is fully opaque, specify [`true`](../Swift/true.md) to ignore the alpha channel and optimize the bitmap’s storage. Specifying [`false`](../Swift/false.md) means that the bitmap must include an alpha channel to handle any partially transparent pixels.
- `scale`: The scale factor to apply to the bitmap. If you specify a value of `0.0`, the scale factor is set to the scale factor of the device’s main screen.

## See Also

### Related Documentation
- [func UIGraphicsEndImageContext()](./uigraphicsendimagecontext%28%29.md)
  Removes the current bitmap-based graphics context from the top of the stack.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](./uigraphicsgetimagefromcurrentimagecontext%28%29.md)
  Returns an image from the contents of the current bitmap-based graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsbeginimagecontextwithoptions(_:_:_:))*