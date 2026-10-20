# perform(schedule:_:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Submits a closure to the context’s queue for asynchronous execution.

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
@preconcurrency
nonisolated func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType = .immediate, _ block: @escaping @Sendable () throws -> T) async rethrows -> T
```

## Parameters

- `schedule`: The required execution schedule. For more information, see [`NSManagedObjectContext.ScheduledTaskType`](./scheduledtasktype.md).
- `block`: The closure to perform.

## See Also

### Performing block operations
- [func perform(() -> Void)](./perform%28_%29.md)
  Asynchronously performs the specified closure on the context’s queue.
- [func performAndWait(() -> Void)](./performandwait%28_%29-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [func performAndWait<T>(() throws -> T) rethrows -> T](./performandwait%28_%29-6aaf1.md)
  Submits a closure to the context’s queue for synchronous execution.
- [NSManagedObjectContext.ScheduledTaskType](./scheduledtasktype.md)
  The different types of scheduled tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/perform(schedule:_:))*