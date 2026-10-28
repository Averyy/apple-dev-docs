# MTLVertexDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An instance that describes how to organize and map data to a vertex function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class MTLVertexDescriptor
```

```objc
@interface MTLVertexDescriptor : NSObject
```

## Overview

An [`MTLVertexDescriptor`](./mtlvertexdescriptor.md) instance is used to configure how vertex data stored in memory is mapped to attributes in a vertex shader.

A pipeline state is the state of the graphics rendering pipeline, including shaders, blending, multisampling, and visibility testing. For every pipeline state, there can be only one [`MTLVertexDescriptor`](./mtlvertexdescriptor.md) instance. When you configure an [`MTLRenderPipelineDescriptor`](./mtlrenderpipelinedescriptor.md) instance to create this pipeline state, you use an [`MTLVertexDescriptor`](./mtlvertexdescriptor.md) instance to establish the vertex layout for the function associated with the pipeline. Create and configure an [`MTLVertexDescriptor`](./mtlvertexdescriptor.md) instance, then use this instance to set the [`vertexDescriptor`](./mtlrenderpipelinedescriptor/vertexdescriptor.md) property of the [`MTLRenderPipelineDescriptor`](./mtlrenderpipelinedescriptor.md) instance.

## Topics

### Setting default values
- [func reset()](./mtlvertexdescriptor/reset%28%29.md)
  Resets the default state for the vertex descriptor.
### Accessing the vertex buffer layouts and vertex attributes
- [var attributes: MTLVertexAttributeDescriptorArray](./mtlvertexdescriptor/attributes.md)
  An array of state data that describes how vertex attribute data is stored in memory and is mapped to arguments for a vertex shader function.
- [var layouts: MTLVertexBufferLayoutDescriptorArray](./mtlvertexdescriptor/layouts.md)
  An array of state data that describes how data are fetched by a vertex shader function when rendering primitives.
### Creating a new vertex descriptor
- [+ vertexDescriptor](./mtlvertexdescriptor/vertexdescriptor.md)
  Creates and returns a new vertex descriptor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Render pass inputs
- [class MTLVertexAttributeDescriptor](./mtlvertexattributedescriptor.md)
  An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [class MTLVertexAttributeDescriptorArray](./mtlvertexattributedescriptorarray.md)
  An array of vertex attribute descriptor instances.
- [class MTLVertexBufferLayoutDescriptor](./mtlvertexbufferlayoutdescriptor.md)
  An object that configures how a render pipeline fetches data to send to the vertex function.
- [class MTLVertexBufferLayoutDescriptorArray](./mtlvertexbufferlayoutdescriptorarray.md)
  An array of vertex buffer layout descriptor instances.
- [var MTLBufferLayoutStrideDynamic: Int](./mtlbufferlayoutstridedynamic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexdescriptor)*