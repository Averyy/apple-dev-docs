# setBoundingBoxMin:max:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Sets a custom bounding box for the object.

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
- (void) setBoundingBoxMin:(SCNVector3 *) min max:(SCNVector3 *) max;
```

## Discussion

You define a bounding box in the local coordinate space using two points identifying its corners, which implicitly determine six axis-aligned planes marking its limits. The x-, y-, and z-coordinate values of any point in the volume are each greater than those of the `min` point and less than those of the `max` point.

By default, Scene Kit automatically computes the bounding volumes of nodes and geometries and uses this information to assist in rendering. You use this method to override the default bounding box.

## Parameters

- `min`: A pointer to the minimum coordinates of the bounding box.
- `max`: A pointer to the maximum coordinates of the bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnboundingvolume/setboundingboxmin:max:)*