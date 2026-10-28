# DISPATCH_QUEUE_PRIORITY_DEFAULT

**Framework**: Dispatch  
**Kind**: var  
**Role**: Global Variable

Tasks run at the default priority, which is equivalent to the default quality-of-service.

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
var DISPATCH_QUEUE_PRIORITY_DEFAULT: Int32 { get }
```

```c
#define DISPATCH_QUEUE_PRIORITY_DEFAULT
```

## Discussion

Use quality-of-service constants instead. This constant maps to the `QOS_CLASS_DEFAULT` class.

Items dispatched to the queue run at the default priority; the queue is scheduled for execution after all high priority queues have been scheduled, but before any low priority queues have been scheduled.

## See Also

### Priorities
- [var DISPATCH_QUEUE_PRIORITY_HIGH: Int32](./dispatch_queue_priority_high.md)
  Tasks run at the highest priority, which is equivalent to the user-initiated quality-of-service level.
- [var DISPATCH_QUEUE_PRIORITY_LOW: Int32](./dispatch_queue_priority_low.md)
  Tasks run at a low priority, which is equivalent to the utility quality-of-service level.
- [var DISPATCH_QUEUE_PRIORITY_BACKGROUND: Int32](./dispatch_queue_priority_background.md)
  Tasks run at the background priority, which is equivalent to the background quality-of-service level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_priority_default)*