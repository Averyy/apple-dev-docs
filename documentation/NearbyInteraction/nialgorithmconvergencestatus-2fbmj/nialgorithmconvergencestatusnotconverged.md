# NIAlgorithmConvergenceStatusNotConverged

**Framework**: Nearby Interaction  
**Kind**: case

A status that indicates the framework’s Camera Assistance feature requires action from the user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 8.0+

## Declaration

```swift
NIAlgorithmConvergenceStatusNotConverged
```

#### Discussion

In this state, the framework needs more information about the user’s physical environment before setting [`horizontalAngle`](ninearbyobject/horizontalangle-9ibky.md) and/or [`verticalDirectionEstimate`](ninearbyobject/verticaldirectionestimate-swift.property.md).

Look to the reasons array of the `convergence` object provided by  [`session(_:didUpdateAlgorithmConvergence:for:)`](nisessiondelegate/session(_:didupdatealgorithmconvergence:for:).md) for more information on the cause. Each reason indicates a specific action the user can do to provide ARKit with the necessary camera data to support Nearby Interaction’s Camera Assistance.

## See Also

- [NIAlgorithmConvergenceStatusConverged](nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusconverged.md)
  A status that indicates the framework’s Camera Assistance feature is operational.
- [NIAlgorithmConvergenceStatusUnknown](nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusunknown.md)
  An indication that the framework is unsure of the Camera Assistance status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusnotconverged)*