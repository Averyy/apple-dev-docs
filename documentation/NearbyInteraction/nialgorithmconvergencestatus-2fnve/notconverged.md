# NIAlgorithmConvergenceStatus.notConverged(_:)

**Framework**: Nearby Interaction  
**Kind**: case

A status that indicates the framework’s Camera Assistance feature requires action from the user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
case notConverged([NIAlgorithmConvergenceStatus.Reason])
```

#### Discussion

In this state, the framework needs more information about the user’s physical environment before setting [`horizontalAngle`](ninearbyobject/horizontalangle-hsg.md) and/or [`verticalDirectionEstimate`](ninearbyobject/verticaldirectionestimate-swift.property.md).

Look to the reasons array of the `convergence` object provided by [`session(_:didUpdateAlgorithmConvergence:for:)`](nisessiondelegate/session(_:didupdatealgorithmconvergence:for:).md) for more information on the cause. Each reason indicates a specific action the user can do to provide ARKit with the necessary camera data to support Nearby Interaction’s Camera Assistance.

## Parameters

- `reason`: A user action that the framework recommends to get the Camera Assistance feature operational.

## See Also

- [NIAlgorithmConvergenceStatus.converged](nialgorithmconvergencestatus-2fnve/converged.md)
  A status that indicates the framework’s Camera Assistance feature is operational.
- [NIAlgorithmConvergenceStatus.unknown](nialgorithmconvergencestatus-2fnve/unknown.md)
  An indication that the framework is unsure of the Camera Assistance status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve/notconverged(_:))*