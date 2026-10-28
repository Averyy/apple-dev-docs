# concavePolyhedron

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

The physics shape is a concave polyhedron closely following the surface of the geometry.

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
static let concavePolyhedron: SCNPhysicsShape.ShapeType
```

```c
extern SCNPhysicsShapeType const SCNPhysicsShapeTypeConcavePolyhedron;
```

## Discussion

This option provides the highest level of detail, at a high cost to simulation performance. Use it only for irregularly shaped bodies where precise collision behavior is crucial to your app’s design.

This shape type may only be used for static physics bodies (that is, those whose [`type`](../../scnphysicsbody/type.md) property is [`SCNPhysicsBodyType.static`](../../scnphysicsbodytype/static.md)).

## See Also

### Type Properties
- [static let boundingBox: SCNPhysicsShape.ShapeType](./boundingbox.md)
  The physics shape is the smallest box containing the geometry.
- [static let convexHull: SCNPhysicsShape.ShapeType](./convexhull.md)
  The physics shape is a convex polyhedron roughly enclosing the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/shapetype/concavepolyhedron)*