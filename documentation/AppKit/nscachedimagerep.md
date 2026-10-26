# NSCachedImageRep

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that stores image data in a form that can be readily transferred to the screen.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
@interface NSCachedImageRep : NSImageRep
```

#### Overview

An [`NSCachedImageRep`](./nscachedimagerep.md) object differs from other image representation objects in that it simply stores the already rendered image, whereas other image representation objects generally have knowledge about how to render the image from source data.

You typically do not use this class directly. Instead, [`NSImage`](./nsimage.md) and its other image representation objects create instances of [`NSCachedImageRep`](./nscachedimagerep.md) as needed to cache versions of the rendered image. This caching speeds up screen-based drawing for existing images during subsequent rendering operations. Cached image representations are also used to capture drawing commands for images created programmatically by locking focus on an image.

## Topics

### Initializing Cached Representations of Images
- [- initWithSize:depth:separate:alpha:](./nscachedimagerep/initwithsize_depth_separate_alpha_.md)
  Returns a cached image representation initialized with the specified image characteristics.
- [- initWithWindow:rect:](./nscachedimagerep/initwithwindow_rect_.md)
  Returns a cached image representation initialized for drawing in the specified window.
### Getting Data
- [- rect](./nscachedimagerep/rect.md)
  Returns the rectangle where the representation is cached.
- [- window](./nscachedimagerep/window.md)
  Returns the window where the representation is cached.

## Relationships

### Inherits From
- [NSImageRep](./nsimagerep.md)

## See Also

### Deprecated classes
- [class NSOpenGLView](./nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](./nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](./nsopengllayer.md)
  A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.
- [NSOpenGLPixelBuffer](./nsopenglpixelbuffer.md)
  An object that provides access to accelerated offscreen rendering.
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
- [NSInputManager](./nsinputmanager.md)
- [NSInputServer](./nsinputserver.md)
- [NSMovie](./nsmovie.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscachedimagerep)*