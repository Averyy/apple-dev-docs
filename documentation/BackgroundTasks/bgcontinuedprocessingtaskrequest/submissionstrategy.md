# BGContinuedProcessingTaskRequest.SubmissionStrategy

**Framework**: Background Tasks  
**Kind**: enum  
**Role**: Enumeration

The ways your app suggests the system handle your task’s submission under varying conditions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum SubmissionStrategy
```

```c
enum BGContinuedProcessingTaskRequestSubmissionStrategy : NSInteger;
```

## Overview

The Continuous Background Task request ([`BGContinuedProcessingTaskRequest`](../bgcontinuedprocessingtaskrequest.md)) property [`strategy`](./strategy.md) is of this type.

For more information on submission strategies, see [Performing long-running tasks on iOS and iPadOS](../performing-long-running-tasks-on-ios-and-ipados.md).

## Topics

### Choosing a strategy
- [BGContinuedProcessingTaskRequest.SubmissionStrategy.fail](./submissionstrategy/fail.md)
  An option that fails the submission of a continuous background task if the system can’t run it immediately.
- [BGContinuedProcessingTaskRequest.SubmissionStrategy.queue](./submissionstrategy/queue.md)
  An option that queues a continuous background task to begin as soon as possible.
### Creating a strategy
- [init?(rawValue: Int)](./submissionstrategy/init%28rawvalue%29.md)
  Creates a submission strategy.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Choosing a processing strategy
- [var strategy: BGContinuedProcessingTaskRequest.SubmissionStrategy](./strategy.md)
  The submission strategy for the scheduler to abide by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/submissionstrategy)*