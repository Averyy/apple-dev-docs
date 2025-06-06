# SquareAzimuth

**Framework**: SwiftUI  
**Kind**: enum

A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@frozen
enum SquareAzimuth
```

## Topics

### Structures
- [SquareAzimuth.Set](squareazimuth/set.md)
### Enumeration Cases
- [SquareAzimuth.back](squareazimuth/back.md)
  Has an orientation with an horizontal angle equal to `180°`
- [SquareAzimuth.front](squareazimuth/front.md)
  Has an orientation with an horizontal angle equal to `0°`.
- [SquareAzimuth.left](squareazimuth/left.md)
  Has an orientation with an horizontal angle equal to `270°`.
- [SquareAzimuth.right](squareazimuth/right.md)
  Has an orientation with an horizontal angle equal to `90°`.
### Initializers
- [init(closestToAzimuth: Angle)](squareazimuth/init(closesttoazimuth:).md)
  Creates a SquareAzimuth case with an orientation that has a horizontal angle closest to the provided azimuth.
### Instance Properties
- [var orientation: Rotation3D](squareazimuth/orientation.md)
  A 3D rotation that is snapped to the center of one of the four sides.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/squareazimuth)*