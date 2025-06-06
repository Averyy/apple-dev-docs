# ARRaycastQuery.Target.estimatedPlane

**Framework**: ARKit  
**Kind**: case

A raycast target that specifies nonplanar surfaces, or planes about which ARKit can only estimate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case estimatedPlane
```

#### Discussion

A raycast with this target intersects feature points around the ray that ARKit estimates may be a real-world surface.

When combined with [`ARRaycastQuery.TargetAlignment.any`](arraycastquery/targetalignment-swift.enum/any.md), ARKit bases estimated plane alignment on the normal of the surface.

When you set your world-tracking configuration’s [`sceneReconstruction`](arworldtrackingconfiguration/scenereconstruction.md) to one of the `mesh` options, ARKit allows a raycast with this target (and target-alignment [`ARRaycastQuery.TargetAlignment.any`](arraycastquery/targetalignment-swift.enum/any.md)) to intersect the scene mesh. Then the raycast result can include points even on nonplanar surfaces or surfaces that have few or no features, such as a white wall. If you set [`sceneReconstruction`](arworldtrackingconfiguration/scenereconstruction.md) to [`ARSceneReconstructionNone`](arscenereconstruction/arscenereconstructionnone.md), raycasts ignore the scene mesh.

## See Also

- [ARRaycastQuery.Target.existingPlaneGeometry](arraycastquery/target-swift.enum/existingplanegeometry.md)
  A raycast target that requires a plane to have a definitive size and shape.
- [ARRaycastQuery.Target.existingPlaneInfinite](arraycastquery/target-swift.enum/existingplaneinfinite.md)
  A raycast target that specifies a detected plane, regardless of its size and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arraycastquery/target-swift.enum/estimatedplane)*