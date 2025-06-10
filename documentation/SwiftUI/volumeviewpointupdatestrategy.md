# VolumeViewpointUpdateStrategy

**Framework**: SwiftUI  
**Kind**: struct

A type describing when the action provided to [`onVolumeViewpointChange(updateStrategy:initial:_:)`](view/onvolumeviewpointchange(updatestrategy:initial:_:).md) should be called.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct VolumeViewpointUpdateStrategy
```

## Topics

### Type Properties
- [static let all: VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy/all.md)
  The action should be run for all viewpoint changes.
- [static let supported: VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy/supported.md)
  The action should only be run when the new viewpoint is equivalent to one of the values provided through [`supportedVolumeViewpoints(_:)`](view/supportedvolumeviewpoints(_:).md).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](view/onvolumeviewpointchange(updatestrategy:initial:_:).md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](view/supportedvolumeviewpoints(_:).md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [struct Viewpoint3D](viewpoint3d.md)
  A type describing what direction something is being viewed from.
- [enum SquareAzimuth](squareazimuth.md)
  A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [struct WorldAlignmentBehavior](worldalignmentbehavior.md)
  A type representing the world alignment behavior for a scene.
- [func volumeWorldAlignment(WorldAlignmentBehavior) -> some Scene](scene/volumeworldalignment(_:).md)
  Specifies how a volume should be aligned when moved in the world.
- [struct WorldScalingBehavior](worldscalingbehavior.md)
  Specifies the scaling behavior a window should have within the world.
- [func defaultWorldScaling(WorldScalingBehavior) -> some Scene](scene/defaultworldscaling(_:).md)
  Specify the world scaling behavior for the window.
- [struct WorldScalingCompensation](worldscalingcompensation.md)
  Indicates whether returned metrics will take dynamic scaling into account.
- [var worldTrackingLimitations: Set<WorldTrackingLimitation>](environmentvalues/worldtrackinglimitations.md)
  The current limitations of the device tracking the user’s surroundings.
- [struct WorldTrackingLimitation](worldtrackinglimitation.md)
  A structure to represent limitations of tracking the user’s surroundings.
- [struct SurfaceSnappingInfo](surfacesnappinginfo.md)
  A type representing information about the window scenes snap state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/volumeviewpointupdatestrategy)*