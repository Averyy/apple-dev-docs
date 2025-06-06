# NSOpenGLView

**Framework**: Appkit  
**Kind**: class

A view that displays OpenGL content in a view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
class NSOpenGLView
```

#### Overview

An [`NSOpenGLView`](nsopenglview.md) object maintains an [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) and [`NSOpenGLContext`](nsopenglcontext.md) object into which OpenGL calls can be rendered. The view provides methods for accessing and managing the [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) and [`NSOpenGLContext`](nsopenglcontext.md) objects, as well as notifications of visible region changes.

An `NSOpenGLView` object cannot have subviews. You can, however, divide a single `NSOpenGLView` into multiple rendering areas using the `glViewport` function.

When creating an `NSOpenGLView` object in Interface Builder, you use the inspector window to specify the pixel format attributes you want for the view. Only those attributes listed in the Interface Builder inspector are set when the view is instantiated.

> **Note**:  In versions of the Xcode Tools that shipped prior to OS X v10.4, the Interface Builder inspector does not list any pixel format attributes for `NSOpenGLView`.

## Topics

### Initializing an NSOpenGLView
- [init?(frame: NSRect, pixelFormat: NSOpenGLPixelFormat?)](nsopenglview/init(frame:pixelformat:).md)
  Returns an `NSOpenGLView` object initialized with the specified frame rectangle and pixel format.
### Managing the NSOpenGLPixelFormat
- [class func defaultPixelFormat() -> NSOpenGLPixelFormat](nsopenglview/defaultpixelformat.md)
  Returns a default [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object.
- [var pixelFormat: NSOpenGLPixelFormat?](nsopenglview/pixelformat.md)
  The [`NSOpenGLPixelFormat`](nsopenglpixelformat.md) object associated with the receiver.
### Managing the NSOpenGLContext
- [func prepareOpenGL()](nsopenglview/prepareopengl.md)
  Used by subclasses to initialize OpenGL state.
- [func clearGLContext()](nsopenglview/clearglcontext.md)
  Releases the [`NSOpenGLContext`](nsopenglcontext.md) object associated with the view.
- [var openGLContext: NSOpenGLContext?](nsopenglview/openglcontext.md)
  The [`NSOpenGLContext`](nsopenglcontext.md) object associated with the receiver.
### Managing the Visible Region
- [func reshape()](nsopenglview/reshape.md)
  Called by Cocoa when the view’s visible rectangle or bounds change.
- [func update()](nsopenglview/update.md)
  Called by Cocoa when the view’s window moves or when the view itself moves or is resized.
### Extended Dynamic Range
- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](nsopenglview/wantsextendeddynamicrangeopenglsurface.md)
  Enables extended dynamic range values on the screen.
### Instance Properties
- [var wantsBestResolutionOpenGLSurface: Bool](nsopenglview/wantsbestresolutionopenglsurface.md)
  A Boolean value indicating whether the view wants an OpenGL backing surface with a resolution greater than 1 pixel per point.
- [var wantsExtendedDynamicRangeOpenGLSurface: Bool](nsopenglview/wantsextendeddynamicrangeopenglsurface.md)
  Enables extended dynamic range values on the screen.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSOpenGLContext](nsopenglcontext.md)
  An object that represents an OpenGL graphics context, into which all OpenGL calls are rendered.
- [class NSOpenGLLayer](nsopengllayer.md)
  A subclass of [`CAOpenGLLayer`](https://developer.apple.com/documentation/QuartzCore/CAOpenGLLayer) that is suitable for rendering OpenGL into layers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nsopenglview)*