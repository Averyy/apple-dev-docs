# Operation.QueuePriority

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants let you prioritize the order in which operations execute.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum QueuePriority
```

```c
enum NSOperationQueuePriority : NSInteger;
```

#### Overview

You can use these constants to specify the relative ordering of operations that are waiting to be started in an operation queue. You should always use these constants (and not the defined value) for determining priority.

## Topics

### Constants
- [Operation.QueuePriority.veryLow](./queuepriority-swift.enum/verylow.md)
  Operations receive very low priority for execution.
- [Operation.QueuePriority.low](./queuepriority-swift.enum/low.md)
  Operations receive low priority for execution.
- [Operation.QueuePriority.normal](./queuepriority-swift.enum/normal.md)
  Operations receive the normal priority for execution.
- [Operation.QueuePriority.high](./queuepriority-swift.enum/high.md)
  Operations receive high priority for execution.
- [Operation.QueuePriority.veryHigh](./queuepriority-swift.enum/veryhigh.md)
  Operations receive very high priority for execution.
### Initializers
- [init?(rawValue: Int)](./queuepriority-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum QualityOfService](../qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/queuepriority-swift.enum)*