# supportedVolumeViewpoints(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies which viewpoints are supported for the window bar and ornaments in a volume.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func supportedVolumeViewpoints(_ viewpoints: SquareAzimuth.Set) -> some View
```

## Discussion

This defaults to all viewpoints and determines which viewpoints the window bar and ornaments will ‘follow’ the user to as they move around the volume.

## See Also

### Interacting with volumes
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](./onvolumeviewpointchange%28updatestrategy,initial,_%29.md)
  Adds an action to perform when the viewpoint of the volume changes.
- [struct VolumeViewpointUpdateStrategy](../volumeviewpointupdatestrategy.md)
  A type describing when the action provided to [`onVolumeViewpointChange(updateStrategy:initial:_:)`](./onvolumeviewpointchange%28updatestrategy,initial,_%29.md) should be called.
- [struct Viewpoint3D](../viewpoint3d.md)
  A type describing what direction something is being viewed from.
- [enum SquareAzimuth](../squareazimuth.md)
  A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [struct WorldAlignmentBehavior](../worldalignmentbehavior.md)
  A type representing the world alignment behavior for a scene.
- [func volumeWorldAlignment(WorldAlignmentBehavior) -> some Scene](../scene/volumeworldalignment%28_%29.md)
  Specifies how a volume should be aligned when moved in the world.
- [struct WorldScalingBehavior](../worldscalingbehavior.md)
  Specifies the scaling behavior a window should have within the world.
- [func defaultWorldScaling(WorldScalingBehavior) -> some Scene](../scene/defaultworldscaling%28_%29.md)
  Specify the world scaling behavior for the window.
- [struct WorldScalingCompensation](../worldscalingcompensation.md)
  Indicates whether returned metrics will take dynamic scaling into account.
- [var worldTrackingLimitations: Set<WorldTrackingLimitation>](../environmentvalues/worldtrackinglimitations.md)
  The current limitations of the device tracking the user’s surroundings.
- [struct WorldTrackingLimitation](../worldtrackinglimitation.md)
  A structure to represent limitations of tracking the user’s surroundings.
- [struct SurfaceSnappingInfo](../surfacesnappinginfo.md)
  A type representing information about the window scenes snap state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/supportedvolumeviewpoints(_:))*