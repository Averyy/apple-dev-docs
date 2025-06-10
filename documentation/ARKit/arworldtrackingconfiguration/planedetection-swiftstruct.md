# ARWorldTrackingConfiguration.PlaneDetection

**Framework**: ARKit  
**Kind**: struct

Options for whether and how the framework detects flat surfaces in captured images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct PlaneDetection
```

#### Overview

By default, this configuration disables plane detection. If you enable horizontal or vertical plane detection, the session adds ARPlaneAnchor objects and notifies your ARSessionDelegate, ARSCNViewDelegate, or ARSKViewDelegate object when its analysis of captured video images detects an area that appears to be a flat surface.

Use an empty set literal `[]` to specify no plane detection.

## Topics

### Plane Detection Option Creation
- [init(rawValue: UInt)](arworldtrackingconfiguration/planedetection-swift.struct/init(rawvalue:).md)
  Creates plane detection options.
### Plane Detection Options
- [static var horizontal: ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct/horizontal.md)
  The session detects planar surfaces that are perpendicular to gravity.
- [static var vertical: ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct/vertical.md)
  The session detects surfaces that are parallel to gravity, regardless of other orientation.
- [static var horizontal: ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct/horizontal.md)
  The session detects planar surfaces that are perpendicular to gravity.
- [static var vertical: ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct/vertical.md)
  The session detects surfaces that are parallel to gravity, regardless of other orientation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](arbodytrackingconfiguration/planedetection.md)
  A value specifying whether and how the session attempts to automatically detect flat surfaces in the camera-captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/planedetection-swift.struct)*