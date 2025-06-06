# concavePolyhedron

**Framework**: SceneKit  
**Kind**: property

The physics shape is a concave polyhedron closely following the surface of the geometry.

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
static let concavePolyhedron: SCNPhysicsShape.ShapeType
```

#### Discussion

This option provides the highest level of detail, at a high cost to simulation performance. Use it only for irregularly shaped bodies where precise collision behavior is crucial to your app’s design.

This shape type may only be used for static physics bodies (that is, those whose [`type`](scnphysicsbody/type.md) property is [`SCNPhysicsBodyType.static`](scnphysicsbodytype/static.md)).

## See Also

- [static let boundingBox: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/boundingbox.md)
  The physics shape is the smallest box containing the geometry.
- [static let convexHull: SCNPhysicsShape.ShapeType](scnphysicsshape/shapetype/convexhull.md)
  The physics shape is a convex polyhedron roughly enclosing the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/shapetype/concavepolyhedron)*