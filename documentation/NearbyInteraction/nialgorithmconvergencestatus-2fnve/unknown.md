# NIAlgorithmConvergenceStatus.unknown

**Framework**: Nearby Interaction  
**Kind**: case

An indication that the framework is unsure of the Camera Assistance status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
case unknown
```

#### Discussion

Look to a subsequent call to [`session(_:didUpdateAlgorithmConvergence:for:)`](nisessiondelegate/session(_:didupdatealgorithmconvergence:for:).md) and check for a more definitive algorithm-convergence status.

## See Also

- [NIAlgorithmConvergenceStatus.converged](nialgorithmconvergencestatus-2fnve/converged.md)
  A status that indicates the framework’s Camera Assistance feature is operational.
- [case notConverged([NIAlgorithmConvergenceStatus.Reason])](nialgorithmconvergencestatus-2fnve/notconverged(_:).md)
  A status that indicates the framework’s Camera Assistance feature requires action from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve/unknown)*