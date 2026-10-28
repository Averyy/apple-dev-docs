# featurePoint

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

A point on a surface detected by ARKit, but not part of any detected planes.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
static var featurePoint: ARHitTestResult.ResultType { get }
```

```c
ARHitTestResultTypeFeaturePoint
```

## Discussion

During a world-tracking AR session, ARKit builds a coarse point cloud representing its rough understanding of the 3D world around the user (see [`rawFeaturePoints`](../../arframe/rawfeaturepoints.md)). Individual feature points represent parts of the camera image likely to be part of a real-world surface, but not necessarily a planar surface.

When you search using this hit-test option, ARKit finds the feature point nearest to the hit-test ray (the extension of the 2D hit-test point into 3D world space), then returns the point on the ray nearest to that feature point.

## See Also

### Result Types
- [static var estimatedHorizontalPlane: ARHitTestResult.ResultType](./estimatedhorizontalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is perpendicular to gravity.
- [static var estimatedVerticalPlane: ARHitTestResult.ResultType](./estimatedverticalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is parallel to gravity.
- [static var existingPlane: ARHitTestResult.ResultType](./existingplane.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), without considering the plane’s size.
- [static var existingPlaneUsingExtent: ARHitTestResult.ResultType](./existingplaneusingextent.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size.
- [static var existingPlaneUsingGeometry: ARHitTestResult.ResultType](./existingplaneusinggeometry.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/resulttype/featurepoint)*