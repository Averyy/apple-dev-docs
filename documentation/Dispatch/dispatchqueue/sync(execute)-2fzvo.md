# sync(execute:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Submits a work item for execution on the current queue and returns after that block finishes executing.

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
func sync(execute workItem: DispatchWorkItem)
```

## Parameters

- `workItem`: The dispatch work item containing the task to execute. For information on how to create this work item, see [`DispatchWorkItem`](../dispatchworkitem.md).

## See Also

### Executing Tasks Synchronously
- [func sync(execute: () -> Void)](./sync%28execute%29-3segw.md)
  Submits a block object for execution and returns after that block finishes executing.
- [func sync<T>(execute: () throws -> T) rethrows -> T](./sync%28execute%29-20xby.md)
  Submits a work item for execution and returns the results from that item after it finishes executing.
- [func sync<T>(flags: DispatchWorkItemFlags, execute: () throws -> T) rethrows -> T](./sync%28flags,execute%29.md)
  Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
- [func asyncAndWait(execute: () -> Void)](./asyncandwait%28execute%29-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/sync(execute:)-2fzvo)*