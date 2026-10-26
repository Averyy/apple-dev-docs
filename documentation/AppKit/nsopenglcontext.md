# NSOpenGLContext

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: The OpenGL API is deprecated. Use [Metal](../Metal/Metal.md) and [MetalKit](../MetalKit/MetalKit.md) instead.

## Declaration

```swift
class NSOpenGLContext
```

```objc
@interface NSOpenGLContext : NSObject
```

#### Overview

An OpenGL context is created using an [`NSOpenGLPixelFormat`](./nsopenglpixelformat.md)object that specifies the context’s buffer types and other attributes. A context can be full-screen, offscreen, or associated with an [`NSView`](./nsview.md) object. A context draws into its *drawable object*, which is the frame buffer that is the target of OpenGL drawing operations.

Every [`NSOpenGLContext`](./nsopenglcontext.md) object wraps a low-level, platform-specific Core OpenGL (CGL) context. Your application can retrieve the CGL context by calling the [`cglContextObj`](./nsopenglcontext/cglcontextobj.md) method. For more information on the underling CGL context, see `CGL`.

## Topics

### Creating Contexts
- [init?(format: NSOpenGLPixelFormat, share: NSOpenGLContext?)](./nsopenglcontext/init%28format,share%29.md)
  Returns an OpenGL context object initialized with the specified pixel format information.
- [init?(cglContextObj: CGLContextObj)](./nsopenglcontext/init%28cglcontextobj%29-30lqr.md)
  Initializes and returns an OpenGL context object using an existing CGL context.
### Managing the Current Context
- [class func clearCurrentContext()](./nsopenglcontext/clearcurrentcontext%28%29.md)
  Clears the current context.
- [class var current: NSOpenGLContext?](./nsopenglcontext/current.md)
  Returns the current OpenGL graphics context.
- [func makeCurrentContext()](./nsopenglcontext/makecurrentcontext%28%29.md)
  Sets the context as the current OpenGL context object.
### Managing the Drawable Object
- [var view: NSView?](./nsopenglcontext/view.md)
  Returns the OpenGL context’s view.
- [func clearDrawable()](./nsopenglcontext/cleardrawable%28%29.md)
  Disassociates the OpenGL context from its viewport.
- [func update()](./nsopenglcontext/update%28%29.md)
  Updates the OpenGL context’s drawable object.
- [- setFullScreen](./nsopenglcontext/setfullscreen.md)
  Sets the OpenGL context to full-screen mode.
- [- setOffScreen:width:height:rowbytes:](./nsopenglcontext/setoffscreen_width_height_rowbytes_.md)
  Instructs the OpenGL context to render into an offscreen buffer with the specified attributes.
### Flushing the Drawing Buffer
- [func flushBuffer()](./nsopenglcontext/flushbuffer%28%29.md)
  Copies the back buffer to the front buffer of the OpenGL context.
### Context Parameter Handling
- [func setValues(UnsafePointer<GLint>, for: NSOpenGLContext.Parameter)](./nsopenglcontext/setvalues%28_,for%29.md)
  Sets the value of the specified parameter.
- [func getValues(UnsafeMutablePointer<GLint>, for: NSOpenGLContext.Parameter)](./nsopenglcontext/getvalues%28_,for%29.md)
  Returns the value of the requested parameter.
### Working with Virtual Screens
- [var currentVirtualScreen: GLint](./nsopenglcontext/currentvirtualscreen.md)
  Returns the current virtual screen for the OpenGL context.
### Getting the CGL Context Object
- [var cglContextObj: CGLContextObj?](./nsopenglcontext/cglcontextobj.md)
  Returns the low-level, platform-specific Core OpenGL (CGL) context object represented by the receiver.
### Getting the Pixel Format
- [var pixelFormat: NSOpenGLPixelFormat](./nsopenglcontext/pixelformat.md)
  The pixel format of the OpenGL context.
### Getting the OpenGL Version
- [static var openGLVersion: (major: GLint, minor: GLint)](./nsopenglcontext/openglversion.md)
  The version of OpenGL.
### Constants
- [NSOpenGLContext.Parameter](./nsopenglcontext/parameter.md)
  Constants that specify context parameters.
### Initializers
- [init?(CGLContextObj: CGLContextObj)](./nsopenglcontext/init%28cglcontextobj%29-4jlgm.md)
- [init?(format: NSOpenGLPixelFormat, shareContext: NSOpenGLContext?)](./nsopenglcontext/init%28format,sharecontext%29.md)
### Copying Attributes
- [- copyAttributesFromContext:withMask:](./nsopenglcontext/copyattributesfromcontext_withmask_.md)
  Copies selected groups of state variables to the OpenGL context.
### Creating Textures
- [- createTexture:fromView:internalFormat:](./nsopenglcontext/createtexture_fromview_internalformat_.md)
  Creates a new texture from the contents of the specified view.
### Working with Pixel Buffers
- [- setPixelBuffer:cubeMapFace:mipMapLevel:currentVirtualScreen:](./nsopenglcontext/setpixelbuffer_cubemapface_mipmaplevel_currentvirtualscreen_.md)
  Attaches the specified pixel buffer to the OpenGL context.
- [- pixelBuffer](./nsopenglcontext/pixelbuffer.md)
  Returns the pixel-buffer object attached to the OpenGL context.
- [- pixelBufferCubeMapFace](./nsopenglcontext/pixelbuffercubemapface.md)
  Returns the cube map face of the pixel buffer attached to the OpenGL context.
- [- pixelBufferMipMapLevel](./nsopenglcontext/pixelbuffermipmaplevel.md)
  Returns the mipmap level of the pixel buffer attached to the OpenGL context.
- [- setTextureImageToPixelBuffer:colorBuffer:](./nsopenglcontext/settextureimagetopixelbuffer_colorbuffer_.md)
  Attaches the image data in the specified pixel buffer to the texture object currently bound by the OpenGL context.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSLocking](../Foundation/nslocking.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated classes
- [class NSOpenGLView](./nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLLayer](./nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
- [class NSOpenGLPixelFormat](./nsopenglpixelformat.md)
  An object that specifies the types of buffers and other attributes of the OpenGL context.
- [class NSDrawer](./nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSForm](./nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](./nsformcell.md) objects to implement the fields.
- [class NSFormCell](./nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](./nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.
- [NSOpenGLPixelBuffer](./nsopenglpixelbuffer.md)
  An object that provides access to accelerated offscreen rendering.
- [NSCachedImageRep](./nscachedimagerep.md)
  An object that stores image data in a form that can be readily transferred to the screen.
- [NSInputManager](./nsinputmanager.md)
- [NSInputServer](./nsinputserver.md)
- [NSMovie](./nsmovie.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext)*