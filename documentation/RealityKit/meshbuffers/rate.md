# MeshBuffers.Rate

**Framework**: RealityKit  
**Kind**: enum

Defines how elements in the buffer map to features of the mesh.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
enum Rate
```

## Topics

### Operators
- [static func == (MeshBuffers.Rate, MeshBuffers.Rate) -> Bool](meshbuffers/rate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [MeshBuffers.Rate.face](meshbuffers/rate/face.md)
  Buffer maps at the face rate.
- [MeshBuffers.Rate.faceVarying](meshbuffers/rate/facevarying.md)
  Buffer maps at the index rate.
- [MeshBuffers.Rate.vertex](meshbuffers/rate/vertex.md)
  Buffer maps at the vertex rate.
### Instance Properties
- [var hashValue: Int](meshbuffers/rate/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](meshbuffers/rate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](meshbuffers/rate/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshbuffers/rate)*