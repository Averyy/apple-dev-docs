# OpenGL Profiles

**Framework**: AppKit

Constants that specify the functionality provided by the renderer.

#### Overview

An OpenGL Profile is requested as part of the pixel format attributes string. When a context is created for a profile, the context must at least implement the requested version of the OpenGL specification. The context may implement a different version of the OpenGL specification as long as the version it implements is compatible with the requested version.

## Topics

### Constants
- [var NSOpenGLProfileVersionLegacy: Int](nsopenglprofileversionlegacy.md)
  The requested profile is a legacy (pre-OpenGL 3.0) profile.
- [var NSOpenGLProfileVersion3_2Core: Int](nsopenglprofileversion3_2core.md)
  The requested profile must implement the OpenGL 3.2 core functionality.
- [var NSOpenGLProfileVersion4_1Core: Int](nsopenglprofileversion4_1core.md)

## See Also

- [typealias NSOpenGLPixelFormatAttribute](nsopenglpixelformatattribute.md)
  Pixel format attributes for OpenGL.
- [OpenGL Pixel Format Attributes](opengl-pixel-format-attributes.md)
  Pixel format attributes for OpenGL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/opengl-profiles)*