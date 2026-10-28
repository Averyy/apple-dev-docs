# existingPlaneUsingExtent

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
static var existingPlaneUsingExtent: ARHitTestResult.ResultType { get }
```

```c
ARHitTestResultTypeExistingPlaneUsingExtent
```

## Discussion

When searching for this result type, ARKit returns a point coplanar with an already detected plane only if that point lies within the area defined by the plane’s [`center`](../../arplaneanchor/center.md) and [`extent`](../../arplaneanchor/extent.md) properties. Those properties (together with the anchor’s [`transform`](../../aranchor/transform.md)) define the smallest rectangular area that includes all regions ARKit estimates to be a part of the plane.

However, that rectangular area may contain regions that are not part of the same real-world surface. There may also be parts of the same real-world surface that lie outside the rectangle because ARKit has not yet recognized them as part of the same plane. You can get a more precise estimate of the plane area ARKit has recognized by testing with the [`existingPlaneUsingGeometry`](./existingplaneusinggeometry.md) type, or extend your hit test to an infinite plane with the [`existingPlane`](./existingplane.md) type.

An existing plane search can return any number of results, depending on how many already-detected planes the hit test ray intersects (if any).

## See Also

### Result Types
- [static var featurePoint: ARHitTestResult.ResultType](./featurepoint.md)
  A point on a surface detected by ARKit, but not part of any detected planes.
- [static var estimatedHorizontalPlane: ARHitTestResult.ResultType](./estimatedhorizontalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is perpendicular to gravity.
- [static var estimatedVerticalPlane: ARHitTestResult.ResultType](./estimatedverticalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is parallel to gravity.
- [static var existingPlane: ARHitTestResult.ResultType](./existingplane.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), without considering the plane’s size.
- [static var existingPlaneUsingGeometry: ARHitTestResult.ResultType](./existingplaneusinggeometry.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/resulttype/existingplaneusingextent)*