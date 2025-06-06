# boundingBox

**Framework**: SceneKit  
**Kind**: property

The physics shape is the smallest box containing the geometry.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let boundingBox: SCNPhysicsShape.ShapeType
```

#### Discussion

This option provides the lowest level of detail and the fastest simulation performance. Use it for generally box-shaped physics bodies or when constructing a compound physics shape.

## See Also

- [static let concavePolyhedron: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/concavepolyhedron.md)
  The physics shape is a concave polyhedron closely following the surface of the geometry.
- [static let convexHull: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/convexhull.md)
  The physics shape is a convex polyhedron roughly enclosing the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/shapetype/boundingbox)*