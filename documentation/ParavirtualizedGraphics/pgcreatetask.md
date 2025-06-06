# PGCreateTask

**Framework**: Paravirtualized Graphics  
**Kind**: typealias

The block signature for a routine that creates a task.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
typealias PGCreateTask = (UInt64, UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> OpaquePointer?
```

#### Return Value

A [`PGTask_t`](pgtask_t.md) pointer, or `NULL` if an error occurred.

#### Discussion

The paravirtualization framework calls this block to request memory for a task. The block allocates virtual memory for the task and returns it to the framework. The block also records any data it needs to keep track of this task and returns a pointer to that data. The framework uses this pointer to identify the task in other operations. The framework never accesses the contents of the [`PGTask_t`](pgtask_t.md) pointer.

## Parameters

- `vmSize`: The size of the virtual memory reservation to make for this task.
- `baseAddress`: On return, the block writes the base-host virtually contiguous address for this task.

## See Also

- [var createTask: PGCreateTask?](pgdevicedescriptor/createtask.md)
  A handler that the framework calls to create a task object.
- [var destroyTask: PGDestroyTask?](pgdevicedescriptor/destroytask.md)
  A handler that the framework calls to destroy a task object.
- [typealias PGDestroyTask](pgdestroytask.md)
  The block signature for a routine that destroys a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgcreatetask)*