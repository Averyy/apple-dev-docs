# Render pass configuration

**Framework**: Metal

Set a render pass’s pipeline state, attachment actions, viewports, and so on, that affect subsequent drawing commands.

#### Overview

These methods encode commands that configure the render pass for all subsequent drawing commands. The most important configuration is the pipeline state (see [`MTLRenderPipelineState`](mtlrenderpipelinestate.md)), which you configure by calling the [`setRenderPipelineState(_:)`](mtlrendercommandencoder/setrenderpipelinestate(_:).md) method.

## Topics

### Configuring pipeline state
- [func setRenderPipelineState(any MTLRenderPipelineState)](mtlrendercommandencoder/setrenderpipelinestate(_:).md)
  Configures the encoder with a render or tile pipeline state that applies to your subsequent draw commands.
### Configuring the actions for attachments
- [func setColorStoreAction(MTLStoreAction, index: Int)](mtlrendercommandencoder/setcolorstoreaction(_:index:).md)
  Configures the store action for a color attachment.
- [func setColorStoreActionOptions(MTLStoreActionOptions, index: Int)](mtlrendercommandencoder/setcolorstoreactionoptions(_:index:).md)
  Configures the store action options for a color attachment.
- [func setDepthStoreAction(MTLStoreAction)](mtlrendercommandencoder/setdepthstoreaction(_:).md)
  Configures the store action for the depth attachment.
- [func setDepthStoreActionOptions(MTLStoreActionOptions)](mtlrendercommandencoder/setdepthstoreactionoptions(_:).md)
  Configures the store action options for the depth attachment.
- [func setStencilStoreAction(MTLStoreAction)](mtlrendercommandencoder/setstencilstoreaction(_:).md)
  Configures the store action for the stencil attachment.
- [func setStencilStoreActionOptions(MTLStoreActionOptions)](mtlrendercommandencoder/setstencilstoreactionoptions(_:).md)
  Configures the store action options for the stencil attachment.
### Configuring blend behavior
- [func setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)](mtlrendercommandencoder/setblendcolor(red:green:blue:alpha:).md)
  Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.
- [func setColorAttachmentMap(MTLLogicalToPhysicalColorAttachmentMap?)](mtlrendercommandencoder/setcolorattachmentmap(_:).md)
  Sets the mapping from logical shader color output to physical render pass color attachments.
### Configuring rendering behavior
- [func setTriangleFillMode(MTLTriangleFillMode)](mtlrendercommandencoder/settrianglefillmode(_:).md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setFrontFacing(MTLWinding)](mtlrendercommandencoder/setfrontfacing(_:).md)
  Configures which face of a primitive, such as a triangle, is the front.
- [func setCullMode(MTLCullMode)](mtlrendercommandencoder/setcullmode(_:).md)
  Configures how the render pipeline determines which primitives to remove.
### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](mtlrendercommandencoder/setdepthstencilstate(_:).md)
  Configures the combined depth and stencil state.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtlrendercommandencoder/setdepthclipmode(_:).md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setDepthTestBounds(ClosedRange<Float>)](mtlrendercommandencoder/setdepthtestbounds(_:).md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](mtlrendercommandencoder/setstencilreferencevalues(front:back:).md)
  Configures different comparison values for front- and back-facing primitives.
### Configuring viewport and scissor behavior
- [func setViewport(MTLViewport)](mtlrendercommandencoder/setviewport(_:).md)
  Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.
- [func setViewports([MTLViewport])](mtlrendercommandencoder/setviewports(_:).md)
  Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.
- [func setScissorRect(MTLScissorRect)](mtlrendercommandencoder/setscissorrect(_:).md)
  Configures a rectangle for the fragment scissor test.
- [func setScissorRects([MTLScissorRect])](mtlrendercommandencoder/setscissorrects(_:).md)
  Configures multiple rectangles for the fragment scissor test.
### Configuring visibility testing
- [func setVisibilityResultMode(MTLVisibilityResultMode, offset: Int)](mtlrendercommandencoder/setvisibilityresultmode(_:offset:).md)
  Configures which visibility test the GPU runs and the destination for any results it generates.
### Configuring vertex amplification
- [func setVertexAmplificationCount(Int, viewMappings: UnsafePointer<MTLVertexAmplificationViewMapping>?)](mtlrendercommandencoder/setvertexamplificationcount(_:viewmappings:).md)
  Configures the number of output vertices the render pipeline produces for each input vertex, optionally with render target and viewport offsets.
### Configuring tessellation factors
- [func setTessellationFactorScale(Float)](mtlrendercommandencoder/settessellationfactorscale(_:).md)
  Configures the scale factor for per-patch tessellation factors.
- [func setTessellationFactorBuffer((any MTLBuffer)?, offset: Int, instanceStride: Int)](mtlrendercommandencoder/settessellationfactorbuffer(_:offset:instancestride:).md)
  Configures the per-patch tessellation factors for any subsequent patch-drawing commands.
### Configuring persistent threadgroup memory
- [func setObjectThreadgroupMemoryLength(Int, index: Int)](mtlrendercommandencoder/setobjectthreadgroupmemorylength(_:index:).md)
  Configures the size of a threadgroup memory buffer for an entry in the object argument table.
- [func setThreadgroupMemoryLength(Int, offset: Int, index: Int)](mtlrendercommandencoder/setthreadgroupmemorylength(_:offset:index:).md)
  Configures the size of a threadgroup memory buffer for an entry in the fragment or tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/render-pass-configuration)*