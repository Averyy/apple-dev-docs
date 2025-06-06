# boundingSphere

**Framework**: SceneKit  
**Kind**: property

The center point and radius of the object’s bounding sphere.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var boundingSphere: (center: SCNVector3, radius: Float) { get }
```

#### Discussion

Scene Kit defines a bounding sphere in the local coordinate space using a center point and a radius. For example, if a node’s bounding sphere has the center point `{3, 1, 4}` and radius `2.0`, all points in the vertex data of node’s geometry (and any geometry attached to its child nodes) lie within `2.0` units of the center point.

The coordinates provided when reading this property are valid only if the object has a volume to be measured. For a geometry containing no vertex data or a node containing no geometry (and whose child nodes, if any, contain no geometry), the values `center` and `radius` are both zero.

## See Also

- [var boundingBox: (min: SCNVector3, max: SCNVector3)](scnboundingvolume/boundingbox.md)
  The minimum and maximum corner points of the object’s bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnboundingvolume/boundingsphere)*