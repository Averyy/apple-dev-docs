# CLSProgressReportingCapability.Kind

**Framework**: ClassKit  
**Kind**: enum

The available kinds of progress reporting that a context can perform.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum Kind
```

#### Overview

Use one of these values to set the [`kind`](clsprogressreportingcapability/kind-swift.property.md) property in each [`CLSProgressReportingCapability`](clsprogressreportingcapability.md) instance when constructing a set of capabilities used to configure a context. Each kind corresponds to a different metric that you provide, like a score or a progress indication.

## Topics

### Reporting Capabilities
- [CLSProgressReportingCapability.Kind.duration](clsprogressreportingcapability/kind-swift.enum/duration.md)
  Time spent performing the task.
- [CLSProgressReportingCapability.Kind.percent](clsprogressreportingcapability/kind-swift.enum/percent.md)
  The percentage of the total task that has been completed.
- [CLSProgressReportingCapability.Kind.binary](clsprogressreportingcapability/kind-swift.enum/binary.md)
  A binary outcome for the task, like true or false.
- [CLSProgressReportingCapability.Kind.quantity](clsprogressreportingcapability/kind-swift.enum/quantity.md)
  A discrete value.
- [CLSProgressReportingCapability.Kind.score](clsprogressreportingcapability/kind-swift.enum/score.md)
  A score.
### Initializers
- [init?(rawValue: Int)](clsprogressreportingcapability/kind-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var details: String?](clsprogressreportingcapability/details.md)
  A description of the capability presented to teachers.
- [var kind: CLSProgressReportingCapability.Kind](clsprogressreportingcapability/kind-swift.property.md)
  The kind of progress reporting capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsprogressreportingcapability/kind-swift.enum)*