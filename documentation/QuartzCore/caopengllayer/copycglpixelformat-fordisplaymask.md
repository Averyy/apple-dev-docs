# copyCGLPixelFormat(forDisplayMask:)

**Framework**: Core Animation  
**Kind**: method

Returns the OpenGL pixel format suitable for rendering to the set of displays specified by the display mask.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func copyCGLPixelFormat(forDisplayMask mask: UInt32) -> CGLPixelFormatObj
```

#### Discussion

This method is called when a pixel format object is needed for the receiver.  The default implementation returns a 32bpp fixed point pixelf format, with the `NoRecovery` and `Accelerated` flags set.

You should not call this method directly, it is intended to be overridden by subclasses.

## Parameters

- `mask`: The display mask the OpenGL content will be rendered on.

## See Also

- [func releaseCGLPixelFormat(CGLPixelFormatObj)](caopengllayer/releasecglpixelformat(_:).md)
  Releases the specified OpenGL pixel format object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/copycglpixelformat(fordisplaymask:))*