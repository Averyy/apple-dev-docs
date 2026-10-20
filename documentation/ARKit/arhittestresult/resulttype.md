# ARHitTestResult.ResultType

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Possible types for specifying a hit-test search, or for the result of a hit-test search.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
struct ResultType
```

```c
enum ARHitTestResultType : NSUInteger;
```

## Topics

### Creating a Result Type
- [init(rawValue: UInt)](./resulttype/init%28rawvalue%29.md)
  Creates a result type.
### Result Types
- [static var featurePoint: ARHitTestResult.ResultType](./resulttype/featurepoint.md)
  A point on a surface detected by ARKit, but not part of any detected planes.
- [static var estimatedHorizontalPlane: ARHitTestResult.ResultType](./resulttype/estimatedhorizontalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is perpendicular to gravity.
- [static var estimatedVerticalPlane: ARHitTestResult.ResultType](./resulttype/estimatedverticalplane.md)
  A point on a real-world planar surface detected during the search, whose orientation is parallel to gravity.
- [static var existingPlane: ARHitTestResult.ResultType](./resulttype/existingplane.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../arworldtrackingconfiguration/planedetection-swift.property.md) option), without considering the plane’s size.
- [static var existingPlaneUsingExtent: ARHitTestResult.ResultType](./resulttype/existingplaneusingextent.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size.
- [static var existingPlaneUsingGeometry: ARHitTestResult.ResultType](./resulttype/existingplaneusinggeometry.md)
  A point on a real-world plane (already detected with the [`planeDetection`](../arworldtrackingconfiguration/planedetection-swift.property.md) option), respecting the plane’s estimated size and shape.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Identifying Results
- [var type: ARHitTestResult.ResultType](./type.md)
  The kind of detected feature the search result represents.
- [var anchor: ARAnchor?](./anchor.md)
  The anchor representing the detected surface, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult/resulttype)*