# MTLMeshRenderPipelineDescriptor

**Framework**: Metal  
**Kind**: class

An object that configures new render pipeline state objects for mesh shading.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLMeshRenderPipelineDescriptor
```

## Topics

### Instance Properties
- [var binaryArchives: [any MTLBinaryArchive]?](mtlmeshrenderpipelinedescriptor/binaryarchives.md)
- [var colorAttachments: MTLRenderPipelineColorAttachmentDescriptorArray](mtlmeshrenderpipelinedescriptor/colorattachments.md)
- [var depthAttachmentPixelFormat: MTLPixelFormat](mtlmeshrenderpipelinedescriptor/depthattachmentpixelformat.md)
- [var fragmentBuffers: MTLPipelineBufferDescriptorArray](mtlmeshrenderpipelinedescriptor/fragmentbuffers.md)
- [var fragmentFunction: (any MTLFunction)?](mtlmeshrenderpipelinedescriptor/fragmentfunction.md)
- [var fragmentLinkedFunctions: MTLLinkedFunctions!](mtlmeshrenderpipelinedescriptor/fragmentlinkedfunctions.md)
- [var isAlphaToCoverageEnabled: Bool](mtlmeshrenderpipelinedescriptor/isalphatocoverageenabled.md)
- [var isAlphaToOneEnabled: Bool](mtlmeshrenderpipelinedescriptor/isalphatooneenabled.md)
- [var isRasterizationEnabled: Bool](mtlmeshrenderpipelinedescriptor/israsterizationenabled.md)
- [var label: String?](mtlmeshrenderpipelinedescriptor/label.md)
- [var maxTotalThreadgroupsPerMeshGrid: Int](mtlmeshrenderpipelinedescriptor/maxtotalthreadgroupspermeshgrid.md)
- [var maxTotalThreadsPerMeshThreadgroup: Int](mtlmeshrenderpipelinedescriptor/maxtotalthreadspermeshthreadgroup.md)
- [var maxTotalThreadsPerObjectThreadgroup: Int](mtlmeshrenderpipelinedescriptor/maxtotalthreadsperobjectthreadgroup.md)
- [var maxVertexAmplificationCount: Int](mtlmeshrenderpipelinedescriptor/maxvertexamplificationcount.md)
- [var meshBuffers: MTLPipelineBufferDescriptorArray](mtlmeshrenderpipelinedescriptor/meshbuffers.md)
- [var meshFunction: (any MTLFunction)?](mtlmeshrenderpipelinedescriptor/meshfunction.md)
- [var meshLinkedFunctions: MTLLinkedFunctions!](mtlmeshrenderpipelinedescriptor/meshlinkedfunctions.md)
- [var meshThreadgroupSizeIsMultipleOfThreadExecutionWidth: Bool](mtlmeshrenderpipelinedescriptor/meshthreadgroupsizeismultipleofthreadexecutionwidth.md)
- [var objectBuffers: MTLPipelineBufferDescriptorArray](mtlmeshrenderpipelinedescriptor/objectbuffers.md)
- [var objectFunction: (any MTLFunction)?](mtlmeshrenderpipelinedescriptor/objectfunction.md)
- [var objectLinkedFunctions: MTLLinkedFunctions!](mtlmeshrenderpipelinedescriptor/objectlinkedfunctions.md)
- [var objectThreadgroupSizeIsMultipleOfThreadExecutionWidth: Bool](mtlmeshrenderpipelinedescriptor/objectthreadgroupsizeismultipleofthreadexecutionwidth.md)
- [var payloadMemoryLength: Int](mtlmeshrenderpipelinedescriptor/payloadmemorylength.md)
- [var rasterSampleCount: Int](mtlmeshrenderpipelinedescriptor/rastersamplecount.md)
- [var shaderValidation: MTLShaderValidation](mtlmeshrenderpipelinedescriptor/shadervalidation.md)
  A value that enables or disables shader validation for the pipeline.
- [var stencilAttachmentPixelFormat: MTLPixelFormat](mtlmeshrenderpipelinedescriptor/stencilattachmentpixelformat.md)
- [var supportIndirectCommandBuffers: Bool](mtlmeshrenderpipelinedescriptor/supportindirectcommandbuffers.md)
### Instance Methods
- [func reset()](mtlmeshrenderpipelinedescriptor/reset.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLRenderPipelineState](mtlrenderpipelinestate.md)
  An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [class MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md)
  An argument of options you pass to a GPU device to get a render pipeline state.
- [class MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md)
  A collection of functions for updating a render pipeline.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [class MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md)
  A color render target that specifies the color configuration and color operations for a render pipeline.
- [class MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md)
  An array of render pipeline color attachment descriptor objects.
- [class MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for tile shading.
- [class MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md)
  A description of a tile-shading render pipeline’s color render target.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmeshrenderpipelinedescriptor)*