# CAOpenGLLayer

**Framework**: Core Animation  
**Kind**: class  
**Role**: Class

A layer that provides a layer suitable for rendering OpenGL content.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class CAOpenGLLayer
```

```objc
@interface CAOpenGLLayer : CALayer
```

#### Overview

To provide OpenGL content you subclass `CAOpenGLLayer` and override [`draw(inCGLContext:pixelFormat:forLayerTime:displayTime:)`](./caopengllayer/draw%28incglcontext,pixelformat,forlayertime,displaytime%29.md). You can specify that the OpenGL content is static by setting the [`isAsynchronous`](./caopengllayer/isasynchronous.md) property to [`false`](../Swift/false.md).

## Topics

### Determining Layer Properties
- [var colorspace: CGColorSpace?](./caopengllayer/colorspace.md)
  The layer’s colorspace in Core Graphics.
- [var wantsExtendedDynamicRangeContent: Bool](./caopengllayer/wantsextendeddynamicrangecontent.md)
  Tells whether or not the layer supports content with extended dynamic range.
### Drawing Layer Content
- [var isAsynchronous: Bool](./caopengllayer/isasynchronous.md)
  Determines when the contents of the layer are updated.
- [func canDraw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?) -> Bool](./caopengllayer/candraw%28incglcontext,pixelformat,forlayertime,displaytime%29.md)
  Returns whether the receiver should draw OpenGL content for the specified time.
- [func draw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?)](./caopengllayer/draw%28incglcontext,pixelformat,forlayertime,displaytime%29.md)
  Draws the OpenGL content for the specified time.
### Managing Pixel Format
- [func copyCGLPixelFormat(forDisplayMask: UInt32) -> CGLPixelFormatObj](./caopengllayer/copycglpixelformat%28fordisplaymask%29.md)
  Returns the OpenGL pixel format suitable for rendering to the set of displays specified by the display mask.
- [func releaseCGLPixelFormat(CGLPixelFormatObj)](./caopengllayer/releasecglpixelformat%28_%29.md)
  Releases the specified OpenGL pixel format object.
### Managing the Rendering Context
- [func copyCGLContext(forPixelFormat: CGLPixelFormatObj) -> CGLContextObj](./caopengllayer/copycglcontext%28forpixelformat%29.md)
  Returns the rendering context the receiver requires for the specified pixel format.
- [func releaseCGLContext(CGLContextObj)](./caopengllayer/releasecglcontext%28_%29.md)
  Releases the specified rendering context.

## Relationships

### Inherits From
- [CALayer](./calayer.md)
### Conforms To
- [CAMediaTiming](./camediatiming.md)
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

### Metal and OpenGL
- [class CAMetalLayer](./cametallayer.md)
  A Core Animation layer that Metal can render into, typically displayed onscreen.
- [protocol CAMetalDrawable](./cametaldrawable.md)
  A Metal drawable associated with a Core Animation layer.
- [class CAEAGLLayer](./caeagllayer.md)
  A layer that supports drawing OpenGL content in iOS and tvOS applications.
- [class CAEDRMetadata](./caedrmetadata.md)
  Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [class CARenderer](./carenderer.md)
  A layer that allows an application to render a layer tree into a Core OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer)*