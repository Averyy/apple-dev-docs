# NSOpenGLPixelBuffer

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that provides access to accelerated offscreen rendering.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```objc
@interface NSOpenGLPixelBuffer : NSObject
```

#### Overview

> **Deprecated**: The OpenGL API is deprecated. Use [Metal](../Metal/Metal.md) and [MetalKit](../MetalKit/MetalKit.md) instead.

Using offscreen rendering you could, for example, draw into the pixel buffer, then use the contents as a texture map elsewhere. Typically you initialize an [`NSOpenGLPixelBuffer`](./nsopenglpixelbuffer.md) object using the [`initWithTextureTarget:textureInternalFormat:textureMaxMipMapLevel:pixelsWide:pixelsHigh:`](./nsopenglpixelbuffer/initwithtexturetarget_textureinternalformat_texturemaxmipmaplevel_pixelswide_pixelshigh_.md) method and attach the resulting object to an OpenGL context with the [`setPixelBuffer:cubeMapFace:mipMapLevel:currentVirtualScreen:`](./nsopenglcontext/setpixelbuffer_cubemapface_mipmaplevel_currentvirtualscreen_.md) method of [`NSOpenGLContext`](./nsopenglcontext.md).

Every [`NSOpenGLPixelBuffer`](./nsopenglpixelbuffer.md) object wraps a low-level, platform-specific Core OpenGL (CGL) pixel buffer object. Your application can retrieve the CGL pixel buffer by calling the [`CGLPBufferObj`](./nsopenglpixelbuffer/cglpbufferobj.md) method. For more information on the underling CGL pixel buffer, see `CGL`.

## Topics

### Initializing an OpenGL Pixel Buffer
- [- initWithTextureTarget:textureInternalFormat:textureMaxMipMapLevel:pixelsWide:pixelsHigh:](./nsopenglpixelbuffer/initwithtexturetarget_textureinternalformat_texturemaxmipmaplevel_pixelswide_pixelshigh_.md)
  Returns an `NSOpenGLPixelBuffer` object initialized with the specified parameters.
- [- initWithCGLPBufferObj:](./nsopenglpixelbuffer/initwithcglpbufferobj_.md)
  Initializes and returns an OpenGL pixel buffer object that encapsulates an existing CGL pixel buffer object.
### Getting OpenGL Pixel Buffer Information
- [CGLPBufferObj](./nsopenglpixelbuffer/cglpbufferobj.md)
  The underlying CGL pixel buffer object associated with the OpenGL pixel buffer object.
- [pixelsHigh](./nsopenglpixelbuffer/pixelshigh.md)
  The height of the OpenGL pixel buffer’s texture (in pixels).
- [pixelsWide](./nsopenglpixelbuffer/pixelswide.md)
  The width of the OpenGL pixel buffer’s texture, in pixels.
- [textureInternalFormat](./nsopenglpixelbuffer/textureinternalformat.md)
  The internal format of the OpenGL pixel buffer’s texture.
- [textureMaxMipMapLevel](./nsopenglpixelbuffer/texturemaxmipmaplevel.md)
  The maximum mipmap level of the OpenGL pixel buffer’s texture.
- [textureTarget](./nsopenglpixelbuffer/texturetarget.md)
  The texture target of the OpenGL pixel buffer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Deprecated classes
- [class NSOpenGLView](./nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](./nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](./nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
- [class NSOpenGLPixelFormat](./nsopenglpixelformat.md)
  An object that specifies the types of buffers and other attributes of the OpenGL context.
- [NSCachedImageRep](./nscachedimagerep.md)
  An object that stores image data in a form that can be readily transferred to the screen.
- [class NSDrawer](./nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSForm](./nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](./nsformcell.md) objects to implement the fields.
- [class NSFormCell](./nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](./nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.
- [NSInputManager](./nsinputmanager.md)
- [NSInputServer](./nsinputserver.md)
- [NSMovie](./nsmovie.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelbuffer)*