# MeshDescriptor.Primitives.polygons(_:_:)

**Framework**: RealityKit  
**Kind**: case

Defines one or more triangles and quadrilaterals with two separate arrays of indices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
case polygons([UInt8], [UInt32])
```

#### Discussion

Each element in the first array represents a polygon and the element’s value indicates how many vertices in that polygon. The elements in the second array are the vertex indices for the polygons.

For example, to represent a triangle and a quadrilateral the first array has the elements `3` and `4`, and the second array has a total of 7 elements, one for every vertex in both polygons.

```swift
.polygons([3, 4], [
    0, 1, 2,
    3, 4, 5, 6
])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdescriptor/primitives-swift.enum/polygons(_:_:))*