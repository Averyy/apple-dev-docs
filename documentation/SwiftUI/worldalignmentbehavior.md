# WorldAlignmentBehavior

**Framework**: SwiftUI  
**Kind**: struct

A type representing the world alignment behavior for a scene.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct WorldAlignmentBehavior
```

#### Overview

A value of this type can be provided to the [`volumeWorldAlignment(_:)`](scene/volumeworldalignment(_:).md) scene modifier to control the world alignment volumes should maintain as they are repositioned. The default value is [`automatic`](worldalignmentbehavior/automatic.md).

## Topics

### Type Properties
- [static var adaptive: WorldAlignmentBehavior](worldalignmentbehavior/adaptive.md)
  When lifted above eye level, the volume will tilt so the front remains fully visible.
- [static var automatic: WorldAlignmentBehavior](worldalignmentbehavior/automatic.md)
  The world alignment behavior that is standard for the system.
- [static var gravityAligned: WorldAlignmentBehavior](worldalignmentbehavior/gravityaligned.md)
  The volume will not tilt so as to remain aligned with gravity.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](view/onvolumeviewpointchange(updatestrategy:initial:_:).md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](view/supportedvolumeviewpoints(_:).md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [struct VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy.md)
  A type describing when the action provided to [`onVolumeViewpointChange(updateStrategy:initial:_:)`](view/onvolumeviewpointchange(updatestrategy:initial:_:).md) should be called.
- [struct Viewpoint3D](viewpoint3d.md)
  A type describing what direction something is being viewed from.
- [enum SquareAzimuth](squareazimuth.md)
  A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/worldalignmentbehavior)*