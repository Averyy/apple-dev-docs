# OpenGL ES

**Framework**: OpenGL ES  
**Kind**: module

Create 3D and 2D graphics effects with this compact, efficient subset of OpenGL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

OpenGL ES provides a C-based interface for hardware-accelerated 2D and 3D graphics rendering. The OpenGL ES framework (`OpenGLES.framework`) in iOS provides implementations of versions 1.1, 2.0, and 3.0 of the OpenGL ES specification.

This collection of documents describes the platform-specific APIs for OpenGL ES on iOS devices, also known as EAGL. EAGL provides graphics contexts that encapsulate all OpenGL ES state and the ability to configure a Core Animation layer to be the destination for OpenGL ES drawing commands. EAGL also allows OpenGL ES objects, such as textures, renderbuffers, and framebuffers, to be shared between two or more graphics contexts.

The Khronos Group maintains the OpenGL ES specifications and references for the cross-platform OpenGL ES APIs:

- [`OpenGL ES API Registry`](https://developer.apple.comhttp://www.khronos.org/registry/gles/) is the official repository of OpenGL ES specification and extension documents provided by the Khronos Group.
- For a complete reference to the OpenGL ES APIs and OpenGL ES Shading Language, see the collection for the version of OpenGL ES you plan to use:
- [`OpenGL ES 1.1 Reference Pages`](https://developer.apple.comhttp://www.khronos.org/opengles/sdk/1.1/docs/man/)
- [`OpenGL ES 2.0 Reference Pages`](https://developer.apple.comhttp://www.khronos.org/opengles/sdk/docs/man/)
- [`OpenGL ES 3.0 Reference Pages`](https://developer.apple.comhttp://www.khronos.org/opengles/sdk/docs/man3/)

## Topics

### Classes
- [class EAGLContext](eaglcontext.md)
  An [`EAGLContext`](eaglcontext.md) object manages an OpenGL ES —the state information, commands, and resources needed to draw using OpenGL ES. To execute OpenGL ES commands, you need a current rendering context.
- [class EAGLSharegroup](eaglsharegroup.md)
  An `EAGLSharegroup` object manages OpenGL ES resources associated with one or more `EAGLContext` objects. It is created when an `EAGLContext` object is initialized and disposed of when the last `EAGLContext` object that references it is released. As an opaque object, there is no developer accessible API.
### Protocols
- [protocol EAGLDrawable](eagldrawable.md)
  iOS objects that implement the `EAGLDrawable` protocol can be used as a rendering surface and displayed to the screen by an `EAGLContext` object. In iOS 2.0, this protocol is implemented only by the `CAEAGLLayer` class, but in the future other classes may choose to implement the protocol. The `EAGLDrawable` protocol is not intended to be implemented by objects outside of the iOS.
### Reference
- [EAGL Functions](eagl-functions.md)
  This document describes the functions in the OpenGL ES framework.
- [OpenGL ES Enumerations](opengl-es-enumerations.md)
- [OpenGL ES Constants](opengl-es-constants.md)
- [OpenGL ES Functions](opengl-es-functions.md)
- [OpenGL ES Data Types](opengl-es-data-types.md)
### Variables
- [var GL_SAMPLER_2D_SHADOW: Int32](gl_sampler_2d_shadow.md)
- [var GL_TEXTURE_ENV_COLOR: Int32](gl_texture_env_color.md)
- [var GL_TEXTURE_ENV_MODE: Int32](gl_texture_env_mode.md)
- [var GL_TIMEOUT_IGNORED: UInt64](gl_timeout_ignored.md)
### Functions
- [func glFramebufferTextureLayer(GLenum, GLenum, GLuint, GLint, GLint)](glframebuffertexturelayer(_:_:_:_:_:).md)

## See Also

- [OpenGL ES Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793)


---

*[View on Apple Developer](https://developer.apple.com/documentation/OpenGLES)*