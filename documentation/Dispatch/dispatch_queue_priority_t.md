# dispatch_queue_priority_t

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

The execution priority for tasks in a global concurrent queue.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef long dispatch_queue_priority_t;
```

#### Discussion

In macOS 10.10 and later, use quality-of-service (QoS) classes to specify the priority of tasks instead.

## Topics

### Priorities
- [var DISPATCH_QUEUE_PRIORITY_HIGH: Int32](./dispatch_queue_priority_high.md)
  Tasks run at the highest priority, which is equivalent to the user-initiated quality-of-service level.
- [var DISPATCH_QUEUE_PRIORITY_DEFAULT: Int32](./dispatch_queue_priority_default.md)
  Tasks run at the default priority, which is equivalent to the default quality-of-service.
- [var DISPATCH_QUEUE_PRIORITY_LOW: Int32](./dispatch_queue_priority_low.md)
  Tasks run at a low priority, which is equivalent to the utility quality-of-service level.
- [var DISPATCH_QUEUE_PRIORITY_BACKGROUND: Int32](./dispatch_queue_priority_background.md)
  Tasks run at the background priority, which is equivalent to the background quality-of-service level.

## See Also

### Thread Scheduling
- [dispatch_qos_class_t](./dispatch_qos_class_t.md)
  Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_set_qos_class_floor](./dispatch_set_qos_class_floor.md)
  Specifies the minimum quality-of-service level for a dispatch queue, source, or workloop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_priority_t)*