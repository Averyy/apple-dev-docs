# NSManagedObjectContext.ScheduledTaskType

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

The different types of scheduled tasks.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
enum ScheduledTaskType
```

## Topics

### Scheduled Task Types
- [NSManagedObjectContext.ScheduledTaskType.enqueued](./scheduledtasktype/enqueued.md)
  The enqueued scheduled task type.
- [NSManagedObjectContext.ScheduledTaskType.immediate](./scheduledtasktype/immediate.md)
  The immediate scheduled task type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Performing block operations
- [func perform(() -> Void)](./perform%28_%29.md)
  Asynchronously performs the specified closure on the context’s queue.
- [func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () throws -> T) async rethrows -> T](./perform%28schedule,_%29.md)
  Submits a closure to the context’s queue for asynchronous execution.
- [func performAndWait(() -> Void)](./performandwait%28_%29-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [func performAndWait<T>(() throws -> T) rethrows -> T](./performandwait%28_%29-6aaf1.md)
  Submits a closure to the context’s queue for synchronous execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype)*