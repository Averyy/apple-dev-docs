# planeDetection

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The configuration’s plane detection options.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var planeDetection: ARWorldTrackingConfiguration.PlaneDetection { get set }
```

```objc
@property (nonatomic, assign) ARPlaneDetection planeDetection;
```

## Mentions

- [Displaying an AR Experience with Metal](../displaying-an-ar-experience-with-metal.md)
- [Understanding World Tracking](../understanding-world-tracking.md)

## Discussion

If set, new planes will continue to be detected and updated over time. Detected planes will be added to the session as [`ARPlaneAnchor`](../arplaneanchor.md) objects. In the event that two planes are merged, the newer plane will be removed. Defaults to `ARPlaneDetectionNone`.

## See Also

### Tracking Surfaces
- [ARWorldTrackingConfiguration.PlaneDetection](./planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.
- [var sceneReconstruction: ARConfiguration.SceneReconstruction](./scenereconstruction.md)
  A flag that enables scene reconstruction.
- [class func supportsSceneReconstruction(ARConfiguration.SceneReconstruction) -> Bool](./supportsscenereconstruction%28_%29.md)
  Checks if the device supports scene reconstruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/planedetection-swift.property)*