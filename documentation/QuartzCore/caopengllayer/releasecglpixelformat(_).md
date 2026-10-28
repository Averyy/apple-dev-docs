# releaseCGLPixelFormat(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Releases the specified OpenGL pixel format object.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func releaseCGLPixelFormat(_ pf: CGLPixelFormatObj)
```

```objc
- (void) releaseCGLPixelFormat:(CGLPixelFormatObj) pf;
```

## Discussion

This method is called when the OpenGL pixel format that was previously returned by [`copyCGLContext(forPixelFormat:)`](./copycglcontext%28forpixelformat%29.md).

You should not call this method directly, it is intended to be overridden by subclasses.

## Parameters

- `pf`: The pixel format object to release.

## See Also

### Managing Pixel Format
- [func copyCGLPixelFormat(forDisplayMask: UInt32) -> CGLPixelFormatObj](./copycglpixelformat%28fordisplaymask%29.md)
  Returns the OpenGL pixel format suitable for rendering to the set of displays specified by the display mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/releasecglpixelformat(_:))*