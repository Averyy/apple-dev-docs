# DISPATCH_QUEUE_PRIORITY_HIGH

**Framework**: Dispatch  
**Kind**: var  
**Role**: Global Variable

Tasks run at the highest priority, which is equivalent to the user-initiated quality-of-service level.

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
var DISPATCH_QUEUE_PRIORITY_HIGH: Int32 { get }
```

```c
#define DISPATCH_QUEUE_PRIORITY_HIGH
```

## Discussion

Use quality-of-service constants instead. This constant maps to the `QOS_CLASS_USER_INITIATED` class.

Items dispatched to the queue run at high priority; the queue is scheduled for execution before any default priority or low priority queue.

## See Also

### Priorities
- [var DISPATCH_QUEUE_PRIORITY_DEFAULT: Int32](./dispatch_queue_priority_default.md)
  Tasks run at the default priority, which is equivalent to the default quality-of-service.
- [var DISPATCH_QUEUE_PRIORITY_LOW: Int32](./dispatch_queue_priority_low.md)
  Tasks run at a low priority, which is equivalent to the utility quality-of-service level.
- [var DISPATCH_QUEUE_PRIORITY_BACKGROUND: Int32](./dispatch_queue_priority_background.md)
  Tasks run at the background priority, which is equivalent to the background quality-of-service level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_queue_priority_high)*