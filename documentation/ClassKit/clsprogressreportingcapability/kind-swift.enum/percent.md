# CLSProgressReportingCapability.Kind.percent

**Framework**: ClassKit  
**Kind**: case  
**Role**: Case

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

```c
CLSProgressReportingCapabilityKindPercent
```

## Discussion

Add this capability to indicate that a context reports a task’s percentage completion on a periodic basis by setting the associated activity’s [`progress`](../../clsactivity/progress.md) property, or by calling the activity’s [`addProgressRange(fromStart:toEnd:)`](../../clsactivity/addprogressrange%28fromstart,toend%29.md) method.

## See Also

### Reporting capabilities
- [CLSProgressReportingCapability.Kind.duration](./duration.md)
  Time spent performing the task.
- [CLSProgressReportingCapability.Kind.binary](./binary.md)
  A binary outcome for the task, like true or false.
- [CLSProgressReportingCapability.Kind.quantity](./quantity.md)
  A discrete value.
- [CLSProgressReportingCapability.Kind.score](./score.md)
  A score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsprogressreportingcapability/kind-swift.enum/percent)*