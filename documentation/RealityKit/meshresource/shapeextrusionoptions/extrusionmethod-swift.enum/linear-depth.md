# MeshResource.ShapeExtrusionOptions.ExtrusionMethod.linear(depth:)

**Framework**: RealityKit  
**Kind**: case

Extrudes the shape with a linear extrusion in Z by the desired depth.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
case linear(depth: Float)
```

#### Discussion

For example an extrusion that has a linear depth of 0.6 meters:

```swift
var extrusionOptions = ShapeExtrusionOptions()
extrusionOptions.extrusionMethod = .linear(depth: 0.6)
```

![None](https://docs-assets.developer.apple.com/published/d5d20210240cb706420f789afe4bdf8e/generateExtrudedShape-extrusionMethod-linear-red.jpg)

You can also use [`MeshResource.ShapeExtrusionOptions.ExtrusionMethod.tracePositions(_:)`](meshresource/shapeextrusionoptions/extrusionmethod-swift.enum/tracepositions(_:).md) an equivalent way.

```swift
.tracePositions([
    [0, 0, -depth/2],
    [0, 0,  depth/2]
)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/shapeextrusionoptions/extrusionmethod-swift.enum/linear(depth:))*