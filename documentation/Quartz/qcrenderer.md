# QCRenderer

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

A base class for low-level rendering.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class QCRenderer
```

```objc
@interface QCRenderer : NSObject
```

## Overview

A `QCRenderer` class is designed for low-level rendering of Quartz Composer compositions. This is the class to use if you want to be in charge of rendering a composition to a specific OpenGL context—either using the [`NSOpenGLContext`](../AppKit/nsopenglcontext.md) class or a `CGLContextObj` object. `QCRenderer` also allows you to load, play, and control a composition.

To render a composition to a specific OpenGL context:

- Create an instance of `QCRenderer` using one of the initialization methods, such as [`init(openGLContext:pixelFormat:file:)`](./qcrenderer/init%28openglcontext,pixelformat,file%29.md).
- Render frames by calling the method [`render(atTime:arguments:)`](./qcrenderer/render%28attime,arguments%29.md)
- If you use double buffering in OpenGL, you must swap the OpenGL buffers.
- Release the renderer when you no longer need it.

This code snippet shows how to implement these tasks:

```objc
NSOpenGLContext*     context = [myNSOpenGLView openGLContext];
NSOpenGLPixelFormat*  format = [myNSOpenGLView pixelFormat];
NSString*               path = @"/Users/MyName/MyComposition.qtz";
QCRenderer* myRenderer;
// Create a Quartz Composer renderer.
myRenderer = [[QCRenderer alloc] initWithOpenGLContext:context
                                           pixelFormat:format
                                                  file:path];
// Render the first 10 seconds of the composition with steps of 1/25s.
for(double t = 0.0; t <= 10.0; t += 1.0/25.0)
{
  [myRenderer renderAtTime:t arguments:nil];
  [context flushBuffer]; //Required on double-buffered contexts
}
// Clean up
 [renderer release];
```

## Topics

### Creating and Initializing a Renderer
- [init!(composition: QCComposition!, colorSpace: CGColorSpace!)](./qcrenderer/init%28composition,colorspace%29.md)
  Creates a  renderer object  with a composition object and a color space.
- [init!(openGLContext: NSOpenGLContext!, pixelFormat: NSOpenGLPixelFormat!, file: String!)](./qcrenderer/init%28openglcontext,pixelformat,file%29.md)
  Creates a  renderer object with an `NSOpenGLContext` object and a composition file.
- [init!(cglContext: CGLContextObj!, pixelFormat: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)](./qcrenderer/init%28cglcontext,pixelformat,colorspace,composition%29-7at42.md)
  Creates a  renderer object  with a `CGLContextObj` object, a pixel format, a color space, and a composition object.
- [init!(offScreenWith: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)](./qcrenderer/init%28offscreenwith,colorspace,composition%29.md)
  Creates an offscreen renderer of a given size with the provided color space and composition object.
### Rendering a Composition
- [func render(atTime: TimeInterval, arguments: [AnyHashable : Any]!) -> Bool](./qcrenderer/render%28attime,arguments%29.md)
  Renders a frame of a composition at the specified time.
### Getting the Composition Object
- [func composition() -> QCComposition!](./qcrenderer/composition%28%29.md)
  Returns the composition object associated with the renderer.
### Taking Snapshot Images
- [func snapshotImage() -> NSImage!](./qcrenderer/snapshotimage%28%29.md)
  Returns an `NSImage` object of the current image in the OpenGL context associated with the renderer.
- [func createSnapshotImage(ofType: String!) -> Any!](./qcrenderer/createsnapshotimage%28oftype%29.md)
  Returns the current image in the OpenGL context associated with the renderer, as an image object of the provided image type.
### Constants
- [Rendering Arguments](./rendering-arguments.md)
  Arguments that you can pass to the [`render(atTime:arguments:)`](./qcrenderer/render%28attime,arguments%29.md) method.
### Initializers
- [init!(CGLContext: CGLContextObj!, pixelFormat: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)](./qcrenderer/init%28cglcontext,pixelformat,colorspace,composition%29-8rq7j.md)
- [init!(offScreenWithSize: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)](./qcrenderer/init%28offscreenwithsize,colorspace,composition%29.md)
### Instance Methods
- [func renderingTime(forTime: TimeInterval, arguments: [AnyHashable : Any]!) -> TimeInterval](./qcrenderer/renderingtime%28fortime,arguments%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [QCCompositionRenderer](./qccompositionrenderer.md)

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
- [class QCView](./qcview.md)
  The `QCView` class is a custom `NSView` class that loads, plays, and controls Quartz Composer compositions. It is an autonomous view that is driven by an internal timer running on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer)*