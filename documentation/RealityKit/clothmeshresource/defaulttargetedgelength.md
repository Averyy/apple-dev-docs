# defaultTargetEdgeLength

**Framework**: RealityKit  
**Kind**: property

Default target edge length for mesh generation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let defaultTargetEdgeLength: Float
```

#### Discussion

It is convenient to have the same target edge length for all shapes, since self-collision assumes similar edge lengths across the whole simulation.

## See Also

- [convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32]) throws](clothmeshresource/init(positions:triangleindices:).md)
  Creates a cloth mesh resource from the given vertex positions and triangle indices.
- [static func patch(size: SIMD2<Float>, targetEdgeLength: Float) throws -> Self](clothmeshresource/patch(size:targetedgelength:).md)
  Creates a rectangular patch mesh with a topology suitable for cloth simulation.
- [static func box(size: SIMD3<Float>, targetEdgeLength: Float) throws -> Self](clothmeshresource/box(size:targetedgelength:).md)
  Creates a box mesh with a topology suitable for cloth simulation.
- [static func sphere(radius: Float, targetEdgeLength: Float) throws -> Self](clothmeshresource/sphere(radius:targetedgelength:).md)
  Creates a sphere mesh with a topology suitable for cloth simulation.
- [static func capsule(height: Float, radius: Float, targetEdgeLength: Float) throws -> Self](clothmeshresource/capsule(height:radius:targetedgelength:).md)
  Creates a capsule mesh with a topology suitable for cloth simulation.
- [static func cylinder(height: Float, radius: Float, withCaps: Bool, targetEdgeLength: Float) throws -> Self](clothmeshresource/cylinder(height:radius:withcaps:targetedgelength:).md)
  Creates a cylinder mesh with a topology suitable for cloth simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/defaulttargetedgelength)*