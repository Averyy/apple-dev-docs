# init(frame:pixelFormat:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSOpenGLView` object initialized with the specified frame rectangle and pixel format.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
init?(frame frameRect: NSRect, pixelFormat format: NSOpenGLPixelFormat?)
```

#### Return Value

An initialized `NSOpenGLView` object, or `nil` if the object could not be initialized.

## Parameters

- `frameRect`: The frame rectangle for the view, specified in the coordinate system of its parent view.
- `format`: The pixel format to use when creating the view’s   object.

## See Also

- [class func defaultPixelFormat() -> NSOpenGLPixelFormat](nsopenglview/defaultpixelformat.md)
  Returns a default [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object.
- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/init(frame:pixelformat:))*