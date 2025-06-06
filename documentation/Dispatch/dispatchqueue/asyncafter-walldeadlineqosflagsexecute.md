# asyncAfter(wallDeadline:qos:flags:execute:)

**Framework**: Dispatch  
**Kind**: method

Schedules a block for execution using the specified attributes, and returns immediately.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@preconcurrency
func asyncAfter(wallDeadline: DispatchWallTime, qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], execute work: @escaping () -> Void)
```

## Parameters

- `wallDeadline`: The time at which to schedule the block for execution. Specifying the current time is less efficient than calling the   method directly. Do not specify the value in  ; doing so is undefined.
- `qos`: The quality-of-service class to use when executing the block. This parameter determines the priority with which the block is scheduled and executed. For a list of possible values, see  .
- `flags`: Additional attributes to apply when executing the block. For a list of possible values, see  .
- `work`: The block containing the work to perform. This block has no return value and no parameters.

## See Also

- [func async(execute: DispatchWorkItem)](dispatchqueue/async(execute:).md)
  Schedules a work item for immediate execution, and returns immediately.
- [func asyncAfter(deadline: DispatchTime, execute: DispatchWorkItem)](dispatchqueue/asyncafter(deadline:execute:).md)
  Schedules a work item for execution at the specified time, and returns immediately.
- [func asyncAfter(deadline: DispatchTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](dispatchqueue/asyncafter(deadline:qos:flags:execute:).md)
  Schedules a block for execution using the specified attributes, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, execute: DispatchWorkItem)](dispatchqueue/asyncafter(walldeadline:execute:).md)
  Schedules a work item for execution after the specified time, and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncafter(walldeadline:qos:flags:execute:))*