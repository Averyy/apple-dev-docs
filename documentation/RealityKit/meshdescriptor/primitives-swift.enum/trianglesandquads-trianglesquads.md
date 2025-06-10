# MeshDescriptor.Primitives.trianglesAndQuads(triangles:quads:)

**Framework**: RealityKit  
**Kind**: case

Defines separate arrays for triangle and quad indices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case trianglesAndQuads(triangles: [UInt32], quads: [UInt32])
```

#### Discussion

The elements of the first array have three vertex indices for each triangle. The elements of the first array have four vertex indices for each quadrilateral.

For example, you can define three triangles with 9 vertex indices in the first array, and two quadrilaterals with 8 vertex indices in the second array.

```swift
.trianglesAndQuads(
    triangles: [0, 1, 2, 7, 8, 9, 42, 43, 44],
    quads: [3, 4, 5, 6, 10, 11, 12, 13]
)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdescriptor/primitives-swift.enum/trianglesandquads(triangles:quads:))*