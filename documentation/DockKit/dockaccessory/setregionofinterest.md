# setRegionOfInterest(_:)

**Framework**: Dockkit  
**Kind**: method

Sets the area in the video frame in which the dock accessory tracks a subject.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final func setRegionOfInterest(_ region: CGRect) async throws
```

#### Discussion

The region of interest is an limited area within the video frame that DockKit tracks a subject in. The default value is `(0,0,1,1)`, which indicates that the whole frame is of interest.

If you disable system tracking, this configuration change applies to any custom tracking for this dock accessory. The configuration applies to any camera stream the app has open if system tracking is enabled.

The region of interest doesn’t persist; it resets to the entire video frame any time an app exits, backgrounds, or stops tracking.

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if device isn’t connected, or [`DockKitError.notSupported`](dockkiterror/notsupported.md) if called on macOS.

## Parameters

- `region`: The area in the video frame in which the dock accessory tracks a subject.

## See Also

- [func animate(motion: DockAccessory.Animation) async throws -> Progress](dockaccessory/animate(motion:).md)
  Starts an animation sequence.
- [var regionOfInterest: CGRect](dockaccessory/regionofinterest.md)
  The area in the video frame in which the dock accessory tracks a subject.
- [DockAccessory.Animation](dockaccessory/animation.md)
  Character animations that describe how to move the dock accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/setregionofinterest(_:))*