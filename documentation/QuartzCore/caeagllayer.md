# CAEAGLLayer

**Framework**: Core Animation  
**Kind**: class  
**Role**: Class

A layer that supports drawing OpenGL content in iOS and tvOS applications.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES is deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class CAEAGLLayer
```

```objc
@interface CAEAGLLayer : CALayer
```

#### Overview

If you plan to use OpenGL for your rendering, use this class as the backing layer for your views by returning it from your view’s [`layerClass`](../UIKit/uiview/layerclass.md) class method. The returned [`CAEAGLLayer`](./caeagllayer.md) object is a wrapper for a Core Animation surface that is fully compatible with OpenGL ES function calls.

Prior to designating the layer’s associated view as the render target for a graphics context, you can change the rendering attributes you want using the [`drawableProperties`](../OpenGLES/eagldrawable/drawableproperties.md) property. This property lets you configure the color format for the rendering surface and whether the surface retains its contents. For a list of keys (and corresponding values) you can include in this dictionary (along with their default values), see the [`EAGLDrawable`](../OpenGLES/eagldrawable.md).

Because an OpenGL ES rendering surface is presented to the user using Core Animation, any effects and animations you apply to the layer affect the 3D content you render. However, for best performance, do the following:

- Set the layer’s opaque attribute to `TRUE`.
- Set the layer bounds to match the dimensions of the display.
- Make sure the layer is not transformed.
- Avoid drawing other layers on top of the `CAEAGLLayer` object. If you must draw other, non OpenGL content, you might find the performance cost acceptable if you place transparent 2D content on top of the GL content and also make sure that the OpenGL content is opaque and not transformed.
- When drawing landscape content on a portrait display, you should rotate the content yourself rather than using the `CAEAGLLayer` transform to rotate it.

## Topics

### Accessing the Layer Properties
- [var drawableProperties: [String : Any]?](../OpenGLES/eagldrawable/drawableproperties.md)
  A dictionary of values that specify the desired characteristics of the drawable surface.
- [var presentsWithTransaction: Bool](./caeagllayer/presentswithtransaction.md)
  A Boolean value that determines whether the layer presents its content using a Core Animation transaction.

## Relationships

### Inherits From
- [CALayer](./calayer.md)
### Conforms To
- [CAMediaTiming](./camediatiming.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [EAGLDrawable](../OpenGLES/eagldrawable.md)
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
- [class CAEDRMetadata](./caedrmetadata.md)
  Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [class CAOpenGLLayer](./caopengllayer.md)
  A layer that provides a layer suitable for rendering OpenGL content.
- [class CARenderer](./carenderer.md)
  A layer that allows an application to render a layer tree into a Core OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caeagllayer)*