# DISPATCH_QUEUE_PRIORITY_BACKGROUND

**Framework**: Dispatch  
**Kind**: var  
**Role**: Global Variable

Tasks run at the background priority, which is equivalent to the background quality-of-service level.

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
var DISPATCH_QUEUE_PRIORITY_BACKGROUND: Int32 { get }
```

```c
#define DISPATCH_QUEUE_PRIORITY_BACKGROUND
```

## Discussion

Use quality-of-service constants instead. This constant maps to the `QOS_CLASS_BACKGROUND` class.

Items dispatched to the queue run at background priority; the queue is scheduled for execution after all high priority queues have been scheduled and the system runs items on a thread whose priority is set for background status. Such a thread has the lowest priority and any disk I/O is throttled to minimize the impact on the system.

## See Also

### Priorities
- [var DISPATCH_QUEUE_PRIORITY_HIGH: Int32](./dispatch_queue_priority_high.md)
  Tasks run at the highest priority, which is equivalent to the user-initiated quality-of-service level.
- [var DISPATCH_QUEUE_PRIORITY_DEFAULT: Int32](./dispatch_queue_priority_default.md)
  Tasks run at the default priority, which is equivalent to the default quality-of-service.
- [var DISPATCH_QUEUE_PRIORITY_LOW: Int32](./dispatch_queue_priority_low.md)
  Tasks run at a low priority, which is equivalent to the utility quality-of-service level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_priority_background)*