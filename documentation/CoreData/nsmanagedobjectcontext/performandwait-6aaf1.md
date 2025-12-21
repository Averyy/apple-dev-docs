# performAndWait(_:)

**Framework**: Core Data  
**Kind**: method

Submits a closure to the context’s queue for synchronous execution.

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
@preconcurrency
nonisolated func performAndWait<T>(_ block: () throws -> T) rethrows -> T
```

#### Discussion

This method supports  — meaning it’s safe to call the method again, from within the closure, before the previous invocation completes.

## Parameters

- `block`: The closure to perform.

## See Also

- [func perform(() -> Void)](nsmanagedobjectcontext/perform(_:).md)
  Asynchronously performs the specified closure on the context’s queue.
- [func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () throws -> T) async rethrows -> T](nsmanagedobjectcontext/perform(schedule:_:).md)
  Submits a closure to the context’s queue for asynchronous execution.
- [func performAndWait(() -> Void)](nsmanagedobjectcontext/performandwait(_:)-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [NSManagedObjectContext.ScheduledTaskType](nsmanagedobjectcontext/scheduledtasktype.md)
  The different types of scheduled tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/performandwait(_:)-6aaf1)*