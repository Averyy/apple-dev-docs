# setOrientation(_:duration:relative:)

**Framework**: DockKit  
**Kind**: method

Sets the position of each axis of orientation to radians for pitch, yaw, and roll.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
final func setOrientation(_ rotation: Vector3D, duration: Duration = .seconds(0), relative: Bool = false) async throws -> Progress
```

#### Return Value

An object that reports progress during the animation sequence.

#### Discussion

This method works only when you disable system tracking.

> **Note**: [`DockKitError.frameRateTooHigh`](dockkiterror/frameratetoohigh.md) if calling the method too frequently, or [`DockKitError.notSupported`](dockkiterror/notsupported.md) in macOS.

## Parameters

- `rotation`: The spatial framework’s Vector3D with X, Y, and Z corresponding to radians of pitch, yaw, and roll axes.
- `duration`: The duration, in seconds, to reach the target orientation.
- `relative`: Calculate the relative-to-current positions, if set to   ; otherwise, move to an absolute position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/setorientation(_:duration:relative:)-84z7i)*