# MTL4RenderPipelineBinaryFunctionsDescriptor

**Framework**: Metal  
**Kind**: class

Allows you to specify additional binary functions to link to each stage of a render pipeline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4RenderPipelineBinaryFunctionsDescriptor
```

## Topics

### Instance Properties
- [var fragmentAdditionalBinaryFunctions: [any MTL4BinaryFunction]?](mtl4renderpipelinebinaryfunctionsdescriptor/fragmentadditionalbinaryfunctions.md)
  Provides an array of binary functions representing additional binary fragment shader functions.
- [var meshAdditionalBinaryFunctions: [any MTL4BinaryFunction]?](mtl4renderpipelinebinaryfunctionsdescriptor/meshadditionalbinaryfunctions.md)
  Provides an array of binary functions representing additional binary mesh shader functions.
- [var objectAdditionalBinaryFunctions: [any MTL4BinaryFunction]?](mtl4renderpipelinebinaryfunctionsdescriptor/objectadditionalbinaryfunctions.md)
  Provides an array of binary functions representing additional binary object shader functions.
- [var tileAdditionalBinaryFunctions: [any MTL4BinaryFunction]?](mtl4renderpipelinebinaryfunctionsdescriptor/tileadditionalbinaryfunctions.md)
  Provides an array of binary functions representing additional binary tile shader functions.
- [var vertexAdditionalBinaryFunctions: [any MTL4BinaryFunction]?](mtl4renderpipelinebinaryfunctionsdescriptor/vertexadditionalbinaryfunctions.md)
  Provides an array of binary functions representing additional binary vertex shader functions.
### Instance Methods
- [func reset()](mtl4renderpipelinebinaryfunctionsdescriptor/reset.md)
  Resets this descriptor to its default state.

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
- [class MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md)
  Groups together properties to create a render pipeline state object.
- [class MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md)
  An argument of options you pass to a GPU device to get a render pipeline state.
- [class MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md)
  A collection of functions for updating a render pipeline.
- [class MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md)
  Groups together properties you use to create a mesh render pipeline state object.
- [class MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for mesh shading.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [class MTL4RenderPipelineColorAttachmentDescriptor](mtl4renderpipelinecolorattachmentdescriptor.md)
- [class MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md)
  A color render target that specifies the color configuration and color operations for a render pipeline.
- [class MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md)
  An array of render pipeline color attachment descriptor objects.
- [class MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md)
  Groups together properties you use to create a tile render pipeline state object.
- [class MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for tile shading.
- [class MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md)
  A description of a tile-shading render pipeline’s color render target.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinebinaryfunctionsdescriptor)*