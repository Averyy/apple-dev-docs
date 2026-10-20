# asyncAfter(deadline:qos:flags:execute:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Schedules a block for execution using the specified attributes, and returns immediately.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
@preconcurrency
func asyncAfter(deadline: DispatchTime, qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], execute work: @escaping @Sendable () -> Void)
```

## Parameters

- `deadline`: The time at which to schedule the block for execution. Specifying the current time is less efficient than calling the [`async(execute:)`](./async%28execute%29.md) method directly. Do not specify the value in [`distantFuture`](../dispatchtime/distantfuture.md); doing so is undefined.
- `qos`: The quality-of-service class to use when executing the block. This parameter determines the priority with which the block is scheduled and executed. For a list of possible values, see [`DispatchQoS`](../dispatchqos.md).
- `flags`: Additional attributes to apply when executing the block. For a list of possible values, see [`DispatchWorkItemFlags`](../dispatchworkitemflags.md).
- `work`: The block containing the work to perform. This block has no return value and no parameters.

## See Also

### Executing Tasks Asynchronously
- [func async(execute: DispatchWorkItem)](./async%28execute%29.md)
  Schedules a work item for immediate execution, and returns immediately.
- [func asyncAfter(deadline: DispatchTime, execute: DispatchWorkItem)](./asyncafter%28deadline,execute%29.md)
  Schedules a work item for execution at the specified time, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, execute: DispatchWorkItem)](./asyncafter%28walldeadline,execute%29.md)
  Schedules a work item for execution after the specified time, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](./asyncafter%28walldeadline,qos,flags,execute%29.md)
  Schedules a block for execution using the specified attributes, and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncafter(deadline:qos:flags:execute:))*