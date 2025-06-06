# NSManagedObjectContext.ScheduledTaskType

**Framework**: Core Data  
**Kind**: enum

The different types of scheduled tasks.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
enum ScheduledTaskType
```

## Topics

### Scheduled Task Types
- [NSManagedObjectContext.ScheduledTaskType.enqueued](nsmanagedobjectcontext/scheduledtasktype/enqueued.md)
  The enqueued scheduled task type.
- [NSManagedObjectContext.ScheduledTaskType.immediate](nsmanagedobjectcontext/scheduledtasktype/immediate.md)
  The immediate scheduled task type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func perform(() -> Void)](nsmanagedobjectcontext/perform(_:).md)
  Asynchronously performs the specified closure on the context’s queue.
- [func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () throws -> T) async rethrows -> T](nsmanagedobjectcontext/perform(schedule:_:).md)
  Submits a closure to the context’s queue for asynchronous execution.
- [func performAndWait(() -> Void)](nsmanagedobjectcontext/performandwait(_:)-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [func performAndWait<T>(() throws -> T) rethrows -> T](nsmanagedobjectcontext/performandwait(_:)-6aaf1.md)
  Submits a closure to the context’s queue for synchronous execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype)*