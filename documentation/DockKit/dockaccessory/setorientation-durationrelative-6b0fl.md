# setOrientation(_:duration:relative:)

**Framework**: Dockkit  
**Kind**: method

Sets the position of each axis of orientation to radians for pitch, yaw, and roll.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final func setOrientation(_ rotation: Rotation3D, duration: Duration = .seconds(0), relative: Bool = false) throws -> Progress
```

## Mentions

- [Modify rotation and positioning programmatically](modify-rotation-and-positioning-behavior-programmatically.md)

#### Return Value

A progress object that reports the progress towards the target orientation.

#### Discussion

This method works only when you disable system tracking.

> **Note**: [`DockKitError.frameRateTooHigh`](dockkiterror/frameratetoohigh.md) if calling the method too frequently, or [`DockKitError.notSupported`](dockkiterror/notsupported.md) in macOS.

## Parameters

- `rotation`: The spatial framework’s Rotation3D with X, Y, and Z corresponding to radians of pitch, yaw, and roll axes.
- `duration`: The duration, in seconds, to reach the target orientation.
- `relative`: Calculate the relative-to-current positions, if set to   ; otherwise, move to an absolute position.

## See Also

- [func setLimits(DockAccessory.Limits) throws](dockaccessory/setlimits(_:).md)
  Sets limits for the axes of rotation.
- [func setOrientation(Vector3D, duration: Duration, relative: Bool) throws -> Progress](dockaccessory/setorientation(_:duration:relative:)-2epe2.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func setAngularVelocity(Vector3D) async throws](dockaccessory/setangularvelocity(_:).md)
  Sets the angular velocity of each axis of orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/setorientation(_:duration:relative:)-6b0fl)*