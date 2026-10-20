# asyncAfter(deadline:execute:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Schedules a work item for execution at the specified time, and returns immediately.

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
func asyncAfter(deadline: DispatchTime, execute: DispatchWorkItem)
```

## Parameters

- `deadline`: The time at which to schedule the work item for execution. Specifying the current time is less efficient than calling the [`async(execute:)`](./async%28execute%29.md) method directly. Do not specify the value in [`distantFuture`](../dispatchtime/distantfuture.md); doing so is undefined.
- `execute`: The work item containing the task to execute. For information on how to create this work item, see [`DispatchWorkItem`](../dispatchworkitem.md).

## See Also

### Executing Tasks Asynchronously
- [func async(execute: DispatchWorkItem)](./async%28execute%29.md)
  Schedules a work item for immediate execution, and returns immediately.
- [func asyncAfter(deadline: DispatchTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./asyncafter%28deadline,qos,flags,execute%29.md)
  Schedules a block for execution using the specified attributes, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, execute: DispatchWorkItem)](./asyncafter%28walldeadline,execute%29.md)
  Schedules a work item for execution after the specified time, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./asyncafter%28walldeadline,qos,flags,execute%29.md)
  Schedules a block for execution using the specified attributes, and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncafter(deadline:execute:))*