# stopTrackedRaycasts

**Framework**: ARKit  
**Kind**: property

An option to stop all active tracked raycasts.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var stopTrackedRaycasts: ARSession.RunOptions { get }
```

#### Discussion

By default, when you call the [`run(_:options:)`](arsession/run(_:options:).md) method on a session that is running or has run before, the session keeps tracking any [`ARTrackedRaycast`](artrackedraycast.md) objects that you previously added by calling [`trackedRaycast(_:updateHandler:)`](arsession/trackedraycast(_:updatehandler:).md).

Use [`stopTrackedRaycasts`](arsession/runoptions/stoptrackedraycasts.md) if you want to stop all active tracked raycasts. Alternatively, you can stop individual raycasts by calling [`stopTracking()`](artrackedraycast/stoptracking().md) on individual raycasts.

## See Also

- [static var resetTracking: ARSession.RunOptions](arsession/runoptions/resettracking.md)
  An option to reset the device’s position from the session’s previous run.
- [static var removeExistingAnchors: ARSession.RunOptions](arsession/runoptions/removeexistinganchors.md)
  An option to remove any anchor objects associated with the session’s previous run.
- [static var resetSceneReconstruction: ARSession.RunOptions](arsession/runoptions/resetscenereconstruction.md)
  An option to reset the scene mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runoptions/stoptrackedraycasts)*