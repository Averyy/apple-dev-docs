# Operation.QueuePriority

**Framework**: Foundation  
**Kind**: enum

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

#### Overview

You can use these constants to specify the relative ordering of operations that are waiting to be started in an operation queue. You should always use these constants (and not the defined value) for determining priority.

## Topics

### Constants
- [Operation.QueuePriority.veryLow](operation/queuepriority-swift.enum/verylow.md)
  Operations receive very low priority for execution.
- [Operation.QueuePriority.low](operation/queuepriority-swift.enum/low.md)
  Operations receive low priority for execution.
- [Operation.QueuePriority.normal](operation/queuepriority-swift.enum/normal.md)
  Operations receive the normal priority for execution.
- [Operation.QueuePriority.high](operation/queuepriority-swift.enum/high.md)
  Operations receive high priority for execution.
- [Operation.QueuePriority.veryHigh](operation/queuepriority-swift.enum/veryhigh.md)
  Operations receive very high priority for execution.
- [Operation.QueuePriority.veryLow](operation/queuepriority-swift.enum/verylow.md)
  Operations receive very low priority for execution.
- [Operation.QueuePriority.low](operation/queuepriority-swift.enum/low.md)
  Operations receive low priority for execution.
- [Operation.QueuePriority.normal](operation/queuepriority-swift.enum/normal.md)
  Operations receive the normal priority for execution.
- [Operation.QueuePriority.high](operation/queuepriority-swift.enum/high.md)
  Operations receive high priority for execution.
- [Operation.QueuePriority.veryHigh](operation/queuepriority-swift.enum/veryhigh.md)
  Operations receive very high priority for execution.
### Initializers
- [init?(rawValue: Int)](operation/queuepriority-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum QualityOfService](qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/queuepriority-swift.enum)*