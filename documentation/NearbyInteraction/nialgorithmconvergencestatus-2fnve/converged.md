# NIAlgorithmConvergenceStatus.converged

**Framework**: Nearby Interaction  
**Kind**: case  
**Role**: Case

A status that indicates the framework’s Camera Assistance feature is operational.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
case converged
```

## Discussion

In this state, the app doesn’t need to coach the user and receives all the benefits of Camera Assistance described in [`isCameraAssistanceEnabled`](../ninearbypeerconfiguration/iscameraassistanceenabled.md).

## See Also

### Interpreting the convergence state
- [case notConverged([NIAlgorithmConvergenceStatus.Reason])](./notconverged%28_%29.md)
  A status that indicates the framework’s Camera Assistance feature requires action from the user.
- [NIAlgorithmConvergenceStatus.unknown](./unknown.md)
  An indication that the framework is unsure of the Camera Assistance status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve/converged)*