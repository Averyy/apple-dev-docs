# MTLRenderPipelineFunctionsDescriptor

**Framework**: Metal  
**Kind**: class

A collection of functions for updating a render pipeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLRenderPipelineFunctionsDescriptor
```

#### Overview

When you create a render pipeline that takes visible functions as parameters, you must specify all possible functions that the render pipeline can call. If you already have a pipeline, you can create a new render pipeline with the same configuration but additional callable functions. To create the new pipeline state object, configure a [`MTLRenderPipelineFunctionsDescriptor`](mtlrenderpipelinefunctionsdescriptor.md) object with the additional callable functions to add, and then call the pipeline state object’s [`makeRenderPipelineState(additionalBinaryFunctions:)`](mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:).md) method, passing the descriptor.

## Topics

### Configuring the Descriptor’s Functions
- [var vertexAdditionalBinaryFunctions: [any MTLFunction]?](mtlrenderpipelinefunctionsdescriptor/vertexadditionalbinaryfunctions.md)
  The vertex functions to add to the render pipeline.
- [var fragmentAdditionalBinaryFunctions: [any MTLFunction]?](mtlrenderpipelinefunctionsdescriptor/fragmentadditionalbinaryfunctions.md)
  The fragment functions to add to the render pipeline.
- [var tileAdditionalBinaryFunctions: [any MTLFunction]?](mtlrenderpipelinefunctionsdescriptor/tileadditionalbinaryfunctions.md)
  The tile functions to add to the render pipeline.

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
- [class MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for mesh shading.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinefunctionsdescriptor)*