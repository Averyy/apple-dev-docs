# CLSProgressReportingCapability.Kind.duration

**Framework**: ClassKit  
**Kind**: case

Time spent performing the task.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case duration
```

#### Discussion

The framework automatically measures the time that a student spends working on a task, so all contexts have a [`CLSProgressReportingCapability.Kind.duration`](clsprogressreportingcapability/kind-swift.enum/duration.md) capability by default. You can replace the default one with a new one if you want to customize the [`details`](clsprogressreportingcapability/details.md) string.

## See Also

- [CLSProgressReportingCapability.Kind.percent](clsprogressreportingcapability/kind-swift.enum/percent.md)
  The percentage of the total task that has been completed.
- [CLSProgressReportingCapability.Kind.binary](clsprogressreportingcapability/kind-swift.enum/binary.md)
  A binary outcome for the task, like true or false.
- [CLSProgressReportingCapability.Kind.quantity](clsprogressreportingcapability/kind-swift.enum/quantity.md)
  A discrete value.
- [CLSProgressReportingCapability.Kind.score](clsprogressreportingcapability/kind-swift.enum/score.md)
  A score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsprogressreportingcapability/kind-swift.enum/duration)*