# releaseCGLContext(_:)

**Framework**: Core Animation  
**Kind**: method

Releases the specified rendering context.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func releaseCGLContext(_ ctx: CGLContextObj)
```

#### Discussion

This method is called when the OpenGL context that was previously returned by [`copyCGLContext(forPixelFormat:)`](caopengllayer/copycglcontext(forpixelformat:).md) is no longer needed.

You should not call this method directly, it is intended to be overridden by subclasses.

## Parameters

- `ctx`: The rendering context to release.

## See Also

- [func copyCGLContext(forPixelFormat: CGLPixelFormatObj) -> CGLContextObj](caopengllayer/copycglcontext(forpixelformat:).md)
  Returns the rendering context the receiver requires for the specified pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/releasecglcontext(_:))*