# CLSProgressReportingCapability.Kind.duration

**Framework**: ClassKit  
**Kind**: case  
**Role**: Case

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

```c
CLSProgressReportingCapabilityKindDuration
```

## Discussion

The framework automatically measures the time that a student spends working on a task, so all contexts have a [`CLSProgressReportingCapability.Kind.duration`](./duration.md) capability by default. You can replace the default one with a new one if you want to customize the [`details`](../details.md) string.

## See Also

### Reporting capabilities
- [CLSProgressReportingCapability.Kind.percent](./percent.md)
  The percentage of the total task that has been completed.
- [CLSProgressReportingCapability.Kind.binary](./binary.md)
  A binary outcome for the task, like true or false.
- [CLSProgressReportingCapability.Kind.quantity](./quantity.md)
  A discrete value.
- [CLSProgressReportingCapability.Kind.score](./score.md)
  A score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsprogressreportingcapability/kind-swift.enum/duration)*