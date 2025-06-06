# removeExistingAnchors

**Framework**: ARKit  
**Kind**: property

An option to remove any anchor objects associated with the session’s previous run.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var removeExistingAnchors: ARSession.RunOptions { get }
```

#### Discussion

By default, when you call the [`run(_:options:)`](arsession/run(_:options:).md) method on a session that has run before or is already running, the session keeps any [`ARAnchor`](aranchor.md) objects that you previously added. That is, objects in the AR scene keep their apparent real-world positions relative to the device (unless you enable the [`resetTracking`](arsession/runoptions/resettracking.md) option).

Enable the [`removeExistingAnchors`](arsession/runoptions/removeexistinganchors.md) option if changing session configurations should invalidate the apparent real-world positions of objects in the AR scene. For example, if you’ve added virtual content to the AR scene whose positions are correlated to real-world objects, remove those anchors so you can reevaluate appropriate real-world positions. On the other hand, if the virtual content in your scene needs to track real-world positions only when that content first appears and can move freely thereafter, you can disable this option to keep the anchors.

## See Also

- [static var resetTracking: ARSession.RunOptions](arsession/runoptions/resettracking.md)
  An option to reset the device’s position from the session’s previous run.
- [static var stopTrackedRaycasts: ARSession.RunOptions](arsession/runoptions/stoptrackedraycasts.md)
  An option to stop all active tracked raycasts.
- [static var resetSceneReconstruction: ARSession.RunOptions](arsession/runoptions/resetscenereconstruction.md)
  An option to reset the scene mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runoptions/removeexistinganchors)*