# MTLVertexAttributeDescriptor

**Framework**: Metal  
**Kind**: class

An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLVertexAttributeDescriptor
```

#### Overview

A vertex attribute descriptor provides organization information so a vertex shader function can locate and load data into its arguments. The descriptor maps memory locations to attribute locations. It supports access to multiple attributes (such as vertex coordinates, surface normals, and texture coordinates) that are interleaved within the same buffer.

## Topics

### Organizing the vertex attribute
- [var format: MTLVertexFormat](mtlvertexattributedescriptor/format.md)
  The format of the vertex attribute.
- [var offset: Int](mtlvertexattributedescriptor/offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [var bufferIndex: Int](mtlvertexattributedescriptor/bufferindex.md)
  The index in the argument table for the associated vertex buffer.
- [enum MTLVertexFormat](mtlvertexformat.md)
  Values that specify the organization of function vertex data.

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

- [class MTLVertexDescriptor](mtlvertexdescriptor.md)
  An instance that describes how to organize and map data to a vertex function.
- [class MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md)
  An array of vertex attribute descriptor instances.
- [class MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md)
  An object that configures how a render pipeline fetches data to send to the vertex function.
- [class MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md)
  An array of vertex buffer layout descriptor instances.
- [let MTLBufferLayoutStrideDynamic: Int](mtlbufferlayoutstridedynamic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor)*