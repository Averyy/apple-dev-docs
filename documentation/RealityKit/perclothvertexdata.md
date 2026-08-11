# PerClothVertexData

**Framework**: RealityKit  
**Kind**: struct

A generic type that stores per-vertex data in a buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct PerClothVertexData<ElementType>
```

## Topics

### Accessing vertex data
- [var vertexCount: Int](perclothvertexdata/vertexcount.md)
  The number of vertices this structure holds data for.
- [func withElements<Result>((Span<ElementType>) -> Result) -> Result](perclothvertexdata/withelements(_:).md)
  Provides read-only access to the per-vertex data within a callback.
- [func withMutableElements<Result>((inout MutableSpan<ElementType>) -> Result) -> Result](perclothvertexdata/withmutableelements(_:).md)
  Provides mutable access to the per-vertex data within a callback.
### Setting vertex values
- [func set(vertexIndices: [UInt32], value: ElementType)](perclothvertexdata/set(vertexindices:value:).md)
  Sets the data for the given vertex indices to a common value.
- [func setAll(value: ElementType)](perclothvertexdata/setall(value:).md)
  Sets the data for all vertices to a common value.
- [func reset()](perclothvertexdata/reset-1nlsc.md)
  Resets the per-vertex data of each vertex to the default position constraint.
- [func reset()](perclothvertexdata/reset-403m8.md)
  Resets the per-vertex data of each vertex to a zero-force external force.
- [func reset()](perclothvertexdata/reset-4x5xi.md)
  Resets the per-vertex data of each vertex to the default motion type.
### Instance Methods
- [func reset()](perclothvertexdata/reset.md)
  Resets the per-vertex data of each vertex to the default position constraint.

## See Also

- [struct ClothSimulationComponent](clothsimulationcomponent.md)
  A component that marks an entity as the simulation root of a localized cloth simulation.
- [struct ClothBodyComponent](clothbodycomponent.md)
  A component that simulates an entity as a deformable cloth body, when part of a cloth simulation.
- [struct ClothBodyMaterial](clothbodymaterial.md)
  A struct that represents a cloth body’s material.
- [struct ClothGrabComponent](clothgrabcomponent.md)
  A component that grabs and drags particles of cloth bodies using either a ray or a volume, as determined by the `mode` property.
- [struct ClothForceVolumeComponent](clothforcevolumecomponent.md)
  A component that creates a force volume applying forces to any intersecting cloth body particles.
- [struct ClothQueryVolumeComponent](clothqueryvolumecomponent.md)
  A component that defines a volume for querying particles of cloth bodies.
- [struct ClothCoordinateSpace](clothcoordinatespace.md)
  Defines a reference frame within a cloth simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perclothvertexdata)*