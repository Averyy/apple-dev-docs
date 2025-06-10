# textureCoordinates(withMappingChannel:)

**Framework**: SceneKit  
**Kind**: method

Returns the texture coordinates at the point of intersection for the specified texture mapping channel.

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
func textureCoordinates(withMappingChannel channel: Int) -> CGPoint
```

#### Return Value

The texture coordinates at the point of intersection, or [`CGPointZero`](https://developer.apple.com/documentation/CoreGraphics/CGPointZero) if the geometry does not have a texture coordinate source for the specified channel.

#### Discussion

An [`SCNGeometry`](scngeometry.md) object can contain multiple sources of texture coordinates, or texture mapping channels. (With multiple channels, you can map texture images for different material properties in different ways.) To use the texture coordinates of a hit-test result, specify which texture coordinate source to look up coordinates in.

For example, to add “scorch marks” to a game character hit by a laser, you might modify a texture image mapped to the [`multiply`](scnmaterial/multiply.md) property of the geometry’s material. Use the [`mappingChannel`](scnmaterialproperty/mappingchannel.md) index from that material property as the `channel` parameter when calling [`textureCoordinates(withMappingChannel:)`](scnhittestresult/texturecoordinates(withmappingchannel:).md) to ensure that you modify the correct location in the texture image.

## Parameters

- `channel`: The index of the mapping channel in which to look up texture coordinates.

## See Also

- [var node: SCNNode](scnhittestresult/node.md)
  The node whose geometry intersects the search ray.
- [var geometryIndex: Int](scnhittestresult/geometryindex.md)
  The index of the geometry element whose surface the search ray intersects.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestresult/texturecoordinates(withmappingchannel:))*