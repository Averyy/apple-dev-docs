# worldTrackingLimitations

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The current limitations of the device tracking the user’s surroundings.

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var worldTrackingLimitations: Set<WorldTrackingLimitation> { get set }
```

## Discussion

Read this environment value from within a view to obtain the current limitations of the device tracking the user’s surroundings. The device’s capabilities may be limited due to physical circumstances such as the lighting. If any of the limitations occur due to changing circumstances, the set is updated accordingly. For example, the following [`Text`](../text.md) view automatically updates when the world tracking limitations change:

```swift
@Environment(\.worldTrackingLimitations)
private var worldTrackingLimitations

var body: some View {
    Text("Can track translation?" + worldTrackingLimitations
        .contains(.translation) ? "No" : "Yes")
}
```

When the device’s world tracking capabilities are limited, don’t prevent the user from experiencing your app entirely. Instead, try to adapt the user experience to the current circumstances in order to provide a meaningful experience at all times.

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
- [func volumeWorldAlignment(WorldAlignmentBehavior) -> some Scene](../scene/volumeworldalignment%28_%29.md)
  Specifies how a volume should be aligned when moved in the world.
- [struct WorldScalingBehavior](../worldscalingbehavior.md)
  Specifies the scaling behavior a window should have within the world.
- [func defaultWorldScaling(WorldScalingBehavior) -> some Scene](../scene/defaultworldscaling%28_%29.md)
  Specify the world scaling behavior for the window.
- [struct WorldScalingCompensation](../worldscalingcompensation.md)
  Indicates whether returned metrics will take dynamic scaling into account.
- [struct WorldTrackingLimitation](../worldtrackinglimitation.md)
  A structure to represent limitations of tracking the user’s surroundings.
- [struct SurfaceSnappingInfo](../surfacesnappinginfo.md)
  A type representing information about the window scenes snap state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/worldtrackinglimitations)*