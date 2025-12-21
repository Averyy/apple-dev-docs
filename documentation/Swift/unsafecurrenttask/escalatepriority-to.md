# escalatePriority(to:)

**Framework**: Swift  
**Kind**: method

Escalate the task `priority` of the passed in task to the `newPriority`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func escalatePriority(to newPriority: TaskPriority)
```

#### Discussion

> ⚠️ **Warning**: This API should rarely be used, and instead you can rely on structured concurrency and implicit priority escalation which happens when a higher priority task awaits on a result of a lower priority task. I.e. using `await` on the target task usually is the correct way to escalate the target task to the current priority of the calling task, especially because in such setup if the waiting task gets escalated, the waited on task would be escalated automatically as well.

The concurrency runtime is free to interpret and handle escalation depending on platform characteristics.

Priority escalation is propagated to child tasks of the waited-on task, and will trigger any priority escalation handlers, if any were registered.

Escalation can only  the priority of a task, and de-escalating priority is not supported.

This method can be called from any task or thread.

## Parameters

- `newPriority`: The new priority the task should continue executing on


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafecurrenttask/escalatepriority(to:))*