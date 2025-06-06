# sync(execute:)

**Framework**: Dispatch  
**Kind**: method

Submits a work item for execution on the current queue and returns after that block finishes executing.

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
func sync(execute workItem: DispatchWorkItem)
```

## Parameters

- `workItem`: The dispatch work item containing the task to execute. For information on how to create this work item, see  .

## See Also

- [func sync(execute: () -> Void)](dispatchqueue/sync(execute:)-3segw.md)
  Submits a block object for execution and returns after that block finishes executing.
- [func sync<T>(execute: () throws -> T) rethrows -> T](dispatchqueue/sync(execute:)-20xby.md)
  Submits a work item for execution and returns the results from that item after it finishes executing.
- [func sync<T>(flags: DispatchWorkItemFlags, execute: () throws -> T) rethrows -> T](dispatchqueue/sync(flags:execute:).md)
  Submits a work item for execution using the specified attributes and returns the results from that item after it finishes executing.
- [func asyncAndWait(execute: () -> Void)](dispatchqueue/asyncandwait(execute:)-1udeu.md)
  Submits a work item for execution and returns only after it finishes executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/sync(execute:)-2fzvo)*