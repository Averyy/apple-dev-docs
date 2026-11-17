# supportsSceneReconstruction(_:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Type Method

Checks if the device supports scene reconstruction.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
class func supportsSceneReconstruction(_ sceneReconstruction: ARConfiguration.SceneReconstruction) -> Bool
```

```objc
+ (BOOL) supportsSceneReconstruction:(ARSceneReconstruction) sceneReconstruction;
```

## Return Value

`YES` if the scene reconstruction type is supported on this device, `NO` otherwise.

## Discussion

Scene reconstruction requires a device with a LiDAR Scanner, such as the fourth-generation iPad Pro.

## Parameters

- `sceneReconstruction`: The scene reconstruction type to check for support.

## See Also

### Tracking Surfaces
- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](./planedetection-swift.property.md)
  The configuration’s plane detection options.
- [ARWorldTrackingConfiguration.PlaneDetection](./planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.
- [var sceneReconstruction: ARConfiguration.SceneReconstruction](./scenereconstruction.md)
  A flag that enables scene reconstruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/supportsscenereconstruction(_:))*