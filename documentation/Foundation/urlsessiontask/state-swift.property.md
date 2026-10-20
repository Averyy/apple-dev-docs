# state

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The current state of the task—active, suspended, in the process of being canceled, or completed.

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
var state: URLSessionTask.State { get }
```

```objc
@property (readonly) NSURLSessionTaskState state;
```

## See Also

### Controlling the task state
- [func cancel()](./cancel%28%29.md)
  Cancels the task.
- [func resume()](./resume%28%29.md)
  Resumes the task, if it is suspended.
- [func suspend()](./suspend%28%29.md)
  Temporarily suspends a task.
- [URLSessionTask.State](./state-swift.enum.md)
  Constants for determining the current state of a task.
- [var priority: Float](./priority.md)
  The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
- [URL session task priority](../url-session-task-priority.md)
  Constants for providing task priority hints to a host, used with the [`priority`](./priority.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.property)*