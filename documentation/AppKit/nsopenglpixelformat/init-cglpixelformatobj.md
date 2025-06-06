# init(cglPixelFormatObj:)

**Framework**: AppKit  
**Kind**: init

Returns an OpenGL pixel format object initialized with using an existing CGL pixel format object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
init?(cglPixelFormatObj format: CGLPixelFormatObj)
```

#### Return Value

An intialized [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object that wraps the CGL pixel format object.

#### Discussion

If your application already has a low-level CGL pixel format object, you can create an [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object to wrap it by calling this initializer. The [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object retains the CGL pixel format object by calling the `CGLRetainPixelFormat(_:)` function.

Your application should not call `CGLDestroyPixelFormat(_:)` to dispose of the CGL pixel format object. Instead, your application should call `CGLReleasePixelFormat(_:)` to decrement its reference count.

## Parameters

- `format`: An existing CGL pixel format object.

## See Also

- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)
- [convenience init?(attributes: UnsafePointer<NSOpenGLPixelFormatAttribute>)](nsopenglpixelformat/init(attributes:).md)
  Returns an OpenGL pixel format object initialized with specified pixel format attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/init(cglpixelformatobj:))*