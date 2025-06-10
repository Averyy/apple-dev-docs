# animate(motion:)

**Framework**: DockKit  
**Kind**: method

Starts an animation sequence.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final func animate(motion: DockAccessory.Animation) async throws -> Progress
```

#### Return Value

A progress object that reports the progress during execution of the animation sequence.

#### Discussion

This method moves the dock accessory along a predefined trajectory to convey a characteristic. Do this only if you disable system tracking.

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if device isn’t connected, [`DockKitError.frameRateTooHigh`](dockkiterror/frameratetoohigh.md) if calling the method too frequently, or [`DockKitError.notSupported`](dockkiterror/notsupported.md) in macOS.

## Parameters

- `motion`: The animation sequence to perform.

## See Also

- [func setRegionOfInterest(CGRect) async throws](dockaccessory/setregionofinterest(_:).md)
  Sets the area in the video frame in which the dock accessory tracks a subject.
- [var regionOfInterest: CGRect](dockaccessory/regionofinterest.md)
  The area in the video frame in which the dock accessory tracks a subject.
- [DockAccessory.Animation](dockaccessory/animation.md)
  Character animations that describe how to move the dock accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/animate(motion:))*