# SCNGeometrySource.Semantic

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
struct Semantic
```

```c
typedef NSString * SCNGeometrySourceSemantic;
```

## Topics

### Basic Geometry Semantics
- [static let vertex: SCNGeometrySource.Semantic](./semantic-swift.struct/vertex.md)
  The semantic for vertex position data.
- [static let normal: SCNGeometrySource.Semantic](./semantic-swift.struct/normal.md)
  The semantic for surface normal data.
- [static let texcoord: SCNGeometrySource.Semantic](./semantic-swift.struct/texcoord.md)
  The semantic for texture coordinate data.
### Advanced Shading Semantics
- [static let color: SCNGeometrySource.Semantic](./semantic-swift.struct/color.md)
  The semantic for per-vertex color data.
- [static let tangent: SCNGeometrySource.Semantic](./semantic-swift.struct/tangent.md)
  The semantic for surface tangent vector data.
### Surface Subdivision Semantics
- [static let edgeCrease: SCNGeometrySource.Semantic](./semantic-swift.struct/edgecrease.md)
  The semantic for edge crease data, used for subdividing surfaces.
- [static let vertexCrease: SCNGeometrySource.Semantic](./semantic-swift.struct/vertexcrease.md)
  The semantic for vertex crease data, used for subdividing surfaces.
### Skeletal Animation Semantics
- [static let boneIndices: SCNGeometrySource.Semantic](./semantic-swift.struct/boneindices.md)
  The semantic for bone index data, used for skeletal animation of skinned surfaces.
- [static let boneWeights: SCNGeometrySource.Semantic](./semantic-swift.struct/boneweights.md)
  The semantic for bone weight data, used for skeletal animation of skinned surfaces.
### Initializers
- [init(String)](./semantic-swift.struct/init%28_%29.md)
- [init(rawValue: String)](./semantic-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometrysource/semantic-swift.struct)*