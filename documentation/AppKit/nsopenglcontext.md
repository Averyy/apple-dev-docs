# NSOpenGLContext

**Framework**: AppKit  
**Kind**: class

An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSOpenGLContext
```

#### Overview

An OpenGL context is created using an [`NSOpenGLPixelFormat`](nsopenglpixelformat.md)object that specifies the context’s buffer types and other attributes. A context can be full-screen, offscreen, or associated with an [`NSView`](nsview.md) object. A context draws into its , which is the frame buffer that is the target of OpenGL drawing operations.

Every [`NSOpenGLContext`](nsopenglcontext.md) object wraps a low-level, platform-specific Core OpenGL (CGL) context. Your application can retrieve the CGL context by calling the [`cglContextObj`](nsopenglcontext/cglcontextobj.md) method. For more information on the underling CGL context, see `CGL`.

## Topics

### Creating Contexts
- [init?(format: NSOpenGLPixelFormat, share: NSOpenGLContext?)](nsopenglcontext/init(format:share:).md)
  Returns an OpenGL context object initialized with the specified pixel format information.
- [init?(cglContextObj: CGLContextObj)](nsopenglcontext/init(cglcontextobj:).md)
  Initializes and returns an OpenGL context object using an existing CGL context.
### Managing the Current Context
- [class func clearCurrentContext()](nsopenglcontext/clearcurrentcontext.md)
  Clears the current context.
- [class var current: NSOpenGLContext?](nsopenglcontext/current.md)
  Returns the current OpenGL graphics context.
- [func makeCurrentContext()](nsopenglcontext/makecurrentcontext.md)
  Sets the context as the current OpenGL context object.
### Managing the Drawable Object
- [var view: NSView?](nsopenglcontext/view.md)
  Returns the OpenGL context’s view.
- [func clearDrawable()](nsopenglcontext/cleardrawable.md)
  Disassociates the OpenGL context from its viewport.
- [func update()](nsopenglcontext/update.md)
  Updates the OpenGL context’s drawable object.
### Flushing the Drawing Buffer
- [func flushBuffer()](nsopenglcontext/flushbuffer.md)
  Copies the back buffer to the front buffer of the OpenGL context.
### Context Parameter Handling
- [func setValues(UnsafePointer<GLint>, for: NSOpenGLContext.Parameter)](nsopenglcontext/setvalues(_:for:).md)
  Sets the value of the specified parameter.
- [func getValues(UnsafeMutablePointer<GLint>, for: NSOpenGLContext.Parameter)](nsopenglcontext/getvalues(_:for:).md)
  Returns the value of the requested parameter.
### Working with Virtual Screens
- [var currentVirtualScreen: GLint](nsopenglcontext/currentvirtualscreen.md)
  Returns the current virtual screen for the OpenGL context.
### Getting the CGL Context Object
- [var cglContextObj: CGLContextObj?](nsopenglcontext/cglcontextobj.md)
  Returns the low-level, platform-specific Core OpenGL (CGL) context object represented by the receiver.
### Getting the Pixel Format
- [var pixelFormat: NSOpenGLPixelFormat](nsopenglcontext/pixelformat.md)
  The pixel format of the OpenGL context.
### Getting the OpenGL Version
- [static var openGLVersion: (major: GLint, minor: GLint)](nsopenglcontext/openglversion.md)
  The version of OpenGL.
### Constants
- [NSOpenGLContext.Parameter](nsopenglcontext/parameter.md)
  Constants that specify context parameters.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSLocking](../Foundation/NSLocking.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSOpenGLView](nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLLayer](nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
- [class NSOpenGLPixelFormat](nsopenglpixelformat.md)
  An object that specifies the types of buffers and other attributes of the OpenGL context.
- [class NSDrawer](nsdrawer.md)
  A user interface element that contains and displays text, scroll, and browser views, in addition to other view subclasses.
- [class NSForm](nsform.md)
  An `NSForm` object is a vertical matrix of [`NSFormCell`](nsformcell.md) objects to implement the fields.
- [class NSFormCell](nsformcell.md)
  The `NSFormCell` class is used to implement text entry fields in a form. The left part of an `NSFormCell` object contains a title. The right part contains an editable text entry field.
- [class NSMenuItemCell](nsmenuitemcell.md)
  An object that handles the measurement and display of a single menu item in its encompassing frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext)*