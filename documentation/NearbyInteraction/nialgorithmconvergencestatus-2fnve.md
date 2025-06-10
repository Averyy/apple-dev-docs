# NIAlgorithmConvergenceStatus

**Framework**: Nearby Interaction  
**Kind**: enum

The possible states of Camera Assistance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
enum NIAlgorithmConvergenceStatus
```

#### Overview

When the app enables Camera Assistance by setting [`isCameraAssistanceEnabled`](ninearbypeerconfiguration/iscameraassistanceenabled.md) to `true`, the framework provides the app one of these values in the [`status`](nialgorithmconvergence/status-j61c.md) field of the convergence object provided by the [`session(_:didUpdateAlgorithmConvergence:for:)`](nisessiondelegate/session(_:didupdatealgorithmconvergence:for:).md) callback.

The framework may require user action before Camera Assistance is fully operational at runtime. This enumeration indicates whether Camera Assistance currently functions as expected on device (convergence state [`NIAlgorithmConvergenceStatus.converged`](nialgorithmconvergencestatus-2fnve/converged.md)), and otherwise, the [`NIAlgorithmConvergenceStatus.Reason`](nialgorithmconvergencestatus-2fnve/reason.md) defines the recommended user actions when status is [`NIAlgorithmConvergenceStatus.notConverged(_:)`](nialgorithmconvergencestatus-2fnve/notconverged(_:).md).

> **Note**: The Objective-C version of this enumeration is [`Algorithm Convergence Status`](algorithm-convergence-status.md).

## Topics

### Interpreting the convergence state
- [NIAlgorithmConvergenceStatus.converged](nialgorithmconvergencestatus-2fnve/converged.md)
  A status that indicates the framework’s Camera Assistance feature is operational.
- [case notConverged([NIAlgorithmConvergenceStatus.Reason])](nialgorithmconvergencestatus-2fnve/notconverged(_:).md)
  A status that indicates the framework’s Camera Assistance feature requires action from the user.
- [NIAlgorithmConvergenceStatus.unknown](nialgorithmconvergencestatus-2fnve/unknown.md)
  An indication that the framework is unsure of the Camera Assistance status.
### Comparing convergence states
- [static func == (NIAlgorithmConvergenceStatus, NIAlgorithmConvergenceStatus) -> Bool](nialgorithmconvergencestatus-2fnve/==(_:_:).md)
  Determines whether two convergence statuses are equal.
### Inspecting the convergence state reason
- [NIAlgorithmConvergenceStatus.Reason](nialgorithmconvergencestatus-2fnve/reason.md)
  The possible reasons for the Camera Assistance status.
- [NIAlgorithmConvergenceStatusConverged](nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusconverged.md)
  A status that indicates the framework’s Camera Assistance feature is operational.
- [NIAlgorithmConvergenceStatusNotConverged](nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusnotconverged.md)
  A status that indicates the framework’s Camera Assistance feature requires action from the user.
- [NIAlgorithmConvergenceStatusUnknown](nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusunknown.md)
  An indication that the framework is unsure of the Camera Assistance status.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [Finding devices with precision](finding-devices-with-precision.md)
  Leverage the spatial awareness of ARKit and Apple Ultra Wideband Chips in your app to guide users to a nearby device.
- [class NIAlgorithmConvergence](nialgorithmconvergence.md)
  An object that provides the state and reason for user coaching recommendations.
- [Algorithm Convergence Status](algorithm-convergence-status.md)
  The possible Objective-C states of Camera Assistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve)*