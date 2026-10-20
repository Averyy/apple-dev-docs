# performAndWait(_:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Submits a closure to the context’s queue for synchronous execution.

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
nonisolated func performAndWait<T>(_ block: @Sendable () throws -> T) rethrows -> T
```

#### Discussion

This method supports *reentrancy* — meaning it’s safe to call the method again, from within the closure, before the previous invocation completes.

## Parameters

- `block`: The closure to perform.

## See Also

### Performing block operations
- [func perform(() -> Void)](./perform%28_%29.md)
  Asynchronously performs the specified closure on the context’s queue.
- [func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () throws -> T) async rethrows -> T](./perform%28schedule,_%29.md)
  Submits a closure to the context’s queue for asynchronous execution.
- [func performAndWait(() -> Void)](./performandwait%28_%29-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [NSManagedObjectContext.ScheduledTaskType](./scheduledtasktype.md)
  The different types of scheduled tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/performandwait(_:)-6aaf1)*