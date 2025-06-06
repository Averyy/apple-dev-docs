# copyCGLContext(forPixelFormat:)

**Framework**: Core Animation  
**Kind**: method

Returns the rendering context the receiver requires for the specified pixel format.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func copyCGLContext(forPixelFormat pf: CGLPixelFormatObj) -> CGLContextObj
```

#### Return Value

A new `CGLContext` with renderers for `pixelFormat`.

#### Discussion

This method is called when a rendering context is needed by the receiver. The default implementation allocates a new context with a null share context.

You should not call this method directly, it is intended to be overridden by subclasses.

## Parameters

- `pf`: The pixel format for the rendering context.

## See Also

- [func releaseCGLContext(CGLContextObj)](caopengllayer/releasecglcontext(_:).md)
  Releases the specified rendering context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/copycglcontext(forpixelformat:))*