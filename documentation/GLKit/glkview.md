# GLKView

**Framework**: GLKit  
**Kind**: class  
**Role**: Class

A default implementation for views that draw their content using OpenGL ES.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class GLKView
```

```objc
@interface GLKView : UIView
```

## Overview

The [`GLKView`](./glkview.md) class simplifies the effort required to create an OpenGL ES application by  directly managing a framebuffer object on your behalf; your application simply needs to draw into the framebuffer when the contents need to be updated.

To use this class in your application, create a new [`GLKView`](./glkview.md) object and provide it an OpenGL ES context. Then, modify the view’s [`drawableColorFormat`](./glkview/drawablecolorformat.md), [`drawableDepthFormat`](./glkview/drawabledepthformat.md), [`drawableStencilFormat`](./glkview/drawablestencilformat.md), and [`drawableMultisample`](./glkview/drawablemultisample.md) properties to configure the format of the drawable’s framebuffer object. After this, the view automatically creates or updates the framebuffer object whenever the view must be redrawn. A [`GLKView`](./glkview.md) object uses the regular view drawing cycle for a [`UIView`](../UIKit/uiview.md)object, calling its [`draw(_:)`](../UIKit/uiview/draw%28_%29.md) method whenever the contents of the view need to be updated. Before calling its `draw `method, the view makes its [`EAGLContext`](../OpenGLES/eaglcontext.md) object the current OpenGL ES context and binds its framebuffer object to the OpenGL ES context as the target for rendering commands. Your application’s implementation of the `draw` method should call one or more OpenGL ES functions to render an image into the framebuffer object. Then, the view resolves any multisampling that you may have enabled and delivers the finished results.

> ❗ **Important**:  Your drawing method should only modify the contents of the framebuffer object. Never attempt to read the pixel information from the underlying framebuffer object, modify or dispose of the framebuffer object, or read its other properties by calling OpenGL ES functions. Instead, rely on the properties and methods provided by the [`GLKView`](./glkview.md) class.

The [`GLKView`](./glkview.md) class can be used in conjunction with a [`GLKViewController`](./glkviewcontroller.md) object to create an animation rendering loop that redraws the contents of the view at a specified frame rate.

### Subclassing Notes

Typically, there is no need to subclass the [`GLKView`](./glkview.md) class. Instead, provide a delegate object to draw the view’s contents. See [`GLKViewDelegate`](./glkviewdelegate.md).

## Topics

### Initializing the View
- [init(frame: CGRect, context: EAGLContext)](./glkview/init%28frame,context%29.md)
  Initializes a new view.
### Delegate
- [var delegate: (any GLKViewDelegate)?](./glkview/delegate.md)
  The view’s delegate.
### Configuring the Framebuffer Object
- [var drawableColorFormat: GLKViewDrawableColorFormat](./glkview/drawablecolorformat.md)
  The format of the color renderbuffer.
- [var drawableDepthFormat: GLKViewDrawableDepthFormat](./glkview/drawabledepthformat.md)
  The format of the depth renderbuffer
- [var drawableStencilFormat: GLKViewDrawableStencilFormat](./glkview/drawablestencilformat.md)
  The format of the stencil renderbuffer.
- [var drawableMultisample: GLKViewDrawableMultisample](./glkview/drawablemultisample.md)
  The format of the multisampling buffer.
### Read-only Framebuffer Properties
- [var drawableHeight: Int](./glkview/drawableheight.md)
  The height, in pixels, of the underlying framebuffer object.
- [var drawableWidth: Int](./glkview/drawablewidth.md)
  The width, in pixels, of the underlying framebuffer object.
### Drawing Your View’s Contents
- [var context: EAGLContext](./glkview/context.md)
  The OpenGL ES context used when drawing the view’s contents.
- [func bindDrawable()](./glkview/binddrawable%28%29.md)
  Binds the underlying framebuffer object to OpenGL ES.
- [var enableSetNeedsDisplay: Bool](./glkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to messages that invalidate the view’s contents.
- [func display()](./glkview/display%28%29.md)
  Redraws the view’s contents immediately.
- [var snapshot: UIImage](./glkview/snapshot.md)
  Draws the contents of the view and returns them as a new image object.
### Deleting the View’s Underlying Framebuffer Object
- [func deleteDrawable()](./glkview/deletedrawable%28%29.md)
  Deletes the drawable object associated with the view.
### Constants
- [enum GLKViewDrawableColorFormat](./glkviewdrawablecolorformat.md)
  The format of the color renderbuffer.
- [enum GLKViewDrawableDepthFormat](./glkviewdrawabledepthformat.md)
  The format of the depth renderbuffer.
- [enum GLKViewDrawableStencilFormat](./glkviewdrawablestencilformat.md)
  The format of the stencil renderbuffer.
- [enum GLKViewDrawableMultisample](./glkviewdrawablemultisample.md)
  The format of the multisampling buffer.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### OpenGL ES View Rendering
- [protocol GLKViewDelegate](./glkviewdelegate.md)
  Drawing callback methods for use with a [`GLKView`](./glkview.md) object.
- [class GLKViewController](./glkviewcontroller.md)
  A view controller that manages an OpenGL ES rendering loop.
- [protocol GLKViewControllerDelegate](./glkviewcontrollerdelegate.md)
  Rendering loop callback methods for use with a [`GLKViewController`](./glkviewcontroller.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview)*