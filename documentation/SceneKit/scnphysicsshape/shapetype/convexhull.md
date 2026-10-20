# convexHull

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The physics shape is a convex polyhedron roughly enclosing the geometry.

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
static let convexHull: SCNPhysicsShape.ShapeType
```

```c
extern SCNPhysicsShapeType const SCNPhysicsShapeTypeConvexHull;
```

#### Discussion

This option provides a moderate level of detail and simulation performance. Use it for rounded or irregularly shaped physics bodies.

## See Also

### Type Properties
- [static let boundingBox: SCNPhysicsShape.ShapeType](./boundingbox.md)
  The physics shape is the smallest box containing the geometry.
- [static let concavePolyhedron: SCNPhysicsShape.ShapeType](./concavepolyhedron.md)
  The physics shape is a concave polyhedron closely following the surface of the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/shapetype/convexhull)*