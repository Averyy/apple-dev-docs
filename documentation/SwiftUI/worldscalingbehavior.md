# WorldScalingBehavior

**Framework**: SwiftUI  
**Kind**: struct

Specifies the scaling behavior a window should have within the world.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct WorldScalingBehavior
```

#### Overview

By default, a regular [`WindowGroup`](windowgroup.md) uses a scaling behavior of [`dynamic`](worldscalingbehavior/dynamic.md), and a window with [`volumetric`](windowstyle/volumetric.md) has a fixed scale.

Dynamic scale means the window will scale larger as it moves further away, maintaining the same angular size. Fixed scale means the window will keep its physical size in the world.

For further information, see [`Spatial layout`](https://developer.apple.com/design/Human-Interface-Guidelines/spatial-layout) in the Human Interface Guidelines.

## Topics

### Type Properties
- [static var automatic: WorldScalingBehavior](worldscalingbehavior/automatic.md)
  The scaling behavior that is standard for the window’s style.
- [static var dynamic: WorldScalingBehavior](worldscalingbehavior/dynamic.md)
  The window will scale up as it moves further away, maintaining the same angular size.

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
- [func defaultWorldScaling(WorldScalingBehavior) -> some Scene](scene/defaultworldscaling(_:).md)
  Specify the world scaling behavior for the window.
- [struct WorldScalingCompensation](worldscalingcompensation.md)
  Indicates whether returned metrics will take dynamic scaling into account.
- [var worldTrackingLimitations: Set<WorldTrackingLimitation>](environmentvalues/worldtrackinglimitations.md)
  The current limitations of the device tracking the user’s surroundings.
- [struct WorldTrackingLimitation](worldtrackinglimitation.md)
  A structure to represent limitations of tracking the user’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/worldscalingbehavior)*