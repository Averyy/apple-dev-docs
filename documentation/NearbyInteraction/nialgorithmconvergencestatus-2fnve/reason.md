# NIAlgorithmConvergenceStatus.Reason

**Framework**: Nearby Interaction  
**Kind**: struct  
**Role**: Structure

The possible reasons for the Camera Assistance status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
struct Reason
```

## Overview

When the app enables Camera Assistance by setting [`isCameraAssistanceEnabled`](../ninearbypeerconfiguration/iscameraassistanceenabled.md) to `true`, the framework provides the app with one or more reasons when the convergence status is [`NIAlgorithmConvergenceStatus.notConverged(_:)`](./notconverged%28_%29.md). The reasons detail specific user actions the framework requires to improve the results of Camera Assistance.

At runtime, the app needs to check the status in the `convergence` object provided by [`session(_:didUpdateAlgorithmConvergence:for:)`](../nisessiondelegate/session%28_,didupdatealgorithmconvergence,for%29.md). If the status indicates that Camera Assistance requires user intervention, the app needs to coach the user, such as by presenting text that explains what to do for each circumstance that [`reasons`](../nialgorithmconvergence/reasons.md) can describe.

> **Note**: The Objective-C version of this class is [`NIAlgorithmConvergenceStatusReason`](../nialgorithmconvergencestatusreason.md).

## Topics

### Comparing convergence status reasons
- [var localizedDescription: String?](./reason/localizeddescription.md)
  A string that contains a description of the error.
### Interpreting the convergence status reason
- [static let insufficientMovement: NIAlgorithmConvergenceStatus.Reason](./reason/insufficientmovement.md)
  Indicates that the device needs to move from its current position in the physical environment.
- [static let insufficientHorizontalSweep: NIAlgorithmConvergenceStatus.Reason](./reason/insufficienthorizontalsweep.md)
  Indicates that the device needs more horizontal motion.
- [static let insufficientVerticalSweep: NIAlgorithmConvergenceStatus.Reason](./reason/insufficientverticalsweep.md)
  Indicates that the device needs more vertical motion.
- [static let insufficientLighting: NIAlgorithmConvergenceStatus.Reason](./reason/insufficientlighting.md)
  Indicates that the camera needs to view the physical environment under better lighting conditions.
- [static let insufficientSignalStrength: NIAlgorithmConvergenceStatus.Reason](./reason/insufficientsignalstrength.md)
  Indicates that the users might be too far apart.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Coaching the user
- [func session(NISession, didUpdateAlgorithmConvergence: NIAlgorithmConvergence, for: NINearbyObject?)](../nisessiondelegate/session%28_,didupdatealgorithmconvergence,for%29.md)
  Provides recommended actions the user can take to facilitate the framework’s Camera Assistance.
- [enum NIAlgorithmConvergenceStatus](../nialgorithmconvergencestatus-2fnve.md)
  The possible states of Camera Assistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve/reason)*