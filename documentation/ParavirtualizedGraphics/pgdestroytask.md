# PGDestroyTask

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that destroys a task.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGDestroyTask = (OpaquePointer) -> Void
```

#### Discussion

The block must clean up any virtual memory that the device object allocated when it created the task.

## Parameters

- `task`: The task to destroy.

## See Also

- [var createTask: PGCreateTask?](pgdevicedescriptor/createtask.md)
  A handler that the framework calls to create a task object.
- [var destroyTask: PGDestroyTask?](pgdevicedescriptor/destroytask.md)
  A handler that the framework calls to destroy a task object.
- [typealias PGCreateTask](pgcreatetask.md)
  The block signature for a routine that creates a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdestroytask)*