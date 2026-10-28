# NSOpenGLCPSwapRectangleEnable

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

Enables or disables the swap rectangle in the context’s drawable object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Deprecated. Do not use this for new development.

## Declaration

```c
static const NSOpenGLContextParameter NSOpenGLCPSwapRectangleEnable;
```

## Discussion

If enabled, the area that is affected by the [`flushBuffer()`](./nsopenglcontext/flushbuffer%28%29.md) method is restricted to a rectangle specified by the values of `NSOpenGLCPSwapRectangle`. However, the portion of the drawable object that lies outside of the swap rectangle may still be flushed to the screen by a visibility change or other user interface action.

## See Also

### Deprecated
- [NSOpenGLCPSwapInterval](./nsopenglcpswapinterval.md)
  Sets or gets the swap interval.
- [NSOpenGLCPSurfaceOrder](./nsopenglcpsurfaceorder.md)
  Get or set the surface order.
- [NSOpenGLCPSurfaceOpacity](./nsopenglcpsurfaceopacity.md)
  Set or get the surface opacity.
- [NSOpenGLCPSurfaceBackingSize](./nsopenglcpsurfacebackingsize.md)
  Set or get the height and width of the back buffer. You can use this to let the system scale an image automatically on swapping to a variable-size buffer. The back buffer size remains fixed at the size that you set up regardless of whether the image is resized to display larger onscreen.
- [NSOpenGLCPReclaimResources](./nsopenglcpreclaimresources.md)
  Enable or disable reclaiming resources.
- [NSOpenGLCPCurrentRendererID](./nsopenglcpcurrentrendererid.md)
  The current renderer ID. You can get this setting.
- [NSOpenGLCPGPUVertexProcessing](./nsopenglcpgpuvertexprocessing.md)
  The CPU is currently processing vertices with the GPU. You can get this state.
- [NSOpenGLCPGPUFragmentProcessing](./nsopenglcpgpufragmentprocessing.md)
  The CPU is currently processing fragments with the GPU. You can get this state.
- [NSOpenGLCPHasDrawable](./nsopenglcphasdrawable.md)
  Returns a Boolean that indicates whether a drawable is attached to the context.
- [NSOpenGLCPMPSwapsInFlight](./nsopenglcpmpswapsinflight.md)
  The number of frames that the multithreaded OpenGL engine can process before stalling. The default value is 1. New frames are queued when the application calls the [`flushBuffer()`](./nsopenglcontext/flushbuffer%28%29.md) method. A larger number may improve overall performance, but adds latency between when a frame is rendered and when a frame is displayed. Interactive applications should leave this value at the default.
- [NSOpenGLCPSwapRectangle](./nsopenglcpswaprectangle.md)
  Sets or gets the swap rectangle.
- [NSOpenGLCPRasterizationEnable](./nsopenglcprasterizationenable.md)
  If disabled, all rasterization of 2D and 3D primitives is disabled.
- [NSOpenGLCPStateValidation](./nsopenglcpstatevalidation.md)
  If enabled, OpenGL inspects the context state each time the [`update()`](./nsopenglcontext/update%28%29.md) method is called to ensure that it is in an appropriate state for switching between renderers.
- [NSOpenGLCPSurfaceSurfaceVolatile](./nsopenglcpsurfacesurfacevolatile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcpswaprectangleenable)*