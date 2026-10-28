# volumeWorldAlignment(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies how a volume should be aligned when moved in the world.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func volumeWorldAlignment(_ behavior: WorldAlignmentBehavior) -> some Scene
```

## Discussion

For example, you can create a volume that remains parallel to the floor even when lifted up high above eye level by applying a [`gravityAligned`](../worldalignmentbehavior/gravityaligned.md) alignment to the scene:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .windowStyle(.volumetric)
        .volumeWorldAlignment(.gravityAligned)
    }
}
```

The default value if you don’t apply the modifier is [`automatic`](../worldalignmentbehavior/automatic.md). With that strategy, volumes will tilt themselves so the front remains fully visible while being repositioned.

## See Also

### Interacting with volumes
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](../view/onvolumeviewpointchange%28updatestrategy,initial,_%29.md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](../view/supportedvolumeviewpoints%28_%29.md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [struct VolumeViewpointUpdateStrategy](../volumeviewpointupdatestrategy.md)
  A type describing when the action provided to [`onVolumeViewpointChange(updateStrategy:initial:_:)`](../view/onvolumeviewpointchange%28updatestrategy,initial,_%29.md) should be called.
- [struct Viewpoint3D](../viewpoint3d.md)
  A type describing what direction something is being viewed from.
- [enum SquareAzimuth](../squareazimuth.md)
  A type describing what direction something is being viewed from along the horizontal plane and snapped to 4 directions.
- [struct WorldAlignmentBehavior](../worldalignmentbehavior.md)
  A type representing the world alignment behavior for a scene.
- [struct WorldScalingBehavior](../worldscalingbehavior.md)
  Specifies the scaling behavior a window should have within the world.
- [func defaultWorldScaling(WorldScalingBehavior) -> some Scene](./defaultworldscaling%28_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/volumeworldalignment(_:))*