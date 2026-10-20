# async(execute:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Schedules a work item for immediate execution, and returns immediately.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func async(execute workItem: DispatchWorkItem)
```

## Parameters

- `workItem`: The work item containing the task to execute. For information on how to create this work item, see [`DispatchWorkItem`](../dispatchworkitem.md).

## See Also

### Executing Tasks Asynchronously
- [func asyncAfter(deadline: DispatchTime, execute: DispatchWorkItem)](./asyncafter%28deadline,execute%29.md)
  Schedules a work item for execution at the specified time, and returns immediately.
- [func asyncAfter(deadline: DispatchTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./asyncafter%28deadline,qos,flags,execute%29.md)
  Schedules a block for execution using the specified attributes, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, execute: DispatchWorkItem)](./asyncafter%28walldeadline,execute%29.md)
  Schedules a work item for execution after the specified time, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./asyncafter%28walldeadline,qos,flags,execute%29.md)
  Schedules a block for execution using the specified attributes, and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/async(execute:))*