# NSOpenGLContext.Parameter

**Framework**: AppKit  
**Kind**: enum

Constants that specify context parameters.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum Parameter
```

#### Overview

These attribute names are used by [`setValues(_:for:)`](nsopenglcontext/setvalues(_:for:).md) and [`getValues(_:for:)`](nsopenglcontext/getvalues(_:for:).md).

## Topics

### Parameters
- [NSOpenGLContext.Parameter.swapInterval](nsopenglcontext/parameter/swapinterval.md)
  Set or get the swap interval.
- [NSOpenGLContext.Parameter.surfaceOrder](nsopenglcontext/parameter/surfaceorder.md)
  Set or get the surface order.
- [NSOpenGLContext.Parameter.surfaceOpacity](nsopenglcontext/parameter/surfaceopacity.md)
  Set or get the surface opacity.
- [NSOpenGLContext.Parameter.surfaceBackingSize](nsopenglcontext/parameter/surfacebackingsize.md)
  Set or get the height and width of the back buffer.
- [NSOpenGLContext.Parameter.reclaimResources](nsopenglcontext/parameter/reclaimresources.md)
  Enable or disable reclaiming resources.
- [NSOpenGLContext.Parameter.currentRendererID](nsopenglcontext/parameter/currentrendererid.md)
  Get the current renderer ID.
- [NSOpenGLContext.Parameter.gpuVertexProcessing](nsopenglcontext/parameter/gpuvertexprocessing.md)
  Get whether the CPU is currently processing vertices with the GPU.
- [NSOpenGLContext.Parameter.gpuFragmentProcessing](nsopenglcontext/parameter/gpufragmentprocessing.md)
  Get whether the CPU is currently processing fragments with the GPU.
- [NSOpenGLContext.Parameter.hasDrawable](nsopenglcontext/parameter/hasdrawable.md)
  Returns a Boolean that indicates whether a drawable is attached to the context.
- [NSOpenGLContext.Parameter.mpSwapsInFlight](nsopenglcontext/parameter/mpswapsinflight.md)
  The number of frames that the multithreaded OpenGL engine can process before stalling.
- [NSOpenGLContext.Parameter.swapRectangle](nsopenglcontext/parameter/swaprectangle.md)
  Sets or gets the swap rectangle.
- [NSOpenGLContext.Parameter.swapRectangleEnable](nsopenglcontext/parameter/swaprectangleenable.md)
  Enables or disables the swap rectangle in the context’s drawable object.
- [NSOpenGLContext.Parameter.rasterizationEnable](nsopenglcontext/parameter/rasterizationenable.md)
  If disabled, all rasterization of 2D and 3D primitives is disabled.
- [NSOpenGLContext.Parameter.stateValidation](nsopenglcontext/parameter/statevalidation.md)
  If enabled, OpenGL inspects the context state each time the update method is called to ensure that it is in an appropriate state for switching between renderers.
- [NSOpenGLContext.Parameter.surfaceSurfaceVolatile](nsopenglcontext/parameter/surfacesurfacevolatile.md)
### Initializers
- [init?(rawValue: Int)](nsopenglcontext/parameter/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/parameter)*