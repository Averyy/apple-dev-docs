# CLSProgressReportingCapability.Kind.percent

**Framework**: ClassKit  
**Kind**: case

The percentage of the total task that has been completed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case percent
```

#### Discussion

Add this capability to indicate that a context reports a task’s percentage completion on a periodic basis by setting the associated activity’s [`progress`](clsactivity/progress.md) property, or by calling the activity’s [`addProgressRange(fromStart:toEnd:)`](clsactivity/addprogressrange(fromstart:toend:).md) method.

## See Also

- [CLSProgressReportingCapability.Kind.duration](clsprogressreportingcapability/kind-swift.enum/duration.md)
  Time spent performing the task.
- [CLSProgressReportingCapability.Kind.binary](clsprogressreportingcapability/kind-swift.enum/binary.md)
  A binary outcome for the task, like true or false.
- [CLSProgressReportingCapability.Kind.quantity](clsprogressreportingcapability/kind-swift.enum/quantity.md)
  A discrete value.
- [CLSProgressReportingCapability.Kind.score](clsprogressreportingcapability/kind-swift.enum/score.md)
  A score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsprogressreportingcapability/kind-swift.enum/percent)*