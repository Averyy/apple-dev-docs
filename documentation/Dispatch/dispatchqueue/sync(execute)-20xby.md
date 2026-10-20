# sync(execute:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Submits a work item for execution and returns the results from that item after it finishes executing.

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
func sync<T>(execute work: () throws -> T) rethrows -> T
```

#### Return Value

The return value of the item in the `work` parameter.

## Parameters

- `work`: The work item containing the work to perform. The block encapsulated by the work item should return a result, which is then returned by this method. For information on how to create this work item, see [`DispatchWorkItem`](../dispatchworkitem.md).

## See Also

### Executing Tasks Synchronously
- [func sync(execute: DispatchWorkItem)](./sync%28execute%29-2fzvo.md)
  Submits a work item for execution on the current queue and returns after that block finishes executing.
- [func sync(execute: () -> Void)](./sync%28execute%29-3segw.md)
  Submits a block object for execution and returns after that block finishes executing.
- [func sync<T>(flags: DispatchWorkItemFlags, execute: () throws -> T) rethrows -> T](./sync%28flags,execute%29.md)
  Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
- [func asyncAndWait(execute: () -> Void)](./asyncandwait%28execute%29-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/sync(execute:)-20xby)*