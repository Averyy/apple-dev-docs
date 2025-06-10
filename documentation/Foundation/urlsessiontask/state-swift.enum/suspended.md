# URLSessionTask.State.suspended

**Framework**: Foundation  
**Kind**: case

The task was suspended by the app.

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
case suspended
```

#### Discussion

No further processing takes place until the task is resumed. A task in this state is not subject to timeouts.

## See Also

- [URLSessionTask.State.running](urlsessiontask/state-swift.enum/running.md)
  The task is currently being serviced by the session.
- [URLSessionTask.State.canceling](urlsessiontask/state-swift.enum/canceling.md)
  The task has received a `cancel` message.
- [URLSessionTask.State.completed](urlsessiontask/state-swift.enum/completed.md)
  The task has completed (without being canceled), and the task’s delegate receives no further callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/state-swift.enum/suspended)*