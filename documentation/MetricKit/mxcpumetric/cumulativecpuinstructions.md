# cumulativeCPUInstructions

**Framework**: MetricKit  
**Kind**: property

The total number of CPU instructions the app executed during the reporting period.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeCPUInstructions: Measurement<Unit> { get }
```

#### Discussion

For CPUs using out-of-order execution, this property represents the count of instructions the pipeline fully executes. These instructions are sometimes referred to as .

## See Also

- [var cumulativeCPUTime: Measurement<UnitDuration>](mxcpumetric/cumulativecputime.md)
  The total amount of CPU the app used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpumetric/cumulativecpuinstructions)*