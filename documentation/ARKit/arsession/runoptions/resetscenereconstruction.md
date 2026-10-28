# resetSceneReconstruction

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

An option to reset the scene mesh.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
static var resetSceneReconstruction: ARSession.RunOptions { get }
```

```c
ARSessionRunOptionResetSceneReconstruction
```

## Discussion

When you reset scene reconstruction, ARKit removes any existing mesh anchors ([`ARMeshAnchor`](../../armeshanchor.md)) from the session.

## See Also

### Run Options
- [static var resetTracking: ARSession.RunOptions](./resettracking.md)
  An option to reset the device’s position from the session’s previous run.
- [static var removeExistingAnchors: ARSession.RunOptions](./removeexistinganchors.md)
  An option to remove any anchor objects associated with the session’s previous run.
- [static var stopTrackedRaycasts: ARSession.RunOptions](./stoptrackedraycasts.md)
  An option to stop all active tracked raycasts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runoptions/resetscenereconstruction)*