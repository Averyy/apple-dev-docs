# getBoundingSphereCenter:radius:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Gets the center point and radius of the object’s bounding sphere.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
- (BOOL) getBoundingSphereCenter:(SCNVector3 *) center radius:(CGFloat *) radius;
```

#### Return Value

[`true`](../../Swift/true.md) if the object has a nonzero volume; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Scene Kit defines a bounding sphere in the local coordinate space using a center point and a radius. For example, if a node’s bounding sphere has the center point `{3, 1, 4}` and radius `2.0`, all points in the vertex data of node’s geometry (and any geometry attached to its child nodes) lie within `2.0` units of the center point.

The coordinates provided by this method are valid only if the object has a volume to be measured. If called on a geometry containing no vertex data or a node containing no geometry (and whose child nodes, if any, contain no geometry), this method returns NO, indicating that the values `*center` and `*radius` are undefined.

## Parameters

- `center`: On output, the center point of the bounding sphere.
- `radius`: On output, the radius of the bounding sphere.

## See Also

### Measuring an Object’s Bounding Volume
- [- getBoundingBoxMin:max:](./getboundingboxmin_max_.md)
  Gets the minimum and maximum corner points of the object’s bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnboundingvolume/getboundingspherecenter:radius:)*