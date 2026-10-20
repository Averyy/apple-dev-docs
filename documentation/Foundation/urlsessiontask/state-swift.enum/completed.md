# URLSessionTask.State.completed

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The task has completed (without being canceled), and the task’s delegate receives no further callbacks.

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
case completed
```

```c
NSURLSessionTaskStateCompleted
```

#### Discussion

If the task completed successfully, the task’s [`error`](../error.md) property is `nil`. Otherwise, it provides an error object that tells what went wrong. A task in this state is not subject to timeouts.

## See Also

### Task states
- [URLSessionTask.State.running](./running.md)
  The task is currently being serviced by the session.
- [URLSessionTask.State.suspended](./suspended.md)
  The task was suspended by the app.
- [URLSessionTask.State.canceling](./canceling.md)
  The task has received a `cancel` message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum/completed)*