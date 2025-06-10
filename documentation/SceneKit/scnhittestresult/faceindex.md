# faceIndex

**Framework**: SceneKit  
**Kind**: property

The index of the primitive in the geometry element intersected by the search ray.

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
var faceIndex: Int { get }
```

## See Also

- [var primitiveCount: Int](scngeometryelement/primitivecount.md)
  The number of primitives in the element.
- [var node: SCNNode](scnhittestresult/node.md)
  The node whose geometry intersects the search ray.
- [var geometryIndex: Int](scnhittestresult/geometryindex.md)
  The index of the geometry element whose surface the search ray intersects.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestresult/faceindex)*