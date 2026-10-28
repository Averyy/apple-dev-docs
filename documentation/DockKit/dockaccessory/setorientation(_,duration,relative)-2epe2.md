# setOrientation(_:duration:relative:)

**Framework**: DockKit  
**Kind**: method  
**Role**: Instance Method

Sets the position of each axis of orientation to radians for pitch, yaw, and roll.

**Availability**:
- iOS 17.0+ - Deprecated in 18.0
- iPadOS 17.0+ - Deprecated in 18.0
- Mac Catalyst 17.0+ - Deprecated in 18.0
- macOS 14.0+ - Deprecated in 15.0

> **Deprecated**: please use async version of setOrientation

## Declaration

```swift
final func setOrientation(_ rotation: Vector3D, duration: Duration = .seconds(0), relative: Bool = false) throws -> Progress
```

## Mentions

- [Modify rotation and positioning programmatically](../modify-rotation-and-positioning-behavior-programmatically.md)

## Return Value

An object that reports progress during the animation sequence.

## Discussion

This method works only when you disable system tracking.

> **Throws**: [`DockKitError.frameRateTooHigh`](../dockkiterror/frameratetoohigh.md) if calling the method too frequently, or [`DockKitError.notSupported`](../dockkiterror/notsupported.md) in macOS.

## Parameters

- `rotation`: The spatial framework’s Vector3D with X, Y, and Z corresponding to radians of pitch, yaw, and roll axes.
- `duration`: The duration, in seconds, to reach the target orientation.
- `relative`: Calculate the relative-to-current positions, if set to  `true`; otherwise, move to an absolute position.

## See Also

### Setting position and limits
- [func setLimits(DockAccessory.Limits) throws](./setlimits%28_%29.md)
  Sets limits for the axes of rotation.
- [func setOrientation(Rotation3D, duration: Duration, relative: Bool) throws -> Progress](./setorientation%28_,duration,relative%29-6b0fl.md)
  Sets the position of each axis of orientation to radians for pitch, yaw, and roll.
- [func setAngularVelocity(Vector3D) async throws](./setangularvelocity%28_%29.md)
  Sets the angular velocity of each axis of orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/setorientation(_:duration:relative:)-2epe2)*