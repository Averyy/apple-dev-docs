# NSOpenGLLayer

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A subclass of `CAOpenGLLayer` that is suitable for rendering OpenGL into layers.

**Availability**:
- macOS 10.6+ - Deprecated in 10.14

> **Deprecated**: The OpenGL API is deprecated. Use [Metal](../Metal/Metal.md) and [MetalKit](../MetalKit/MetalKit.md) instead.

## Declaration

```swift
class NSOpenGLLayer
```

```objc
@interface NSOpenGLLayer : CAOpenGLLayer
```

## Overview

Unlike [`CAOpenGLLayer`](../QuartzCore/caopengllayer.md), [`NSOpenGLLayer`](./nsopengllayer.md) uses AppKit types.

## Topics

### Drawing the Content
- [func canDraw(in: NSOpenGLContext, pixelFormat: NSOpenGLPixelFormat, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>) -> Bool](./nsopengllayer/candraw%28in,pixelformat,forlayertime,displaytime%29.md)
  Invoked to ask the layer whether it can (or should) draw.
- [func draw(in: NSOpenGLContext, pixelFormat: NSOpenGLPixelFormat, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>)](./nsopengllayer/draw%28in,pixelformat,forlayertime,displaytime%29.md)
  Draws the OpenGL content for the specified time.
### Managing the Pixel Format
- [var openGLPixelFormat: NSOpenGLPixelFormat?](./nsopengllayer/openglpixelformat.md)
  Provides access to the layer’s associated OpenGL pixel format.
- [func openGLPixelFormat(forDisplayMask: UInt32) -> NSOpenGLPixelFormat](./nsopengllayer/openglpixelformat%28fordisplaymask%29.md)
  Returns the OpenGL pixel format suitable for the specified displays.
### Managing the Rendering Context
- [var openGLContext: NSOpenGLContext?](./nsopengllayer/openglcontext.md)
  The layer’s OpenGL context.
- [func openGLContext(for: NSOpenGLPixelFormat) -> NSOpenGLContext](./nsopengllayer/openglcontext%28for%29.md)
  Returns the OpenGL context to use for the requested pixel format.
### Accessing the Associated View
- [var view: NSView?](./nsopengllayer/view.md)
  Returns the view associated with the layer.

## Relationships

### Inherits From
- [CAOpenGLLayer](../QuartzCore/caopengllayer.md)
### Conforms To
- [CAMediaTiming](../QuartzCore/camediatiming.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated classes
- [class NSOpenGLView](./nsopenglview.md)
  A view that displays OpenGL content in a view.
- [class NSOpenGLContext](./nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer)*