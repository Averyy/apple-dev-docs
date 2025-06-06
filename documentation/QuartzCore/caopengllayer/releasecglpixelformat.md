# releaseCGLPixelFormat(_:)

**Framework**: Core Animation  
**Kind**: method

Releases the specified OpenGL pixel format object.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func releaseCGLPixelFormat(_ pf: CGLPixelFormatObj)
```

#### Discussion

This method is called when the OpenGL pixel format that was previously returned by [`copyCGLContext(forPixelFormat:)`](caopengllayer/copycglcontext(forpixelformat:).md).

You should not call this method directly, it is intended to be overridden by subclasses.

## Parameters

- `pf`: The pixel format object to release.

## See Also

- [func copyCGLPixelFormat(forDisplayMask: UInt32) -> CGLPixelFormatObj](caopengllayer/copycglpixelformat(fordisplaymask:).md)
  Returns the OpenGL pixel format suitable for rendering to the set of displays specified by the display mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/releasecglpixelformat(_:))*