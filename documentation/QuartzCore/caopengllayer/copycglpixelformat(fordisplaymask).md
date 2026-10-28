# copyCGLPixelFormat(forDisplayMask:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Returns the OpenGL pixel format suitable for rendering to the set of displays specified by the display mask.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func copyCGLPixelFormat(forDisplayMask mask: UInt32) -> CGLPixelFormatObj
```

```objc
- (CGLPixelFormatObj) copyCGLPixelFormatForDisplayMask:(uint32_t) mask;
```

## Discussion

This method is called when a pixel format object is needed for the receiver.  The default implementation returns a 32bpp fixed point pixelf format, with the `NoRecovery` and `Accelerated` flags set.

You should not call this method directly, it is intended to be overridden by subclasses.

## Parameters

- `mask`: The display mask the OpenGL content will be rendered on.

## See Also

### Managing Pixel Format
- [func releaseCGLPixelFormat(CGLPixelFormatObj)](./releasecglpixelformat%28_%29.md)
  Releases the specified OpenGL pixel format object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/copycglpixelformat(fordisplaymask:))*