# MTLVertexBufferLayoutDescriptor

**Framework**: Metal  
**Kind**: class

An object that configures how a render pipeline fetches data to send to the vertex function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLVertexBufferLayoutDescriptor
```

## Topics

### Organizing the vertex buffer layout
- [var stepFunction: MTLVertexStepFunction](mtlvertexbufferlayoutdescriptor/stepfunction.md)
  The circumstances under which the vertex and its attributes are presented to the vertex function.
- [var stepRate: Int](mtlvertexbufferlayoutdescriptor/steprate.md)
  The interval at which the vertex and its attributes are presented to the vertex function.
- [var stride: Int](mtlvertexbufferlayoutdescriptor/stride.md)
  The number of bytes between the first byte of two consecutive vertices in a buffer.
- [enum MTLVertexStepFunction](mtlvertexstepfunction.md)
  The frequency with which the vertex function or post-tessellation vertex function fetches attribute data.

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
- [class MTLVertexAttributeDescriptor](mtlvertexattributedescriptor.md)
  An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [class MTLVertexAttributeDescriptorArray](mtlvertexattributedescriptorarray.md)
  An array of vertex attribute descriptor instances.
- [class MTLVertexBufferLayoutDescriptorArray](mtlvertexbufferlayoutdescriptorarray.md)
  An array of vertex buffer layout descriptor instances.
- [let MTLBufferLayoutStrideDynamic: Int](mtlbufferlayoutstridedynamic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor)*