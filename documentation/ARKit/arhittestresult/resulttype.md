# ARHitTestResult.ResultType

**Framework**: ARKit  
**Kind**: struct

Possible types for specifying a hit-test search, or for the result of a hit-test search.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct ResultType
```

## Topics

### Creating a Result Type
- [init(rawValue: UInt)](arhittestresult/resulttype/init(rawvalue:).md)
  Creates a result type.
### Result Types
- [static var featurePoint: ARHitTestResult.ResultType](arhittestresult/resulttype/featurepoint.md)
  A point on a surface detected by ARKit, but not part of any detected planes.
- [static var estimatedHorizontalPlane: ARHitTestResult.ResultType](arhittestresult/resulttype/estimatedhorizontalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is perpendicular to gravity.
- [static var estimatedVerticalPlane: ARHitTestResult.ResultType](arhittestresult/resulttype/estimatedverticalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is parallel to gravity.
- [static var existingPlane: ARHitTestResult.ResultType](arhittestresult/resulttype/existingplane.md)
  A point on a real-world plane (already detected with the [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) option), without considering the plane’s size.
- [static var existingPlaneUsingExtent: ARHitTestResult.ResultType](arhittestresult/resulttype/existingplaneusingextent.md)
  A point on a real-world plane (already detected with the [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size.
- [static var existingPlaneUsingGeometry: ARHitTestResult.ResultType](arhittestresult/resulttype/existingplaneusinggeometry.md)
  A point on a real-world plane (already detected with the [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size and shape.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var type: ARHitTestResult.ResultType](arhittestresult/type.md)
  The kind of detected feature the search result represents.
- [var anchor: ARAnchor?](arhittestresult/anchor.md)
  The anchor representing the detected surface, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/resulttype)*