# MTLVertexDescriptor

**Framework**: Metal  
**Kind**: class

An object that describes how to organize and map data to a vertex function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLVertexDescriptor
```

#### Overview

A [`MTLVertexDescriptor`](mtlvertexdescriptor.md) object is used to configure how vertex data stored in memory is mapped to attributes in a vertex shader.

A pipeline state is the state of the graphics rendering pipeline, including shaders, blending, multisampling, and visibility testing. For every pipeline state, there can be only one [`MTLVertexDescriptor`](mtlvertexdescriptor.md) object. When you configure a [`MTLRenderPipelineDescriptor`](mtlrenderpipelinedescriptor.md) object to create this pipeline state, you use a [`MTLVertexDescriptor`](mtlvertexdescriptor.md) object to establish the vertex layout for the function associated with the pipeline. Create and configure a [`MTLVertexDescriptor`](mtlvertexdescriptor.md) object, then use this object to set the [`vertexDescriptor`](mtlrenderpipelinedescriptor/vertexdescriptor.md) property of the [`MTLRenderPipelineDescriptor`](mtlrenderpipelinedescriptor.md) object.

## Topics

### Setting Default Values
- [func reset()](mtlvertexdescriptor/reset.md)
  Resets the default state for the vertex descriptor.
### Accessing the Vertex Buffer Layouts and Vertex Attributes
- [var attributes: MTLVertexAttributeDescriptorArray](mtlvertexdescriptor/attributes.md)
  An array of state data that describes how vertex attribute data is stored in memory and is mapped to arguments for a vertex shader function.
- [var layouts: MTLVertexBufferLayoutDescriptorArray](mtlvertexdescriptor/layouts.md)
  An array of state data that describes how data are fetched by a vertex shader function when rendering primitives.

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

- [class MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md)
  An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [class MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md)
  An array of vertex attribute descriptor objects.
- [class MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md)
  An object that configures how a render pipeline fetches data to send to the vertex function.
- [class MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md)
  An array of vertex buffer layout descriptor objects.
- [let MTLBufferLayoutStrideDynamic: Int](mtlbufferlayoutstridedynamic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexdescriptor)*