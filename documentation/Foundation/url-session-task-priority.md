# URL session task priority

**Framework**: Foundation

Constants for providing task priority hints to a host, used with the [`priority`](urlsessiontask/priority.md) property.

## Topics

### Priority constants
- [class let defaultPriority: Float](urlsessiontask/defaultpriority.md)
  The default URL session task priority, used implicitly for any task you have not prioritized.
- [class let lowPriority: Float](urlsessiontask/lowpriority.md)
  A low URL session task priority, with a floating point value above the minimum of `0` and below the default value.
- [class let highPriority: Float](urlsessiontask/highpriority.md)
  A high URL session task priority, with a floating point value above the default value and below the maximum of `1.0`.

## See Also

- [func cancel()](urlsessiontask/cancel.md)
  Cancels the task.
- [func resume()](urlsessiontask/resume.md)
  Resumes the task, if it is suspended.
- [func suspend()](urlsessiontask/suspend.md)
  Temporarily suspends a task.
- [var state: URLSessionTask.State](urlsessiontask/state-swift.property.md)
  The current state of the task—active, suspended, in the process of being canceled, or completed.
- [URLSessionTask.State](urlsessiontask/state-swift.enum.md)
  Constants for determining the current state of a task.
- [var priority: Float](urlsessiontask/priority.md)
  The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url-session-task-priority)*