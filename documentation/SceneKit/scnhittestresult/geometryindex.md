# geometryIndex

**Framework**: SceneKit  
**Kind**: property

The index of the geometry element whose surface the search ray intersects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var geometryIndex: Int { get }
```

#### Discussion

Every [`SCNGeometry`](scngeometry.md) object contains one or more [`SCNGeometryElement`](scngeometryelement.md) objects that define how its vertices connect to form a surface. This property provides the index of the geometry element intersecting the search ray. For more information about that geometry element, use the geometry’s [`element(at:)`](scngeometry/element(at:).md) method.

## See Also

- [var node: SCNNode](scnhittestresult/node.md)
  The node whose geometry intersects the search ray.
- [var faceIndex: Int](scnhittestresult/faceindex.md)
  The index of the primitive in the geometry element intersected by the search ray.
- [var localCoordinates: SCNVector3](scnhittestresult/localcoordinates.md)
  The point of intersection between the geometry and the search ray, in the local coordinate system of the node containing the geometry.
- [var worldCoordinates: SCNVector3](scnhittestresult/worldcoordinates.md)
  The point of intersection between the geometry and the search ray, in the scene’s world coordinate system.
- [var localNormal: SCNVector3](scnhittestresult/localnormal.md)
  The surface normal vector at the point of intersection, in the local coordinate system of the node containing the geometry intersected by the search ray.
- [var worldNormal: SCNVector3](scnhittestresult/worldnormal.md)
  The surface normal vector at the point of intersection, in the scene’s world coordinate system.
- [var modelTransform: SCNMatrix4](scnhittestresult/modeltransform.md)
  The world transform matrix of the node containing the intersection.
- [func textureCoordinates(withMappingChannel: Int) -> CGPoint](scnhittestresult/texturecoordinates(withmappingchannel:).md)
  Returns the texture coordinates at the point of intersection for the specified texture mapping channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestresult/geometryindex)*