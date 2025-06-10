# BGContinuedProcessingTaskRequest.SubmissionStrategy

**Framework**: Background Tasks  
**Kind**: enum

The ways your app suggests the system handle your task’s submission under varying conditions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum SubmissionStrategy
```

#### Overview

The Continuous Background Task request ([`BGContinuedProcessingTaskRequest`](bgcontinuedprocessingtaskrequest.md)) property [`strategy`](bgcontinuedprocessingtaskrequest/strategy.md) is of this type.

For more information on submission strategies, see [`Performing long-running tasks on iOS and iPadOS`](performing-long-running-tasks-on-ios-and-ipados.md).

## Topics

### Choosing a strategy
- [BGContinuedProcessingTaskRequest.SubmissionStrategy.fail](bgcontinuedprocessingtaskrequest/submissionstrategy/fail.md)
  An option that fails the submission of a continuous background task if the system can’t run it immediately.
- [BGContinuedProcessingTaskRequest.SubmissionStrategy.queue](bgcontinuedprocessingtaskrequest/submissionstrategy/queue.md)
  An option that queues a continuous background task to begin as soon as possible.
### Creating a strategy
- [init?(rawValue: Int)](bgcontinuedprocessingtaskrequest/submissionstrategy/init(rawvalue:).md)
  Creates a submission strategy.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var strategy: BGContinuedProcessingTaskRequest.SubmissionStrategy](bgcontinuedprocessingtaskrequest/strategy.md)
  The submission strategy for the scheduler to abide by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy)*