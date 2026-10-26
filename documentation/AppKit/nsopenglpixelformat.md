# NSOpenGLPixelFormat

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that specifies the types of buffers and other attributes of the OpenGL context.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: The OpenGL API is deprecated. Use [Metal](../Metal/Metal.md) and [MetalKit](../MetalKit/MetalKit.md) instead.

## Declaration

```swift
class NSOpenGLPixelFormat
```

```objc
@interface NSOpenGLPixelFormat : NSObject
```

#### Overview

To render with OpenGL into an [`NSOpenGLContext`](./nsopenglcontext.md), you must specify the context’s pixel format.

Every [`NSOpenGLPixelFormat`](./nsopenglpixelformat.md) object wraps a low-level, platform-specific Core OpenGL (CGL) pixel format object. Your application can retrieve the CGL pixel format object by calling the [`cglPixelFormatObj`](./nsopenglpixelformat/cglpixelformatobj.md) method. For more information on the underling CGL pixel format object, see `CGL`.

## Topics

### Creating an OpenGL Pixel Format
- [init?(cglPixelFormatObj: CGLPixelFormatObj)](./nsopenglpixelformat/init%28cglpixelformatobj%29-2zqw4.md)
  Returns an OpenGL pixel format object initialized with using an existing CGL pixel format object.
- [convenience init?(attributes: UnsafePointer<NSOpenGLPixelFormatAttribute>)](./nsopenglpixelformat/init%28attributes%29.md)
  Returns an OpenGL pixel format object initialized with specified pixel format attributes.
- [- initWithData:](./nsopenglpixelformat/initwithdata_.md)
  Returns an OpenGL pixel format object initialized with specified pixel format attribute data.
### Managing the Pixel Format
- [var cglPixelFormatObj: CGLPixelFormatObj?](./nsopenglpixelformat/cglpixelformatobj.md)
  The low-level, platform-specific Core OpenGL (CGL) pixel format object represented by the receiver.
- [func getValues(UnsafeMutablePointer<GLint>, forAttribute: NSOpenGLPixelFormatAttribute, forVirtualScreen: GLint)](./nsopenglpixelformat/getvalues%28_,forattribute,forvirtualscreen%29.md)
  Gets the value for the specified pixel format attribute.
- [var numberOfVirtualScreens: GLint](./nsopenglpixelformat/numberofvirtualscreens.md)
  The number of virtual screens associated with the OpenGL pixel format.
### Constants
- [typealias NSOpenGLPixelFormatAttribute](./nsopenglpixelformatattribute.md)
  Pixel format attributes for OpenGL.
- [OpenGL Pixel Format Attributes](./opengl-pixel-format-attributes.md)
  Pixel format attributes for OpenGL.
- [OpenGL Profiles](./opengl-profiles.md)
  Constants that specify the functionality provided by the renderer.
### Initializers
- [init?(CGLPixelFormatObj: CGLPixelFormatObj)](./nsopenglpixelformat/init%28cglpixelformatobj%29-6et9a.md)
- [init?(coder: NSCoder)](./nsopenglpixelformat/init%28coder%29.md)
### Managing Attributes
- [- attributes](./nsopenglpixelformat/attributes.md)
  The attribute data for the pixel format object.
- [- setAttributes:](./nsopenglpixelformat/setattributes_.md)
  Sets the attribute data for the pixel format object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated classes
- [class NSOpenGLView](./nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](./nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](./nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat)*