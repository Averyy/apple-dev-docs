# MTLVertexBufferLayoutDescriptorArray

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An array of vertex buffer layout descriptor instances.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class MTLVertexBufferLayoutDescriptorArray
```

```objc
@interface MTLVertexBufferLayoutDescriptorArray : NSObject
```

## Overview

An [`MTLVertexBufferLayoutDescriptorArray`](./mtlvertexbufferlayoutdescriptorarray.md) holds an array of vertex buffer layout states. The methods of [`MTLVertexBufferLayoutDescriptorArray`](./mtlvertexbufferlayoutdescriptorarray.md) set the vertex buffer layout state in the array or retrieve the state from the array.

## Topics

### Accessing a specified vertex buffer layout
- [subscript(Int) -> MTLVertexBufferLayoutDescriptor!](./mtlvertexbufferlayoutdescriptorarray/subscript%28_%29.md)
  Returns the state of the specified vertex buffer layout.
- [- setObject:atIndexedSubscript:](./mtlvertexbufferlayoutdescriptorarray/setobject_atindexedsubscript_.md)
  Sets the state of the specified vertex buffer layout.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Render pass inputs
- [class MTLVertexDescriptor](./mtlvertexdescriptor.md)
  An instance that describes how to organize and map data to a vertex function.
- [class MTLVertexAttributeDescriptor](./mtlvertexattributedescriptor.md)
  An object that determines how to store attribute data in memory and map it to the arguments of a vertex function.
- [class MTLVertexAttributeDescriptorArray](./mtlvertexattributedescriptorarray.md)
  An array of vertex attribute descriptor instances.
- [class MTLVertexBufferLayoutDescriptor](./mtlvertexbufferlayoutdescriptor.md)
  An object that configures how a render pipeline fetches data to send to the vertex function.
- [var MTLBufferLayoutStrideDynamic: Int](./mtlbufferlayoutstridedynamic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray)*