# planeDetection

**Framework**: ARKit  
**Kind**: property

A value specifying whether and how the session attempts to automatically detect flat surfaces in the camera-captured image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var planeDetection: ARWorldTrackingConfiguration.PlaneDetection { get set }
```

#### Discussion

By default, plane detection is off. If you enable [`horizontal`](arworldtrackingconfiguration/planedetection-swift.struct/horizontal.md) or [`vertical`](arworldtrackingconfiguration/planedetection-swift.struct/vertical.md) plane detection, the session adds [`ARPlaneAnchor`](arplaneanchor.md) objects and notifies your [`ARSessionDelegate`](arsessiondelegate.md), [`ARSCNViewDelegate`](arscnviewdelegate.md), or [`ARSKViewDelegate`](arskviewdelegate.md) object whenever its analysis of captured video images detects an area that appears to be a flat surface.

## See Also

- [ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodytrackingconfiguration/planedetection)*