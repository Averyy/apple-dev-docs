# LowLevelRenderer

**Framework**: RealityKit  
**Kind**: class

A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelRenderer
```

#### Overview

`LowLevelRenderer` manages camera constants, per-instance transforms, MSAA resolve, tonemapping, and optional color gamut conversion. You are responsible for creating and committing the Metal command buffer; the renderer only encodes into it.

## Topics

### Creating a renderer
- [convenience init(configuration: LowLevelRenderer.Configuration, renderContext: any LowLevelRenderContext) async throws](lowlevelrenderer/init(configuration:rendercontext:).md)
  Creates a renderer, asynchronously compiling all required GPU resources.
- [LowLevelRenderer.Configuration](lowlevelrenderer/configuration.md)
  The configuration for a renderer.
### Rendering a frame
- [func render(using: any MTLCommandBuffer, (inout LowLevelRenderer.RenderState) -> ())](lowlevelrenderer/render(using:_:).md)
  Encodes draw calls for the frame into the given command buffer using a caller-controlled render callback.
- [LowLevelRenderer.RenderState](lowlevelrenderer/renderstate.md)
  The per-frame render state passed to the `render(using:_:)` callback.
- [LowLevelRenderer.Resources](lowlevelrenderer/resources.md)
  Prepared GPU resources for a renderer.
### Managing mesh instances
- [func meshInstances(at: Int) -> LowLevelMeshInstanceArray?](lowlevelrenderer/meshinstances(at:).md)
  Returns the mesh instance array at the given slot index, or `nil` if the slot is unoccupied.
- [func setMeshInstances(LowLevelMeshInstanceArray?, at: Int) throws(LowLevelRendererError)](lowlevelrenderer/setmeshinstances(_:at:).md)
  Assigns a mesh instance array to the given slot index.
- [var meshInstancesArrayCount: Int](lowlevelrenderer/meshinstancesarraycount.md)
  The number of mesh instance array slots.
### Culling and sorting instances
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, outIndices: inout OutputSpan<Int>, configuration: LowLevelRenderer.CullConfiguration)](lowlevelrenderer/cullmeshinstances(_:indices:outindices:configuration:).md)
  Culls mesh instances against a frustum, writing surviving indices to an output span.
- [static func cullMeshInstances(LowLevelMeshInstanceArray, indices: Span<Int>, configuration: LowLevelRenderer.CullConfiguration) -> [Int]](lowlevelrenderer/cullmeshinstances(_:indices:configuration:).md)
  Culls mesh instances against a frustum and returns the surviving indices.
- [LowLevelRenderer.CullConfiguration](lowlevelrenderer/cullconfiguration.md)
  The configuration for a frustum culling operation.
- [static func sortMeshInstances(LowLevelMeshInstanceArray, indices: inout MutableSpan<Int>, configuration: LowLevelRenderer.SortConfiguration)](lowlevelrenderer/sortmeshinstances(_:indices:configuration:).md)
  Sorts the given mesh instances by sort category and, for transparent instances, by back-to-front distance from the camera.
- [LowLevelRenderer.SortConfiguration](lowlevelrenderer/sortconfiguration.md)
  The configuration for a mesh instance sort pass.
### Configuring cameras
- [var cameras: LowLevelRenderer.CameraArray](lowlevelrenderer/cameras.md)
  The array of active cameras.
- [LowLevelRenderer.CameraArray](lowlevelrenderer/cameraarray.md)
  A mutable, fixed-capacity array of camera values.
- [LowLevelRenderer.Camera](lowlevelrenderer/camera.md)
  The view and projection parameters for a single camera.
### Managing color matching
- [var colorMatch: LowLevelRenderer.ColorMatch](lowlevelrenderer/colormatch-swift.property.md)
  The active color gamut conversion. The renderer applies this value only when `enableColorMatch` is `true` in `Configuration`.
- [LowLevelRenderer.ColorMatch](lowlevelrenderer/colormatch-swift.struct.md)
  A color gamut conversion applied during resolve.
- [func setColorMatch(targetingColorSpace: CGColorSpace) throws(LowLevelRendererError)](lowlevelrenderer/setcolormatch(targetingcolorspace:).md)
  Updates the color match by computing a gamut conversion matrix from the renderer’s working color space to the given target display color space.
- [var workingColorSpace: CGColorSpace](lowlevelrenderer/workingcolorspace.md)
  The color space in which the renderer performs all shading calculations.
### Accessing render output
- [var output: LowLevelRenderer.Output](lowlevelrenderer/output-swift.property.md)
  The per-frame output target configuration, including color and depth textures, viewports, and render target dimensions.
- [LowLevelRenderer.Output](lowlevelrenderer/output-swift.struct.md)
  The per-frame output target configuration for a renderer.
- [var renderTargetDescriptor: LowLevelRenderTarget.Descriptor](lowlevelrenderer/rendertargetdescriptor.md)
  The render target descriptor derived from the renderer’s configuration.
### Initializers
- [init(resources: LowLevelRenderer.Resources) throws(LowLevelRendererError)](lowlevelrenderer/init(resources:).md)
  Creates a renderer using pre-compiled GPU resources.
### Instance Properties
- [var time: Float](lowlevelrenderer/time.md)
  The scene time, in seconds, that the renderer passes to shaders as a uniform.

## See Also

- [protocol LowLevelRenderContext](lowlevelrendercontext.md)
  An entry point for creating rendering resources and compiling materials.
- [protocol LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
  The interface for creating lighting functions for use in materials.
- [protocol LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)
  The interface for creating Metal shader functions from a ShaderGraph.
- [class LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)
  A standalone Metal-backed render context for creating low-level rendering resources.
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown when binding or updating a low-level rendering resource fails.
- [struct LowLevelRendererError](lowlevelrenderererror.md)
  An error thrown when creating or configuring a renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer)*