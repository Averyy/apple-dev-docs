# init(cglPixelFormatObj:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns an OpenGL pixel format object initialized with using an existing CGL pixel format object.

**Availability**:
- macOS 10.6+ - Deprecated in 10.14

## Declaration

```swift
init?(cglPixelFormatObj format: CGLPixelFormatObj)
```

```objc
- (NSOpenGLPixelFormat *) initWithCGLPixelFormatObj:(CGLPixelFormatObj) format;
```

## Return Value

An intialized [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object that wraps the CGL pixel format object.

## Discussion

If your application already has a low-level CGL pixel format object, you can create an [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object to wrap it by calling this initializer. The [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object retains the CGL pixel format object by calling the `CGLRetainPixelFormat(_:)` function.

Your application should not call `CGLDestroyPixelFormat(_:)` to dispose of the CGL pixel format object. Instead, your application should call `CGLReleasePixelFormat(_:)` to decrement its reference count.

## Parameters

- `format`: An existing CGL pixel format object.

## See Also

### Creating an OpenGL Pixel Format
- [convenience init?(attributes: UnsafePointer<NSOpenGLPixelFormatAttribute>)](./init%28attributes%29.md)
  Returns an OpenGL pixel format object initialized with specified pixel format attributes.
- [- initWithData:](./initwithdata_.md)
  Returns an OpenGL pixel format object initialized with specified pixel format attribute data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/init(cglpixelformatobj:)-2zqw4)*