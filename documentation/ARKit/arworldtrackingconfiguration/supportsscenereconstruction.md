# supportsSceneReconstruction(_:)

**Framework**: ARKit  
**Kind**: method

Checks if the device supports scene reconstruction.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
class func supportsSceneReconstruction(_ sceneReconstruction: ARConfiguration.SceneReconstruction) -> Bool
```

#### Discussion

Scene reconstruction requires a device with a LiDAR Scanner, such as the fourth-generation iPad Pro.

## See Also

- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.property.md)
  The configuration’s plane detection options.
- [ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.
- [var sceneReconstruction: ARConfiguration.SceneReconstruction](arworldtrackingconfiguration/scenereconstruction.md)
  A flag that enables scene reconstruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/supportsscenereconstruction(_:))*