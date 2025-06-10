# URLSessionTask.State.running

**Framework**: Foundation  
**Kind**: case

The task is currently being serviced by the session.

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
case running
```

#### Discussion

A task in this state is subject to the request and resource timeouts specified in the session configuration object.

## See Also

- [URLSessionTask.State.suspended](urlsessiontask/state-swift.enum/suspended.md)
  The task was suspended by the app.
- [URLSessionTask.State.canceling](urlsessiontask/state-swift.enum/canceling.md)
  The task has received a `cancel` message.
- [URLSessionTask.State.completed](urlsessiontask/state-swift.enum/completed.md)
  The task has completed (without being canceled), and the task’s delegate receives no further callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum/running)*