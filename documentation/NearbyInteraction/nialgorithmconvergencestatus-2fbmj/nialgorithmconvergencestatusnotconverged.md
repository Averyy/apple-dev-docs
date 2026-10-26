# NIAlgorithmConvergenceStatusNotConverged

**Framework**: Nearby Interaction  
**Kind**: case  
**Role**: Enumeration Case

A status that indicates the framework’s Camera Assistance feature requires action from the user.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- watchOS

## Declaration

```c
NIAlgorithmConvergenceStatusNotConverged
```

#### Discussion

In this state, the framework needs more information about the user’s physical environment before setting [`horizontalAngle`](../ninearbyobject/horizontalangle-9ibky.md) and/or [`verticalDirectionEstimate`](../ninearbyobject/verticaldirectionestimate-swift.property.md).

Look to the reasons array of the `convergence` object provided by  [`session(_:didUpdateAlgorithmConvergence:for:)`](../nisessiondelegate/session%28_,didupdatealgorithmconvergence,for%29.md) for more information on the cause. Each reason indicates a specific action the user can do to provide ARKit with the necessary camera data to support Nearby Interaction’s Camera Assistance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusnotconverged)*