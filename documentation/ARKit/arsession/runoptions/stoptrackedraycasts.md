# stopTrackedRaycasts

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

An option to stop all active tracked raycasts.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
static var stopTrackedRaycasts: ARSession.RunOptions { get }
```

```c
ARSessionRunOptionStopTrackedRaycasts
```

## Discussion

By default, when you call the [`run(_:options:)`](../run%28_,options%29.md) method on a session that is running or has run before, the session keeps tracking any [`ARTrackedRaycast`](../../artrackedraycast.md) objects that you previously added by calling [`trackedRaycast(_:updateHandler:)`](../trackedraycast%28_,updatehandler%29.md).

Use [`stopTrackedRaycasts`](./stoptrackedraycasts.md) if you want to stop all active tracked raycasts. Alternatively, you can stop individual raycasts by calling [`stopTracking()`](../../artrackedraycast/stoptracking%28%29.md) on individual raycasts.

## See Also

### Run Options
- [static var resetTracking: ARSession.RunOptions](./resettracking.md)
  An option to reset the device’s position from the session’s previous run.
- [static var removeExistingAnchors: ARSession.RunOptions](./removeexistinganchors.md)
  An option to remove any anchor objects associated with the session’s previous run.
- [static var resetSceneReconstruction: ARSession.RunOptions](./resetscenereconstruction.md)
  An option to reset the scene mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/runoptions/stoptrackedraycasts)*