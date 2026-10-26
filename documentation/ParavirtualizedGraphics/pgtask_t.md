# PGTask_t

**Framework**: Paravirtualized Graphics  
**Kind**: typealias  
**Role**: Type Alias

An opaque data pointer representing a specific virtual task.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```c
typedef struct PGTask_s PGTask_t;
```

#### Discussion

A client using the framework determines which data it needs to keep track of each task. The framework never accesses the contents of the pointer.

## See Also

### Managing Tasks
- [createTask](./pgdevicedescriptor/createtask.md)
  A handler that the framework calls to create a task object.
- [destroyTask](./pgdevicedescriptor/destroytask.md)
  A handler that the framework calls to destroy a task object.
- [PGCreateTask](./pgcreatetask.md)
  The block signature for a routine that creates a task.
- [PGDestroyTask](./pgdestroytask.md)
  The block signature for a routine that destroys a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgtask_t)*