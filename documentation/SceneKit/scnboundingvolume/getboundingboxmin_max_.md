# getBoundingBoxMin:max:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Gets the minimum and maximum corner points of the object’s bounding box.

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
- (BOOL) getBoundingBoxMin:(SCNVector3 *) min max:(SCNVector3 *) max;
```

#### Return Value

[`true`](../../Swift/true.md) if the object has a nonzero volume; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Scene Kit defines a bounding box in the local coordinate space using two points identifying its corners, which implicitly determine six axis-aligned planes marking its limits. For example, if a geometry’s bounding box has the minimum corner `{-1, 0, 2}` and the maximum corner `{3, 4, 5}`, all points in the geometry’s vertex data have an x-coordinate value between `-1.0` and `3.0`, inclusive.

The coordinates provided by this method are valid only if the object has a volume to be measured. If called on a geometry containing no vertex data or a node containing no geometry (and whose child nodes, if any, contain no geometry), this method returns NO, indicating that the values `*min` and `*max` are undefined.

## Parameters

- `min`: On output, the minimum coordinates of the bounding box.
- `max`: On output, the maximum coordinates of the bounding box.

## See Also

### Measuring an Object’s Bounding Volume
- [- getBoundingSphereCenter:radius:](./getboundingspherecenter_radius_.md)
  Gets the center point and radius of the object’s bounding sphere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnboundingvolume/getboundingboxmin:max:)*