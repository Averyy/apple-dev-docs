# convexHull

**Framework**: SceneKit  
**Kind**: property

The physics shape is a convex polyhedron roughly enclosing the geometry.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let convexHull: SCNPhysicsShape.ShapeType
```

#### Discussion

This option provides a moderate level of detail and simulation performance. Use it for rounded or irregularly shaped physics bodies.

## See Also

- [static let boundingBox: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/boundingbox.md)
  The physics shape is the smallest box containing the geometry.
- [static let concavePolyhedron: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/concavepolyhedron.md)
  The physics shape is a concave polyhedron closely following the surface of the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/shapetype/convexhull)*