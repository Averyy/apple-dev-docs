# Algorithm Convergence Status

**Framework**: Nearby Interaction  
**Role**: API Collection

The possible Objective-C states of Camera Assistance.

#### Overview

When the app enables Camera Assistance by setting [`isCameraAssistanceEnabled`](./ninearbypeerconfiguration/iscameraassistanceenabled.md) = `true`, the framework may require user action before the feature is operational at runtime. This enumeration indicates whether Camera Assistance currently functions as expected on device, and the [`NIAlgorithmConvergenceStatusReason`](./nialgorithmconvergencestatusreason.md) reasons define the recommended user actions to get Camera Assistance operational, if needed.

## Topics

### Status
- [enum NIAlgorithmConvergenceStatus](./nialgorithmconvergencestatus-2fnve.md)
  The possible states of Camera Assistance.
### Coaching recommendations
- [NIAlgorithmConvergenceStatusReasonInsufficientHorizontalSweep](./nialgorithmconvergencestatusreasoninsufficienthorizontalsweep.md)
  Indicates that the camera needs to view the user’s environment from different horizontal angles.
- [NIAlgorithmConvergenceStatusReasonInsufficientVerticalSweep](./nialgorithmconvergencestatusreasoninsufficientverticalsweep.md)
  Indicates that the camera needs to view the user’s environment from different vertical angles.
- [NIAlgorithmConvergenceStatusReasonInsufficientMovement](./nialgorithmconvergencestatusreasoninsufficientmovement.md)
  Indicates that the device needs to move from its current position in the physical environment.
- [NIAlgorithmConvergenceStatusReasonInsufficientLighting](./nialgorithmconvergencestatusreasoninsufficientlighting.md)
  Indicates that the camera needs to view the phsyical environment under better lighting conditions.
### Reasons
- [NIAlgorithmConvergenceStatusReason](./nialgorithmconvergencestatusreason.md)
  The possible reasons for the framework’s Camera Assistance status.
- [NIAlgorithmConvergenceStatusReasonDescription](./nialgorithmconvergencestatusreasondescription.md)
  A human-readable description for a particular convergence status reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/algorithm-convergence-status)*