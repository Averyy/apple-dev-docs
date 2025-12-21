# NSOpenGLPixelFormat

**Framework**: AppKit  
**Kind**: class

An object that specifies the types of buffers and other attributes of the OpenGL context.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSOpenGLPixelFormat
```

#### Overview

To render with OpenGL into an [`NSOpenGLContext`](nsopenglcontext.md), you must specify the context’s pixel format.

Every [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object wraps a low-level, platform-specific Core OpenGL (CGL) pixel format object. Your application can retrieve the CGL pixel format object by calling the [`cglPixelFormatObj`](nsopenglpixelformat/cglpixelformatobj.md) method. For more information on the underling CGL pixel format object, see `CGL`.

## Topics

### Creating an OpenGL Pixel Format
- [init?(cglPixelFormatObj: CGLPixelFormatObj)](nsopenglpixelformat/init(cglpixelformatobj:).md)
  Returns an OpenGL pixel format object initialized with using an existing CGL pixel format object.
- [convenience init?(attributes: UnsafePointer<NSOpenGLPixelFormatAttribute>)](nsopenglpixelformat/init(attributes:).md)
  Returns an OpenGL pixel format object initialized with specified pixel format attributes.
### Managing the Pixel Format
- [var cglPixelFormatObj: CGLPixelFormatObj?](nsopenglpixelformat/cglpixelformatobj.md)
  The low-level, platform-specific Core OpenGL (CGL) pixel format object represented by the receiver.
- [func getValues(UnsafeMutablePointer<GLint>, forAttribute: NSOpenGLPixelFormatAttribute, forVirtualScreen: GLint)](nsopenglpixelformat/getvalues(_:forattribute:forvirtualscreen:).md)
  Gets the value for the specified pixel format attribute.
- [var numberOfVirtualScreens: GLint](nsopenglpixelformat/numberofvirtualscreens.md)
  The number of virtual screens associated with the OpenGL pixel format.
### Constants
- [typealias NSOpenGLPixelFormatAttribute](nsopenglpixelformatattribute.md)
  Pixel format attributes for OpenGL.
- [OpenGL Pixel Format Attributes](opengl-pixel-format-attributes.md)
  Pixel format attributes for OpenGL.
- [OpenGL Profiles](opengl-profiles.md)
  Constants that specify the functionality provided by the renderer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSOpenGLView](nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
- [class NSDrawer](nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSForm](nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](nsformcell.md) objects to implement the fields.
- [class NSFormCell](nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat)*