# NSOpenGLView

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A view that displays OpenGL content in a view.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use MTKView instead.

## Declaration

```swift
class NSOpenGLView
```

```objc
@interface NSOpenGLView : NSView
```

## Overview

An [`NSOpenGLView`](./nsopenglview.md) object maintains an [`NSOpenGLPixelFormat`](./nsopenglpixelformat.md) and [`NSOpenGLContext`](./nsopenglcontext.md) object into which OpenGL calls can be rendered. The view provides methods for accessing and managing the [`NSOpenGLPixelFormat`](./nsopenglpixelformat.md) and [`NSOpenGLContext`](./nsopenglcontext.md) objects, as well as notifications of visible region changes.

An `NSOpenGLView` object cannot have subviews. You can, however, divide a single `NSOpenGLView` into multiple rendering areas using the `glViewport` function.

When creating an `NSOpenGLView` object in Interface Builder, you use the inspector window to specify the pixel format attributes you want for the view. Only those attributes listed in the Interface Builder inspector are set when the view is instantiated.

> **Note**:  In versions of the Xcode Tools that shipped prior to OS X v10.4, the Interface Builder inspector does not list any pixel format attributes for `NSOpenGLView`.

## Topics

### Initializing an NSOpenGLView
- [init?(frame: NSRect, pixelFormat: NSOpenGLPixelFormat?)](./nsopenglview/init%28frame,pixelformat%29.md)
  Returns an `NSOpenGLView` object initialized with the specified frame rectangle and pixel format.
### Managing the NSOpenGLPixelFormat
- [class func defaultPixelFormat() -> NSOpenGLPixelFormat](./nsopenglview/defaultpixelformat%28%29.md)
  Returns a default [`NSOpenGLPixelFormat`](./nsopenglpixelformat.md) object.
- [var pixelFormat: NSOpenGLPixelFormat?](./nsopenglview/pixelformat.md)
  The [`NSOpenGLPixelFormat`](./nsopenglpixelformat.md) object associated with the receiver.
### Managing the NSOpenGLContext
- [func prepareOpenGL()](./nsopenglview/prepareopengl%28%29.md)
  Used by subclasses to initialize OpenGL state.
- [func clearGLContext()](./nsopenglview/clearglcontext%28%29.md)
  Releases the [`NSOpenGLContext`](./nsopenglcontext.md) object associated with the view.
- [var openGLContext: NSOpenGLContext?](./nsopenglview/openglcontext.md)
  The [`NSOpenGLContext`](./nsopenglcontext.md) object associated with the receiver.
### Managing the Visible Region
- [func reshape()](./nsopenglview/reshape%28%29.md)
  Called by Cocoa when the view’s visible rectangle or bounds change.
- [func update()](./nsopenglview/update%28%29.md)
  Called by Cocoa when the view’s window moves or when the view itself moves or is resized.
### Extended Dynamic Range
- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](./nsopenglview/wantsextendeddynamicrangeopenglsurface.md)
  Enables extended dynamic range values on the screen.
### Instance Properties
- [var wantsBestResolutionOpenGLSurface: Bool](./nsopenglview/wantsbestresolutionopenglsurface.md)
  A Boolean value indicating whether the view wants an OpenGL backing surface with a resolution greater than 1 pixel per point.
- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](./nsopenglview/wantsextendeddynamicrangeopenglsurface.md)
  Enables extended dynamic range values on the screen.

## Relationships

### Inherits From
- [NSView](./nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](./nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated classes
- [class NSOpenGLContext](./nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview)*