# MLJob

**Framework**: Create ML  
**Kind**: class

The representation of a model’s asynchronous training session you use to monitor the session’s progress or terminate its execution.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
final class MLJob<Result>
```

## Topics

### Receiving progress updates
- [var checkpoints: AnyPublisher<MLCheckpoint, Never>](mljob/checkpoints.md)
  A publisher that sends a checkpoint for each of the session’s checkpoint intervals.
- [var result: AnyPublisher<Result, any Error>](mljob/result.md)
  A publisher that provides a result when the training session has finished.
- [var phase: AnyPublisher<MLPhase, Never>](mljob/phase.md)
  Phase publisher.
### Managing a job
- [func cancel()](mljob/cancel.md)
  Stops the training session’s execution.
- [var isCanceled: Bool](mljob/iscanceled.md)
  A Boolean value that indicates whether you canceled the job.
### Inspecting a job
- [let startDate: Date](mljob/startdate.md)
  The date and time when the training session began.
- [let progress: Progress](mljob/progress.md)
  The training session’s current progress.
- [struct MLProgress](mlprogress.md)
  A convenience type that exposes information about the progress of a training session.
### Default Implementations
- [Cancellable Implementations](mljob/cancellable-implementations.md)

## Relationships

### Conforms To
- [Cancellable](../Combine/Cancellable.md)

## See Also

- [class MLTrainingSession](mltrainingsession.md)
  The current state of a model’s asynchronous training session.
- [struct MLTrainingSessionParameters](mltrainingsessionparameters.md)
  The configuration settings for a training session.
- [struct MLCheckpoint](mlcheckpoint.md)
  The state of a model’s asynchronous training session at a specific point in time during the feature extraction or training phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mljob)*