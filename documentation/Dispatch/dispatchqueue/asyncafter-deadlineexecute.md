# asyncAfter(deadline:execute:)

**Framework**: Dispatch  
**Kind**: method

Schedules a work item for execution at the specified time, and returns immediately.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func asyncAfter(deadline: DispatchTime, execute: DispatchWorkItem)
```

## Parameters

- `deadline`: The time at which to schedule the work item for execution. Specifying the current time is less efficient than calling the   method directly. Do not specify the value in  ; doing so is undefined.
- `execute`: The work item containing the task to execute. For information on how to create this work item, see  .

## See Also

- [func async(execute: DispatchWorkItem)](dispatchqueue/async(execute:).md)
  Schedules a work item for immediate execution, and returns immediately.
- [func asyncAfter(deadline: DispatchTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](dispatchqueue/asyncafter(deadline:qos:flags:execute:).md)
  Schedules a block for execution using the specified attributes, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, execute: DispatchWorkItem)](dispatchqueue/asyncafter(walldeadline:execute:).md)
  Schedules a work item for execution after the specified time, and returns immediately.
- [func asyncAfter(wallDeadline: DispatchWallTime, qos: DispatchQoS, flags: DispatchWorkItemFlags, execute: () -> Void)](dispatchqueue/asyncafter(walldeadline:qos:flags:execute:).md)
  Schedules a block for execution using the specified attributes, and returns immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncafter(deadline:execute:))*