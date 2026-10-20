# init(frame:pixelFormat:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns an `NSOpenGLView` object initialized with the specified frame rectangle and pixel format.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use MTKView instead.

## Declaration

```swift
init?(frame frameRect: NSRect, pixelFormat format: NSOpenGLPixelFormat?)
```

```objc
- (instancetype) initWithFrame:(NSRect) frameRect pixelFormat:(NSOpenGLPixelFormat *) format;
```

#### Return Value

An initialized `NSOpenGLView` object, or `nil` if the object could not be initialized.

## Parameters

- `frameRect`: The frame rectangle for the view, specified in the coordinate system of its parent view.
- `format`: The pixel format to use when creating the view’s `NSOpenGLContext` object.

## See Also

### Related Documentation
- [class func defaultPixelFormat() -> NSOpenGLPixelFormat](./defaultpixelformat%28%29.md)
  Returns a default [`NSOpenGLPixelFormat`](../nsopenglpixelformat.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/init(frame:pixelformat:))*