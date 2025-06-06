# estimatedVerticalPlane

**Framework**: ARKit  
**Kind**: property

A point on a real-world planar surface detected during the search, whose orientation is parallel to gravity.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
static var estimatedVerticalPlane: ARHitTestResult.ResultType { get }
```

#### Discussion

ARKit provides two ways to locate real-world flat surfaces in a scene.  (enabled with [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) on your session configuration) is an ongoing process, continuously analyzing the scene to accurately map the position and extent of any planes in view. Because plane detection takes time, you can fall back to  to get an instant, but less accurate, indication of whether a 2D point in the camera image corresponds to a real-world flat surface.

Because plane detection results are more accurate than plane estimation results, ARKit prefers the former when searching for both. If your hit-test search includes both [`estimatedVerticalPlane`](arhittestresult/resulttype/estimatedverticalplane.md) and one or more [`existingPlane`](arhittestresult/resulttype/existingplane.md) types, and the search finds any already detected plane anchors, the search returns only the existing plane(s) and no estimated plane.

An estimated plane search returns at most one result—the best estimate for a vertical plane intersecting the hit-test ray.

## See Also

- [static var featurePoint: ARHitTestResult.ResultType](arhittestresult/resulttype/featurepoint.md)
  A point on a surface detected by ARKit, but not part of any detected planes.
- [static var estimatedHorizontalPlane: ARHitTestResult.ResultType](arhittestresult/resulttype/estimatedhorizontalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is perpendicular to gravity.
- [static var existingPlane: ARHitTestResult.ResultType](arhittestresult/resulttype/existingplane.md)
  A point on a real-world plane (already detected with the [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) option), without considering the plane’s size.
- [static var existingPlaneUsingExtent: ARHitTestResult.ResultType](arhittestresult/resulttype/existingplaneusingextent.md)
  A point on a real-world plane (already detected with the [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size.
- [static var existingPlaneUsingGeometry: ARHitTestResult.ResultType](arhittestresult/resulttype/existingplaneusinggeometry.md)
  A point on a real-world plane (already detected with the [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/resulttype/estimatedverticalplane)*