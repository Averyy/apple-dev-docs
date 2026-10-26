# NIAlgorithmConvergenceStatusReason

**Framework**: Nearby Interaction  
**Kind**: typealias  
**Role**: Type Alias

The possible reasons for the framework’s Camera Assistance status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```c
typedef NSString * NIAlgorithmConvergenceStatusReason;
```

#### Discussion

The framework provides the app with one or more reasons for the current convergence status. Reasons detail specific user actions the framework believes will get the Camera Assistance feature operational.

At runtime, the app needs to check the status in the `convergence` object provided by [`session(_:didUpdateAlgorithmConvergence:for:)`](./nisessiondelegate/session%28_,didupdatealgorithmconvergence,for%29.md). If the status indicates that Camera Assistance requires user intervention, the app needs to coach the user, such as by presenting text that explains what to do, for every value in the [`reasons`](./nialgorithmconvergence/reasons.md) field.

## See Also

### Reasons
- [NIAlgorithmConvergenceStatusReasonDescription](./nialgorithmconvergencestatusreasondescription.md)
  A human-readable description for a particular convergence status reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatusreason)*