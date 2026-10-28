# releaseCGLContext(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Releases the specified rendering context.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func releaseCGLContext(_ ctx: CGLContextObj)
```

```objc
- (void) releaseCGLContext:(CGLContextObj) ctx;
```

## Discussion

This method is called when the OpenGL context that was previously returned by [`copyCGLContext(forPixelFormat:)`](./copycglcontext%28forpixelformat%29.md) is no longer needed.

You should not call this method directly, it is intended to be overridden by subclasses.

## Parameters

- `ctx`: The rendering context to release.

## See Also

### Managing the Rendering Context
- [func copyCGLContext(forPixelFormat: CGLPixelFormatObj) -> CGLContextObj](./copycglcontext%28forpixelformat%29.md)
  Returns the rendering context the receiver requires for the specified pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/releasecglcontext(_:))*