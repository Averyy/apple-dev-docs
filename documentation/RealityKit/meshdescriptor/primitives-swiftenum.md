# MeshDescriptor.Primitives

**Framework**: RealityKit  
**Kind**: enum

Indicates which primitive shape type a mesh applies to its vertex indices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
enum Primitives
```

## Topics

### Enumeration Cases
- [MeshDescriptor.Primitives.polygons(_:_:)](meshdescriptor/primitives-swift.enum/polygons(_:_:).md)
  Defines one or more triangles and quadrilaterals with two separate arrays of indices.
- [MeshDescriptor.Primitives.triangles(_:)](meshdescriptor/primitives-swift.enum/triangles(_:).md)
  Defines one or more triangles with an integer array of indices.
- [MeshDescriptor.Primitives.trianglesAndQuads(triangles:quads:)](meshdescriptor/primitives-swift.enum/trianglesandquads(triangles:quads:).md)
  Defines separate arrays for triangle and quad indices.

## See Also

- [struct MeshDescriptor](meshdescriptor.md)
  Defines a 3D mesh’s structure and data.
- [MeshDescriptor.Materials](meshdescriptor/materials-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdescriptor/primitives-swift.enum)*