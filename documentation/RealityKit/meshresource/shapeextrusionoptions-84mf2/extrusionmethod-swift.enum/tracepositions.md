# MeshResource.ShapeExtrusionOptions.ExtrusionMethod.tracePositions(_:)

**Framework**: RealityKit  
**Kind**: case

Extrudes the shape by sweeping it along a piecewise-linear curve.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
case tracePositions([SIMD3<Float>])
```

#### Discussion

The curve is defined as the set of line segments For each edge in the provided curve, the swept shape (e.g. the 2D path provided in `MeshResource(extruding: Path)`, or text) will be instantiated at the edge’s endpoints. Each instance of the swept shape will be joined together by a strip of geometry.

The positions are traced in such a way as to avoid twist in the generated 3D shape.  When possible, the local y-axis of the swept (2D) shape will be aligned with the y-axis of the generated 3D shape.

For example, extrude a rounded square along the z-axis, while zig-zagging in the y-axis:

```swift
// Positions in a zig-zag pattern.
let positions: [SIMD3<Float>] = [
    [0,    0,   0],
    [0, -0.1, 0.2],
    [0,    0, 0.4],
    [0, -0.1, 0.6]
]

var extrusionOptions = ShapeExtrusionOptions()
extrusionOptions.extrusionMethod = .tracePositions(positions)
```

![None](https://docs-assets.developer.apple.com/published/93b88510bd5a9d355fd94f15be445ac8/generateExtrudedShape-extrusionMethod-tracePositions-red.jpg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions-84mf2/extrusionmethod-swift.enum/tracepositions(_:))*