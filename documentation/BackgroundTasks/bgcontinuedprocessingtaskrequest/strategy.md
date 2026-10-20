# strategy

**Framework**: Background Tasks  
**Kind**: property  
**Role**: Instance Property

The submission strategy for the scheduler to abide by.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var strategy: BGContinuedProcessingTaskRequest.SubmissionStrategy { get set }
```

```objc
@property (nonatomic) BGContinuedProcessingTaskRequestSubmissionStrategy strategy;
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](../performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

The default value is [`BGContinuedProcessingTaskRequest.SubmissionStrategy.queue`](./submissionstrategy/queue.md).

## See Also

### Choosing a processing strategy
- [BGContinuedProcessingTaskRequest.SubmissionStrategy](./submissionstrategy.md)
  The ways your app suggests the system handle your task’s submission under varying conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/strategy)*