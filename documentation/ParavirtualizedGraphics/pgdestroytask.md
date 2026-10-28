# PGDestroyTask

**Framework**: Paravirtualized Graphics  
**Kind**: typealias  
**Role**: Type Alias

The block signature for a routine that destroys a task.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```c
typedef void (^)(struct PGTask_s *) PGDestroyTask;
```

## Discussion

The block must clean up any virtual memory that the device object allocated when it created the task.

## Parameters

- `task`: The task to destroy.

## See Also

### Managing Tasks
- [createTask](./pgdevicedescriptor/createtask.md)
  A handler that the framework calls to create a task object.
- [destroyTask](./pgdevicedescriptor/destroytask.md)
  A handler that the framework calls to destroy a task object.
- [PGCreateTask](./pgcreatetask.md)
  The block signature for a routine that creates a task.
- [PGTask_t](./pgtask_t.md)
  An opaque data pointer representing a specific virtual task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdestroytask)*