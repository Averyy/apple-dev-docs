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
### Deprecated
- [NSOpenGLCPSwapInterval](../nsopenglcpswapinterval.md)
  Sets or gets the swap interval.
- [NSOpenGLCPSurfaceOrder](../nsopenglcpsurfaceorder.md)
  Get or set the surface order.
- [NSOpenGLCPSurfaceOpacity](../nsopenglcpsurfaceopacity.md)
  Set or get the surface opacity.
- [NSOpenGLCPSurfaceBackingSize](../nsopenglcpsurfacebackingsize.md)
  Set or get the height and width of the back buffer. You can use this to let the system scale an image automatically on swapping to a variable-size buffer. The back buffer size remains fixed at the size that you set up regardless of whether the image is resized to display larger onscreen.
- [NSOpenGLCPReclaimResources](../nsopenglcpreclaimresources.md)
  Enable or disable reclaiming resources.
- [NSOpenGLCPCurrentRendererID](../nsopenglcpcurrentrendererid.md)
  The current renderer ID. You can get this setting.
- [NSOpenGLCPGPUVertexProcessing](../nsopenglcpgpuvertexprocessing.md)
  The CPU is currently processing vertices with the GPU. You can get this state.
- [NSOpenGLCPGPUFragmentProcessing](../nsopenglcpgpufragmentprocessing.md)
  The CPU is currently processing fragments with the GPU. You can get this state.
- [NSOpenGLCPHasDrawable](../nsopenglcphasdrawable.md)
  Returns a Boolean that indicates whether a drawable is attached to the context.
- [NSOpenGLCPMPSwapsInFlight](../nsopenglcpmpswapsinflight.md)
  The number of frames that the multithreaded OpenGL engine can process before stalling. The default value is 1. New frames are queued when the application calls the [`flushBuffer`](./flushbuffer%28%29.md) method. A larger number may improve overall performance, but adds latency between when a frame is rendered and when a frame is displayed. Interactive applications should leave this value at the default.
- [NSOpenGLCPSwapRectangle](../nsopenglcpswaprectangle.md)
  Sets or gets the swap rectangle.
- [NSOpenGLCPSwapRectangleEnable](../nsopenglcpswaprectangleenable.md)
  Enables or disables the swap rectangle in the context’s drawable object.
- [NSOpenGLCPRasterizationEnable](../nsopenglcprasterizationenable.md)
  If disabled, all rasterization of 2D and 3D primitives is disabled.
- [NSOpenGLCPStateValidation](../nsopenglcpstatevalidation.md)
  If enabled, OpenGL inspects the context state each time the [`update`](./update%28%29.md) method is called to ensure that it is in an appropriate state for switching between renderers.
- [NSOpenGLCPSurfaceSurfaceVolatile](../nsopenglcpsurfacesurfacevolatile.md)

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