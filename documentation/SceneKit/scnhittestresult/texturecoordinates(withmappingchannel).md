# textureCoordinates(withMappingChannel:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Returns the texture coordinates at the point of intersection for the specified texture mapping channel.

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
func textureCoordinates(withMappingChannel channel: Int) -> CGPoint
```

```objc
- (CGPoint) textureCoordinatesWithMappingChannel:(NSInteger) channel;
```

## Return Value

The texture coordinates at the point of intersection, or [`CGPointZero`](../../CoreGraphics/cgpointzero.md) if the geometry does not have a texture coordinate source for the specified channel.

## Discussion

An [`SCNGeometry`](../scngeometry.md) object can contain multiple sources of texture coordinates, or texture mapping channels. (With multiple channels, you can map texture images for different material properties in different ways.) To use the texture coordinates of a hit-test result, specify which texture coordinate source to look up coordinates in.

For example, to add “scorch marks” to a game character hit by a laser, you might modify a texture image mapped to the [`multiply`](../scnmaterial/multiply.md) property of the geometry’s material. Use the [`mappingChannel`](../scnmaterialproperty/mappingchannel.md) index from that material property as the `channel` parameter when calling [`textureCoordinates(withMappingChannel:)`](./texturecoordinates%28withmappingchannel%29.md) to ensure that you modify the correct location in the texture image.

## Parameters

- `channel`: The index of the mapping channel in which to look up texture coordinates.

## See Also

### Retrieving Information About a Hit-Test Result
- [var node: SCNNode](./node.md)
  The node whose geometry intersects the search ray.
- [var geometryIndex: Int](./geometryindex.md)
  The index of the geometry element whose surface the search ray intersects.
- [var faceIndex: Int](./faceindex.md)
  The index of the primitive in the geometry element intersected by the search ray.
- [var localCoordinates: SCNVector3](./localcoordinates.md)
  The point of intersection between the geometry and the search ray, in the local coordinate system of the node containing the geometry.
- [var worldCoordinates: SCNVector3](./worldcoordinates.md)
  The point of intersection between the geometry and the search ray, in the scene’s world coordinate system.
- [var localNormal: SCNVector3](./localnormal.md)
  The surface normal vector at the point of intersection, in the local coordinate system of the node containing the geometry intersected by the search ray.
- [var worldNormal: SCNVector3](./worldnormal.md)
  The surface normal vector at the point of intersection, in the scene’s world coordinate system.
- [var modelTransform: SCNMatrix4](./modeltransform.md)
  The world transform matrix of the node containing the intersection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestresult/texturecoordinates(withmappingchannel:))*