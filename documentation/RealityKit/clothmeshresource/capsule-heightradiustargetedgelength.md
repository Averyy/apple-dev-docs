# capsule(height:radius:targetEdgeLength:)

**Framework**: RealityKit  
**Kind**: method

Creates a capsule mesh with a topology suitable for cloth simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func capsule(height: Float, radius: Float, targetEdgeLength: Float = defaultTargetEdgeLength) throws -> Self
```

#### Return Value

The generated capsule mesh resource.

#### Discussion

- height: The height of the cylinder portion of the capsule, in meters. The total capsule height is `height + 2 * radius`.
- radius: The radius of the body and the caps of the generated capsule, in meters.
- targetEdgeLength: The targeted average edge length for the generated mesh, in meters. The generated mesh will contain edges with a length as close as possible to this.

## See Also

- [convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32]) throws](clothmeshresource/init(positions:triangleindices:).md)
  Creates a cloth mesh resource from the given vertex positions and triangle indices.
- [static func patch(size: SIMD2<Float>, targetEdgeLength: Float) throws -> Self](clothmeshresource/patch(size:targetedgelength:).md)
  Creates a rectangular patch mesh with a topology suitable for cloth simulation.
- [static func box(size: SIMD3<Float>, targetEdgeLength: Float) throws -> Self](clothmeshresource/box(size:targetedgelength:).md)
  Creates a box mesh with a topology suitable for cloth simulation.
- [static func sphere(radius: Float, targetEdgeLength: Float) throws -> Self](clothmeshresource/sphere(radius:targetedgelength:).md)
  Creates a sphere mesh with a topology suitable for cloth simulation.
- [static func cylinder(height: Float, radius: Float, withCaps: Bool, targetEdgeLength: Float) throws -> Self](clothmeshresource/cylinder(height:radius:withcaps:targetedgelength:).md)
  Creates a cylinder mesh with a topology suitable for cloth simulation.
- [static let defaultTargetEdgeLength: Float](clothmeshresource/defaulttargetedgelength.md)
  Default target edge length for mesh generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource/capsule(height:radius:targetedgelength:))*