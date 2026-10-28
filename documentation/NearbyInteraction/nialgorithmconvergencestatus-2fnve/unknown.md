# NIAlgorithmConvergenceStatus.unknown

**Framework**: Nearby Interaction  
**Kind**: case  
**Role**: Case

An indication that the framework is unsure of the Camera Assistance status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
case unknown
```

## Discussion

Look to a subsequent call to [`session(_:didUpdateAlgorithmConvergence:for:)`](../nisessiondelegate/session%28_,didupdatealgorithmconvergence,for%29.md) and check for a more definitive algorithm-convergence status.

## See Also

### Interpreting the convergence state
- [NIAlgorithmConvergenceStatus.converged](./converged.md)
  A status that indicates the framework’s Camera Assistance feature is operational.
- [case notConverged([NIAlgorithmConvergenceStatus.Reason])](./notconverged%28_%29.md)
  A status that indicates the framework’s Camera Assistance feature requires action from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve/unknown)*