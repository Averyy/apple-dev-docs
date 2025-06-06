# sceneReconstruction

**Framework**: ARKit  
**Kind**: property

A flag that enables scene reconstruction.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var sceneReconstruction: ARConfiguration.SceneReconstruction { get set }
```

#### Discussion

When you enable scene reconstruction, ARKit provides a polygonal mesh that estimates the shape of the physical environment. Before setting this property, call [`supportsSceneReconstruction(_:)`](arworldtrackingconfiguration/supportsscenereconstruction(_:).md) to ensure device support. For a sample app that demonstrates scene reconstruction, see [`Visualizing and interacting with a reconstructed scene`](visualizing-and-interacting-with-a-reconstructed-scene.md).

If you enable plane detection, ARKit applies that information to the mesh. Where the LiDAR scanner may produce a slightly uneven mesh on a real-world surface, ARKit smooths out the mesh where it detects a plane on that surface.

If you enable people occlusion, ARKit adjusts the mesh according to any people it detects in the camera feed. ARKit removes any part of the scene mesh that overlaps with people, as defined by the [`personSegmentation`](arconfiguration/framesemantics-swift.struct/personsegmentation.md) or [`personSegmentationWithDepth`](arconfiguration/framesemantics-swift.struct/personsegmentationwithdepth.md) frame semantics.

## See Also

- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.property.md)
  The configuration’s plane detection options.
- [ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.
- [class func supportsSceneReconstruction(ARConfiguration.SceneReconstruction) -> Bool](arworldtrackingconfiguration/supportsscenereconstruction(_:).md)
  Checks if the device supports scene reconstruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/scenereconstruction)*