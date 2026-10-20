# boundingBox

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The physics shape is the smallest box containing the geometry.

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
static let boundingBox: SCNPhysicsShape.ShapeType
```

```c
extern SCNPhysicsShapeType const SCNPhysicsShapeTypeBoundingBox;
```

#### Discussion

This option provides the lowest level of detail and the fastest simulation performance. Use it for generally box-shaped physics bodies or when constructing a compound physics shape.

## See Also

### Type Properties
- [static let concavePolyhedron: SCNPhysicsShape.ShapeType](./concavepolyhedron.md)
  The physics shape is a concave polyhedron closely following the surface of the geometry.
- [static let convexHull: SCNPhysicsShape.ShapeType](./convexhull.md)
  The physics shape is a convex polyhedron roughly enclosing the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/shapetype/boundingbox)*