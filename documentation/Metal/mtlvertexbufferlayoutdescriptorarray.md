# MTLVertexBufferLayoutDescriptorArray

**Framework**: Metal  
**Kind**: class

An array of vertex buffer layout descriptor objects.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLVertexBufferLayoutDescriptorArray
```

#### Overview

A [`MTLVertexBufferLayoutDescriptorArray`](mtlvertexbufferlayoutdescriptorarray.md) holds an array of vertex buffer layout states. The methods of [`MTLVertexBufferLayoutDescriptorArray`](mtlvertexbufferlayoutdescriptorarray.md) set the vertex buffer layout state in the array or retrieve the state from the array.

## Topics

### Accessing a Specified Vertex Buffer Layout
- [subscript(Int) -> MTLVertexBufferLayoutDescriptor!](mtlvertexbufferlayoutdescriptorarray/subscript(_:).md)
  Returns the state of the specified vertex buffer layout.

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
- [class MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md)
  An array of vertex attribute descriptor objects.
- [class MTLVertexBufferLayoutDescriptor](mtlvertexbufferlayoutdescriptor.md)
  An object that configures how a render pipeline fetches data to send to the vertex function.
- [let MTLBufferLayoutStrideDynamic: Int](mtlbufferlayoutstridedynamic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray)*