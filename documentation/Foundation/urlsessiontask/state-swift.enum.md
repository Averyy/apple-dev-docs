# URLSessionTask.State

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Constants for determining the current state of a task.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum State
```

```c
enum NSURLSessionTaskState : NSInteger;
```

## Topics

### Task states
- [URLSessionTask.State.running](./state-swift.enum/running.md)
  The task is currently being serviced by the session.
- [URLSessionTask.State.suspended](./state-swift.enum/suspended.md)
  The task was suspended by the app.
- [URLSessionTask.State.canceling](./state-swift.enum/canceling.md)
  The task has received a `cancel` message.
- [URLSessionTask.State.completed](./state-swift.enum/completed.md)
  The task has completed (without being canceled), and the task’s delegate receives no further callbacks.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Controlling the task state
- [func cancel()](./cancel%28%29.md)
  Cancels the task.
- [func resume()](./resume%28%29.md)
  Resumes the task, if it is suspended.
- [func suspend()](./suspend%28%29.md)
  Temporarily suspends a task.
- [var state: URLSessionTask.State](./state-swift.property.md)
  The current state of the task—active, suspended, in the process of being canceled, or completed.
- [var priority: Float](./priority.md)
  The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
- [URL session task priority](../url-session-task-priority.md)
  Constants for providing task priority hints to a host, used with the [`priority`](./priority.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum)*