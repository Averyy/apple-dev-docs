# SCNGeometrySource.Semantic

**Framework**: SceneKit  
**Kind**: struct

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct Semantic
```

## Topics

### Basic Geometry Semantics
- [static let vertex: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/vertex.md)
  The semantic for vertex position data.
- [static let normal: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/normal.md)
  The semantic for surface normal data.
- [static let texcoord: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/texcoord.md)
  The semantic for texture coordinate data.
### Advanced Shading Semantics
- [static let color: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/color.md)
  The semantic for per-vertex color data.
- [static let tangent: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/tangent.md)
  The semantic for surface tangent vector data.
### Surface Subdivision Semantics
- [static let edgeCrease: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/edgecrease.md)
  The semantic for edge crease data, used for subdividing surfaces.
- [static let vertexCrease: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/vertexcrease.md)
  The semantic for vertex crease data, used for subdividing surfaces.
### Skeletal Animation Semantics
- [static let boneIndices: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/boneindices.md)
  The semantic for bone index data, used for skeletal animation of skinned surfaces.
- [static let boneWeights: SCNGeometrySource.Semantic](scngeometrysource/semantic-swift.struct/boneweights.md)
  The semantic for bone weight data, used for skeletal animation of skinned surfaces.
### Initializers
- [init(String)](scngeometrysource/semantic-swift.struct/init(_:).md)
- [init(rawValue: String)](scngeometrysource/semantic-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct)*