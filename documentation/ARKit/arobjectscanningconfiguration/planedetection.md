# planeDetection

**Framework**: ARKit  
**Kind**: property

A value specifying whether and how the session attempts to automatically detect flat surfaces in the camera-captured image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var planeDetection: ARWorldTrackingConfiguration.PlaneDetection { get set }
```

#### Discussion

By default, plane detection is off. If you enable [`horizontal`](arworldtrackingconfiguration/planedetection-swift.struct/horizontal.md) or [`vertical`](arworldtrackingconfiguration/planedetection-swift.struct/vertical.md) plane detection, the session adds [`ARPlaneAnchor`](arplaneanchor.md) objects and notifies your [`ARSessionDelegate`](arsessiondelegate.md), [`ARSCNViewDelegate`](arscnviewdelegate.md), or [`ARSKViewDelegate`](arskviewdelegate.md) object whenever its analysis of captured video images detects an area that appears to be a flat surface.

In an object-scanning session, you can use detected planes to help determine where the origin (anchor point) for a scanned object should be relative to its extent.

## See Also

- [ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arobjectscanningconfiguration/planedetection)*