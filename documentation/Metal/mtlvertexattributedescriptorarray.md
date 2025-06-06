# MTLVertexAttributeDescriptorArray

**Framework**: Metal  
**Kind**: class

An array of vertex attribute descriptor objects.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLVertexAttributeDescriptorArray
```

#### Overview

A [`MTLVertexAttributeDescriptorArray`](mtlvertexattributedescriptorarray.md) object is an array of objects that defines how vertex attribute data is formatted and assigned to an index in the attribute argument table. The methods of [`MTLVertexAttributeDescriptorArray`](mtlvertexattributedescriptorarray.md) set or retrieve the attribute formatting information from the array.

## Topics

### Accessing a Specified Vertex Attribute
- [subscript(Int) -> MTLVertexAttributeDescriptor!](mtlvertexattributedescriptorarray/subscript(_:).md)
  Returns the state of the specified vertex attribute.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLVertexDescriptor](mtlvertexdescriptor.md)
  An object that describes how to organize and map data to a vertex function.
- [class MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md)
  An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [class MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md)
  An object that configures how a render pipeline fetches data to send to the vertex function.
- [class MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md)
  An array of vertex buffer layout descriptor objects.
- [let MTLBufferLayoutStrideDynamic: Int](mtlbufferlayoutstridedynamic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray)*