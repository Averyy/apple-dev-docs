# destroyTask

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property

A handler that the framework calls to destroy a task object.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite, nullable) PGDestroyTask destroyTask;
```

## See Also

### Managing Tasks
- [createTask](./createtask.md)
  A handler that the framework calls to create a task object.
- [PGCreateTask](../pgcreatetask.md)
  The block signature for a routine that creates a task.
- [PGDestroyTask](../pgdestroytask.md)
  The block signature for a routine that destroys a task.
- [PGTask_t](../pgtask_t.md)
  An opaque data pointer representing a specific virtual task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor/destroytask)*