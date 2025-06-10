# MeshResource.ShapeExtrusionOptions.ExtrusionMethod.traceTransforms(_:)

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
case traceTransforms([simd_float4x4])
```

#### Discussion

The swept shape (e.g. the 2D path provided in `MeshResource(extruding: Path)`, or text) is instantiated at each of the provided transforms.  Each instance is joined together by a strip of geometry. You can specify a different rotation of the swept shape for each point on the curve with `traceTransforms`.

For example, extrude a rounded square along the z-axis while zig-zagging in the y-axis, using the default rotation throughout. This creates a mesh where the swept shapes have the same orientation.

```swift
// Positions in a zig-zag pattern.
let positions: [SIMD3<Float>] = [
    [0,    0,   0],
    [0, -0.1, 0.2],
    [0,    0, 0.4],
    [0, -0.1, 0.6]
]

var extrusionOptions = ShapeExtrusionOptions()
extrusionOptions.extrusionMethod = .traceTransforms(
    positions.map { position in
        Transform(translation: position).matrix
    }
)
```

![None](https://docs-assets.developer.apple.com/published/c6f16e2949accc8f0c48a62dd6a502ee/generateExtrudedShape-extrusionMethod-traceTransforms-red.jpg)

You can also add a rotation for each point in the collection. For example, use the index to rotate the angle by `.pi / 6` in the z-axis for each position.

```swift
extrusionOptions.extrusionMethod = .traceTransforms(
    positions.enumerated().map { index, position in
        Transform(
            rotation: simd_quatf(
                // Increase the angle depending on index.
                angle: Float(index) * .pi / 6, axis: [0, 0, 1]
            ),
            translation: position
        ).matrix
    }
)
```

![None](https://docs-assets.developer.apple.com/published/24dbfe6b4dc3bc4560e39fc4f925a335/generateExtrudedShape-extrusionMethod-traceTransforms-red-rotated.jpg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions-3sc8p/extrusionmethod-swift.enum/tracetransforms(_:))*