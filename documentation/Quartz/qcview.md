# QCView

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

The `QCView` class is a custom `NSView` class that loads, plays, and controls Quartz Composer compositions. It is an autonomous view that is driven by an internal timer running on the main thread.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class QCView
```

```objc
@interface QCView : NSView
```

## Overview

The view can be set to render a composition automatically when it is placed onscreen. The view stops rendering when it is placed offscreen. When not rendering, the view is filled with the current erase color. The rendered composition automatically synchronizes to the vertical retrace of the monitor.

When you archive a `QCView` object, it saves the composition that’s loaded at the time the view is archived.

If you want to perform custom operations while a composition is rendering such as setting input parameters or drawing OpenGL content, you need to subclass `QCView` and implement the [`render(atTime:arguments:)`](./qcview/render%28attime,arguments%29.md) method.

## Topics

### Performing Custom Operations During Rendering
- [func render(atTime: TimeInterval, arguments: [AnyHashable : Any]!) -> Bool](./qcview/render%28attime,arguments%29.md)
  Overrides to perform  your custom operations prior to or after rendering a frame of a composition.
### Loading a Composition
- [func loadComposition(fromFile: String!) -> Bool](./qcview/loadcomposition%28fromfile%29.md)
  Loads the composition file located at the specified path.
- [func load(QCComposition!) -> Bool](./qcview/load%28_%29.md)
  Loads a [`QCComposition`](./qccomposition.md) object into the view.
- [func loadedComposition() -> QCComposition!](./qcview/loadedcomposition%28%29.md)
  Returns the composition loaded in the view.
- [func unloadComposition()](./qcview/unloadcomposition%28%29.md)
  Unloads the composition from the view.
### Managing the Erase Color
- [func erase()](./qcview/erase%28%29.md)
  Clears the view using the current erase color.
- [func eraseColor() -> NSColor!](./qcview/erasecolor%28%29.md)
  Retrieves the current color used to erase the view.
- [func setEraseColor(NSColor!)](./qcview/seterasecolor%28_%29.md)
  Sets the color used to erase the view.
### Setting and Getting Event Masks
- [func eventForwardingMask() -> Int](./qcview/eventforwardingmask%28%29.md)
  Retrieves the mask used to filter which types of events are forwarded from the view to the composition during rendering.
- [func setEventForwardingMask(Int)](./qcview/seteventforwardingmask%28_%29.md)
  Sets the mask used to filter which types of events are forwarded from the view to the composition during rendering.
### Setting and Getting the Maximum Frame Rate
- [func maxRenderingFrameRate() -> Float](./qcview/maxrenderingframerate%28%29.md)
  Returns the maximum frame rate for rendering.
- [func setMaxRenderingFrameRate(Float)](./qcview/setmaxrenderingframerate%28_%29.md)
  Sets the maximum rendering frame rate.
### Managing Rendering
- [func startRendering() -> Bool](./qcview/startrendering%28%29.md)
  Starts rendering the composition that is in the view.
- [func isRendering() -> Bool](./qcview/isrendering%28%29.md)
  Checks whether a composition is rendering in the view.
- [func autostartsRendering() -> Bool](./qcview/autostartsrendering%28%29.md)
  Checks whether the view is set to start rendering automatically.
- [func setAutostartsRendering(Bool)](./qcview/setautostartsrendering%28_%29.md)
  Sets whether the composition that is in the view starts rendering automatically when the view is put on the screen.
- [func stopRendering()](./qcview/stoprendering%28%29.md)
  Stops rendering the composition that is in the view.
- [func pauseRendering()](./qcview/pauserendering%28%29.md)
  Pauses rendering in the view.
- [func isPausedRendering() -> Bool](./qcview/ispausedrendering%28%29.md)
  Returns whether or not the rendering in the view is paused.
- [func resumeRendering()](./qcview/resumerendering%28%29.md)
  Resumes rendering a paused composition.
### Using Interface Builder
- [func play(Any!)](./qcview/play%28_%29.md)
  Plays or pauses a composition in a view.
- [func start(Any!)](./qcview/start%28_%29.md)
  Starts rendering a composition in a view.
- [func stop(Any!)](./qcview/stop%28_%29.md)
  Stops rendering a composition in a view.
### Taking Snapshot Images
- [func snapshotImage() -> NSImage!](./qcview/snapshotimage%28%29.md)
  Returns an `NSImage` object of the current image in the view.
- [func createSnapshotImage(ofType: String!) -> Any!](./qcview/createsnapshotimage%28oftype%29.md)
  Returns the current image in the view as an image object of the provided image type.
### Working With OpenGL
- [func openGLContext() -> NSOpenGLContext!](./qcview/openglcontext%28%29.md)
  Returns the OpenGL context used by the view.
- [func openGLPixelFormat() -> NSOpenGLPixelFormat!](./qcview/openglpixelformat%28%29.md)
  Returns the OpenGL pixel format used by the view.
### Notifications
- [QCViewDidStartRenderingNotification](./qcviewdidstartrenderingnotification.md)
  Posted when the view starts rendering.
- [QCViewDidStopRenderingNotification](./qcviewdidstoprenderingnotification.md)
  Posted when the view stops rendering.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [QCCompositionRenderer](./qccompositionrenderer.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class QCComposition](./qccomposition.md)
  The `QCComposition` class represents a Quartz Composer composition that either:
- [class QCCompositionLayer](./qccompositionlayer.md)
  A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.
- [class QCCompositionParameterView](./qccompositionparameterview.md)
  A class that allows users to edit the input parameters of a composition in real time. The composition can be rendering in any of the following objects: [`QCRenderer`](./qcrenderer.md), [`QCView`](./qcview.md), or [`QCCompositionLayer`](./qccompositionlayer.md).
- [class QCCompositionPickerPanel](./qccompositionpickerpanel.md)
  The `QCCompositionPickerPanel` class represents a utility window that allows users to browse compositions that are in the Quartz Composer composition repository and, if supported, preview the composition. The `QCCompositionPickerPanel` class cannot be subclassed.
- [class QCCompositionPickerView](./qccompositionpickerview.md)
  The `QCCompositionPickerView` class allows users to browse compositions that are in the Quartz Composer composition repository, and to preview them. You can set the default input parameters for a composition preview  by using the method setDefaultValue:forInputKey:.
- [class QCCompositionRepository](./qccompositionrepository.md)
  The `QCCompositionRepository` class represents a system-wide centralized repository of built-in and installed Quartz Composer compositions (`/Library/Compositions` and `~/Library/Compositions`). The `QCCompositionRepository` class cannot be subclassed.
- [class QCPatchController](./qcpatchcontroller.md)
- [class QCPlugIn](./qcplugin.md)
  A base class to subclass for writing custom patches.
- [class QCPlugInViewController](./qcpluginviewcontroller.md)
  The `QCPlugInViewController` class communicates (through Cocoa bindings) between a custom patch and the view used for the internal settings of the custom patch. Only custom patches that use internal settings exposed to the user need to use the `QCPlugInViewController` class.
- [class QCRenderer](./qcrenderer.md)
  A base class for low-level rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview)*