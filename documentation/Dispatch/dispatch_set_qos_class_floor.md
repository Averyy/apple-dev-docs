# dispatch_set_qos_class_floor

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Specifies the minimum quality-of-service level for a dispatch queue, source, or workloop.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```c
extern void dispatch_set_qos_class_floor(dispatch_object_t object, dispatch_qos_class_t qos_class, int relative_priority);
```

#### Discussion

Use this function to enforce a minimum QoS level on all tasks you assign to the object. If the QoS level of a work item is below the specified minimum, the queue, source, or workloop elevates the priority of that work item to the minimum value. Elevation of the priority happens even if the work item doesn’t have “enforce” semantics in place.

## Parameters

- `object`: The [`dispatch_queue_t`](./dispatch_queue_t.md), [`dispatch_source_t`](./dispatch_source_t.md), or [`dispatch_workloop_t`](./dispatch_workloop_t.md) object you want to modify. This object must be currently inactive. If you specify an object other than a dispatch queue, source, or workloop, this function terminates the current process.
- `qos_class`: The minimum quality-of-service (QoS) level to assign to the object.
- `relative_priority`: The relative priority within the QoS level. This value is a negative offset from the scheduler priority associated with the value in qos_class. This value must not be greater than `0`.

## See Also

### Thread Scheduling
- [dispatch_qos_class_t](./dispatch_qos_class_t.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_queue_priority_t](./dispatch_queue_priority_t.md)
  The execution priority for tasks in a global concurrent queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_set_qos_class_floor)*