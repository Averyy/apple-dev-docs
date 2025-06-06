# Algorithm Convergence Status

**Framework**: Nearby Interaction

The possible Objective-C states of Camera Assistance.

#### Overview

When the app enables Camera Assistance by setting [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md) = `true`, the framework may require user action before the feature is operational at runtime. This enumeration indicates whether Camera Assistance currently functions as expected on device, and the [`NIAlgorithmConvergenceStatusReason`](nialgorithmconvergencestatusreason.md) reasons define the recommended user actions to get Camera Assistance operational, if needed.

## Topics

### Status
- [enum NIAlgorithmConvergenceStatus](nialgorithmconvergencestatus-2fnve.md)
  The possible states of Camera Assistance.

## See Also

- [Finding devices with precision](finding-devices-with-precision.md)
  Leverage the spatial awareness of ARKit and Apple Ultra Wideband Chips in your app to guide users to a nearby device.
- [class NIAlgorithmConvergence](nialgorithmconvergence.md)
  An object that provides the state and reason for user coaching recommendations.
- [enum NIAlgorithmConvergenceStatus](nialgorithmconvergencestatus-2fnve.md)
  The possible states of Camera Assistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/algorithm-convergence-status)*