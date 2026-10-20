# existingPlane

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), without considering the plane’s size.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
static var existingPlane: ARHitTestResult.ResultType { get }
```

```c
ARHitTestResultTypeExistingPlane
```

#### Discussion

When searching for this result type, ARKit can return any point coplanar with an already detected plane, regardless of whether that plane’s already detected [`extent`](../../arplaneanchor/extent.md) or [`geometry`](../../arplaneanchor/geometry.md) includes that point. (That is, this result type searches the infinite extensions of detected planes.)

An existing plane search can return any number of results, depending on how many already-detected planes the hit test ray intersects (if any).

## See Also

### Result Types
- [static var featurePoint: ARHitTestResult.ResultType](./featurepoint.md)
  A point on a surface detected by ARKit, but not part of any detected planes.
- [static var estimatedHorizontalPlane: ARHitTestResult.ResultType](./estimatedhorizontalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is perpendicular to gravity.
- [static var estimatedVerticalPlane: ARHitTestResult.ResultType](./estimatedverticalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is parallel to gravity.
- [static var existingPlaneUsingExtent: ARHitTestResult.ResultType](./existingplaneusingextent.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size.
- [static var existingPlaneUsingGeometry: ARHitTestResult.ResultType](./existingplaneusinggeometry.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../../arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/resulttype/existingplane)*