# cumulativeCPUInstructions

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total number of CPU instructions the app executed during the reporting period.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CPUInstructionsCountMetric`](../cpuinstructionscountmetric.md) instead.

## Declaration

```swift
var cumulativeCPUInstructions: Measurement<Unit> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnit *> * cumulativeCPUInstructions;
```

## Discussion

For CPUs using out-of-order execution, this property represents the count of instructions the pipeline fully executes. These instructions are sometimes referred to as *retired instructions*.

## See Also

### Reading CPU use
- [var cumulativeCPUTime: Measurement<UnitDuration>](./cumulativecputime.md)
  The total amount of CPU the app used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpumetric/cumulativecpuinstructions)*