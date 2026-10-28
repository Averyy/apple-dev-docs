# CLSProgressReportingCapability.Kind

**Framework**: ClassKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CLSProgressReportingCapabilityKind : NSInteger;
```

## Overview

Use one of these values to set the [`kind`](./kind-swift.property.md) property in each [`CLSProgressReportingCapability`](../clsprogressreportingcapability.md) instance when constructing a set of capabilities used to configure a context. Each kind corresponds to a different metric that you provide, like a score or a progress indication.

## Topics

### Reporting capabilities
- [CLSProgressReportingCapability.Kind.duration](./kind-swift.enum/duration.md)
  Time spent performing the task.
- [CLSProgressReportingCapability.Kind.percent](./kind-swift.enum/percent.md)
  The percentage of the total task that has been completed.
- [CLSProgressReportingCapability.Kind.binary](./kind-swift.enum/binary.md)
  A binary outcome for the task, like true or false.
- [CLSProgressReportingCapability.Kind.quantity](./kind-swift.enum/quantity.md)
  A discrete value.
- [CLSProgressReportingCapability.Kind.score](./kind-swift.enum/score.md)
  A score.
### Initializers
- [init?(rawValue: Int)](./kind-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Characterizing the Capability
- [var details: String?](./details.md)
  A description of the capability presented to teachers.
- [var kind: CLSProgressReportingCapability.Kind](./kind-swift.property.md)
  The kind of progress reporting capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsprogressreportingcapability/kind-swift.enum)*