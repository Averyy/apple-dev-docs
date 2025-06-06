# WorldScalingCompensation

**Framework**: SwiftUI  
**Kind**: struct

Indicates whether returned metrics will take dynamic scaling into account.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct WorldScalingCompensation
```

#### Overview

On visionOS, a window scene or a volume scene with the [`defaultWorldScaling(_:)`](scene/defaultworldscaling(_:).md) modifier may scale dynamically when the user repositions it. In those cases, the metrics returned by a [`PhysicalMetric`](physicalmetric.md) or [`PhysicalMetricsConverter`](physicalmetricsconverter.md) value may or may not correspond to the units of a `RealityView`.

World scale compensation lets you specify if this scaling is taken into account. If the values are [`unscaled`](worldscalingcompensation/unscaled.md), they will correspond to the physical metrics of the user’s surroundings, regardless of dynamic scale. If [`scaled`](worldscalingcompensation/scaled.md), they will be scaled appropriately for the scene, which means they will match the default coordinate system of a `RealityView` in that scene.

## Topics

### Type Properties
- [static let scaled: WorldScalingCompensation](worldscalingcompensation/scaled.md)
  Returns metrics that are scaled appropriately to match the coordinate system of their scene, including any world scaling behavior.
- [static let unscaled: WorldScalingCompensation](worldscalingcompensation/unscaled.md)
  Returns metrics that match the scale of the user’s surroundings, regardless of the world scaling behavior of their scene.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct WorldAlignmentBehavior](worldalignmentbehavior.md)
  A type representing the world alignment behavior for a scene.
- [func volumeWorldAlignment(WorldAlignmentBehavior) -> some Scene](scene/volumeworldalignment(_:).md)
  Specifies how a volume should be aligned when moved in the world.
- [struct WorldScalingBehavior](worldscalingbehavior.md)
  Specifies the scaling behavior a window should have within the world.
- [func defaultWorldScaling(WorldScalingBehavior) -> some Scene](scene/defaultworldscaling(_:).md)
  Specify the world scaling behavior for the window.
- [var worldTrackingLimitations: Set<WorldTrackingLimitation>](environmentvalues/worldtrackinglimitations.md)
  The current limitations of the device tracking the user’s surroundings.
- [struct WorldTrackingLimitation](worldtrackinglimitation.md)
  A structure to represent limitations of tracking the user’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/worldscalingcompensation)*