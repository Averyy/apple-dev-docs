# init(vertexDescriptor:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

Creates a new vertex descriptor by performing a deep copy of the specified vertex descriptor.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(vertexDescriptor: MDLVertexDescriptor)
```

```objc
- (instancetype) initWithVertexDescriptor:(MDLVertexDescriptor *) vertexDescriptor;
```

#### Return Value

A new vertex descriptor that is an indpendent copy of the specified vertex descriptor.

#### Discussion

A vertex descriptor does not own vertex data—vertex data belongs to the [`vertexBuffers`](../mdlmesh/vertexbuffers.md) property of the mesh that owns a vertex descriptor—so this method does not copy vertex data. A call to the [`copy()`](../../ObjectiveC/nsobject-swift.class/copy%28%29.md) or [`copy(with:)`](../../Foundation/nscopying/copy%28with%29.md) method uses this initializer to produce a fully independent copy of the original instance.

## Parameters

- `vertexDescriptor`: The vertex descriptor from which to copy information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor/init(vertexdescriptor:))*