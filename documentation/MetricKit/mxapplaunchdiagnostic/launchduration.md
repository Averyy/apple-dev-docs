# launchDuration

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total app launch duration.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`launchDuration`](../applaunchdiagnostic/launchduration.md) instead.

## Declaration

```swift
var launchDuration: Measurement<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitDuration *> * launchDuration;
```

## See Also

### Reading app launch metrics
- [var callStackTree: MXCallStackTree](./callstacktree.md)
  The call stack tree associated with the app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchdiagnostic/launchduration)*