# NSOpenGLContext.Parameter

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify context parameters.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: OpenGL API deprecated; please use Metal and MetalKit.  (Define GL_SILENCE_DEPRECATION to silence these warnings.)

## Declaration

```swift
enum Parameter
```

```c
enum NSOpenGLContextParameter : NSInteger;
```

#### Overview

These attribute names are used by [`setValues(_:for:)`](./setvalues%28_,for%29.md) and [`getValues(_:for:)`](./getvalues%28_,for%29.md).

## Topics

### Parameters
- [NSOpenGLContext.Parameter.swapInterval](./parameter/swapinterval.md)
  Set or get the swap interval.
- [NSOpenGLContext.Parameter.surfaceOrder](./parameter/surfaceorder.md)
  Set or get the surface order.
- [NSOpenGLContext.Parameter.surfaceOpacity](./parameter/surfaceopacity.md)
  Set or get the surface opacity.
- [NSOpenGLContext.Parameter.surfaceBackingSize](./parameter/surfacebackingsize.md)
  Set or get the height and width of the back buffer.
- [NSOpenGLContext.Parameter.reclaimResources](./parameter/reclaimresources.md)
  Enable or disable reclaiming resources.
- [NSOpenGLContext.Parameter.currentRendererID](./parameter/currentrendererid.md)
  Get the current renderer ID.
- [NSOpenGLContext.Parameter.gpuVertexProcessing](./parameter/gpuvertexprocessing.md)
  Get whether the CPU is currently processing vertices with the GPU.
- [NSOpenGLContext.Parameter.gpuFragmentProcessing](./parameter/gpufragmentprocessing.md)
  Get whether the CPU is currently processing fragments with the GPU.
- [NSOpenGLContext.Parameter.hasDrawable](./parameter/hasdrawable.md)
  Returns a Boolean that indicates whether a drawable is attached to the context.
- [NSOpenGLContext.Parameter.mpSwapsInFlight](./parameter/mpswapsinflight.md)
  The number of frames that the multithreaded OpenGL engine can process before stalling.
- [NSOpenGLContext.Parameter.swapRectangle](./parameter/swaprectangle.md)
  Sets or gets the swap rectangle.
- [NSOpenGLContext.Parameter.swapRectangleEnable](./parameter/swaprectangleenable.md)
  Enables or disables the swap rectangle in the context’s drawable object.
- [NSOpenGLContext.Parameter.rasterizationEnable](./parameter/rasterizationenable.md)
  If disabled, all rasterization of 2D and 3D primitives is disabled.
- [NSOpenGLContext.Parameter.stateValidation](./parameter/statevalidation.md)
  If enabled, OpenGL inspects the context state each time the update method is called to ensure that it is in an appropriate state for switching between renderers.
- [NSOpenGLContext.Parameter.surfaceSurfaceVolatile](./parameter/surfacesurfacevolatile.md)
### Initializers
- [init?(rawValue: Int)](./parameter/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter)*