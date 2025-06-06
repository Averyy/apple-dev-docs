# NIAlgorithmConvergenceStatusUnknown

**Framework**: Nearby Interaction  
**Kind**: case

An indication that the framework is unsure of the Camera Assistance status.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 8.0+

## Declaration

```swift
NIAlgorithmConvergenceStatusUnknown
```

#### Discussion

Look to a subsequent call to [`session(_:didUpdateAlgorithmConvergence:for:)`](nisessiondelegate/session(_:didupdatealgorithmconvergence:for:).md) and check for a more definitive algorithm-convergence status.

## See Also

- [NIAlgorithmConvergenceStatusConverged](nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusconverged.md)
  A status that indicates the framework’s Camera Assistance feature is operational.
- [NIAlgorithmConvergenceStatusNotConverged](nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusnotconverged.md)
  A status that indicates the framework’s Camera Assistance feature requires action from the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fbmj/nialgorithmconvergencestatusunknown)*