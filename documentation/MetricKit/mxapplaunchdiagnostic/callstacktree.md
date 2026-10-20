# callStackTree

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The call stack tree associated with the app launch.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`callStackTree`](../applaunchdiagnostic/callstacktree.md) instead.

## Declaration

```swift
var callStackTree: MXCallStackTree { get }
```

```objc
@property (strong, readonly, nonnull) MXCallStackTree * callStackTree;
```

## See Also

### Reading app launch metrics
- [var launchDuration: Measurement<UnitDuration>](./launchduration.md)
  The total app launch duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchdiagnostic/callstacktree)*