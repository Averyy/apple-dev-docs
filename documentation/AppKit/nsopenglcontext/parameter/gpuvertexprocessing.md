# NSOpenGLContext.Parameter.gpuVertexProcessing

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Get whether the CPU is currently processing vertices with the GPU.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: OpenGL API deprecated; please use Metal and MetalKit.  (Define GL_SILENCE_DEPRECATION to silence these warnings.)

## Declaration

```swift
case gpuVertexProcessing
```

```c
NSOpenGLContextParameterGPUVertexProcessing
```

## See Also

### Parameters
- [NSOpenGLContext.Parameter.swapInterval](./swapinterval.md)
  Set or get the swap interval.
- [NSOpenGLContext.Parameter.surfaceOrder](./surfaceorder.md)
  Set or get the surface order.
- [NSOpenGLContext.Parameter.surfaceOpacity](./surfaceopacity.md)
  Set or get the surface opacity.
- [NSOpenGLContext.Parameter.surfaceBackingSize](./surfacebackingsize.md)
  Set or get the height and width of the back buffer.
- [NSOpenGLContext.Parameter.reclaimResources](./reclaimresources.md)
  Enable or disable reclaiming resources.
- [NSOpenGLContext.Parameter.currentRendererID](./currentrendererid.md)
  Get the current renderer ID.
- [NSOpenGLContext.Parameter.gpuFragmentProcessing](./gpufragmentprocessing.md)
  Get whether the CPU is currently processing fragments with the GPU.
- [NSOpenGLContext.Parameter.hasDrawable](./hasdrawable.md)
  Returns a Boolean that indicates whether a drawable is attached to the context.
- [NSOpenGLContext.Parameter.mpSwapsInFlight](./mpswapsinflight.md)
  The number of frames that the multithreaded OpenGL engine can process before stalling.
- [NSOpenGLContext.Parameter.swapRectangle](./swaprectangle.md)
  Sets or gets the swap rectangle.
- [NSOpenGLContext.Parameter.swapRectangleEnable](./swaprectangleenable.md)
  Enables or disables the swap rectangle in the context’s drawable object.
- [NSOpenGLContext.Parameter.rasterizationEnable](./rasterizationenable.md)
  If disabled, all rasterization of 2D and 3D primitives is disabled.
- [NSOpenGLContext.Parameter.stateValidation](./statevalidation.md)
  If enabled, OpenGL inspects the context state each time the update method is called to ensure that it is in an appropriate state for switching between renderers.
- [NSOpenGLContext.Parameter.surfaceSurfaceVolatile](./surfacesurfacevolatile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter/gpuvertexprocessing)*