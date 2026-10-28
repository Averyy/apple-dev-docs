# CLSProgressReportingCapability.Kind.binary

**Framework**: ClassKit  
**Kind**: case  
**Role**: Case

A binary outcome for the task, like true or false.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case binary
```

```c
CLSProgressReportingCapabilityKindBinary
```

## Discussion

Add this capability to indicate that a context reports a binary condition at the end of a task, like pass or fail, using a [`CLSBinaryItem`](../../clsbinaryitem.md) instance.

## See Also

### Reporting capabilities
- [CLSProgressReportingCapability.Kind.duration](./duration.md)
  Time spent performing the task.
- [CLSProgressReportingCapability.Kind.percent](./percent.md)
  The percentage of the total task that has been completed.
- [CLSProgressReportingCapability.Kind.quantity](./quantity.md)
  A discrete value.
- [CLSProgressReportingCapability.Kind.score](./score.md)
  A score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsprogressreportingcapability/kind-swift.enum/binary)*