# MeshBuffers.Identifier

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct Identifier
```

## Topics

### Operators
- [static func == (MeshBuffers.Identifier, MeshBuffers.Identifier) -> Bool](meshbuffers/identifier/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var description: String](meshbuffers/identifier/description.md)
  A textual representation of this instance.
- [var hashValue: Int](meshbuffers/identifier/hashvalue.md)
  The hash value.
- [let isBlendShape: Bool](meshbuffers/identifier/isblendshape.md)
- [let isCustom: Bool](meshbuffers/identifier/iscustom.md)
- [let name: String](meshbuffers/identifier/name.md)
### Instance Methods
- [func hash(into: inout Hasher)](meshbuffers/identifier/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let bitangents: MeshBuffers.Identifier](meshbuffers/identifier/bitangents.md)
- [static let jointInfluences: MeshBuffers.Identifier](meshbuffers/identifier/jointinfluences.md)
- [static let normals: MeshBuffers.Identifier](meshbuffers/identifier/normals.md)
- [static let positions: MeshBuffers.Identifier](meshbuffers/identifier/positions.md)
- [static let tangents: MeshBuffers.Identifier](meshbuffers/identifier/tangents.md)
- [static let textureCoordinates: MeshBuffers.Identifier](meshbuffers/identifier/texturecoordinates.md)
- [static let triangleIndices: MeshBuffers.Identifier](meshbuffers/identifier/triangleindices.md)
### Default Implementations
- [Equatable Implementations](meshbuffers/identifier/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshbuffers/identifier)*