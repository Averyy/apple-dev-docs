# resetSceneReconstruction

**Framework**: ARKit  
**Kind**: property

An option to reset the scene mesh.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var resetSceneReconstruction: ARSession.RunOptions { get }
```

#### Discussion

When you reset scene reconstruction, ARKit removes any existing mesh anchors ([`ARMeshAnchor`](armeshanchor.md)) from the session.

## See Also

- [static var resetTracking: ARSession.RunOptions](arsession/runoptions/resettracking.md)
  An option to reset the device’s position from the session’s previous run.
- [static var removeExistingAnchors: ARSession.RunOptions](arsession/runoptions/removeexistinganchors.md)
  An option to remove any anchor objects associated with the session’s previous run.
- [static var stopTrackedRaycasts: ARSession.RunOptions](arsession/runoptions/stoptrackedraycasts.md)
  An option to stop all active tracked raycasts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runoptions/resetscenereconstruction)*