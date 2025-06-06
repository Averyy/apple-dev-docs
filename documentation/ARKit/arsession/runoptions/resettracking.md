# resetTracking

**Framework**: ARKit  
**Kind**: property

An option to reset the device’s position from the session’s previous run.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var resetTracking: ARSession.RunOptions { get }
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Discussion

By default, when you call the [`run(_:options:)`](arsession/run(_:options:).md) method on a session that has run before or is already running, the session resumes device position tracking from its last known state. (For example, an [`ARAnchor`](aranchor.md) object keeps its apparent position relative to the camera.) When you call the [`run(_:options:)`](arsession/run(_:options:).md) method with a configuration of the same type as the session’s current configuration, you can add this option to force device position tracking to return to its initial state.

When you call the [`run(_:options:)`](arsession/run(_:options:).md) method with a configuration of a different type than the session’s current configuration, the session always resets tracking (that is, this option is implicitly enabled).

In either case, when you reset tracking, ARKit also removes any existing anchors from the session.

## See Also

- [static var removeExistingAnchors: ARSession.RunOptions](arsession/runoptions/removeexistinganchors.md)
  An option to remove any anchor objects associated with the session’s previous run.
- [static var stopTrackedRaycasts: ARSession.RunOptions](arsession/runoptions/stoptrackedraycasts.md)
  An option to stop all active tracked raycasts.
- [static var resetSceneReconstruction: ARSession.RunOptions](arsession/runoptions/resetscenereconstruction.md)
  An option to reset the scene mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runoptions/resettracking)*