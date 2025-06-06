# perform(_:)

**Framework**: Core Data  
**Kind**: method

Asynchronously performs the specified closure on the context’s queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func perform(_ block: @escaping () -> Void)
```

## Mentions

- [Using Core Data in the background](using-core-data-in-the-background.md)

#### Discussion

This method encapsulates an autorelease pool and a call to [`processPendingChanges()`](nsmanagedobjectcontext/processpendingchanges().md).

## Parameters

- `block`: The closure to perform.

## See Also

- [func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () throws -> T) async rethrows -> T](nsmanagedobjectcontext/perform(schedule:_:).md)
  Submits a closure to the context’s queue for asynchronous execution.
- [func performAndWait(() -> Void)](nsmanagedobjectcontext/performandwait(_:)-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [func performAndWait<T>(() throws -> T) rethrows -> T](nsmanagedobjectcontext/performandwait(_:)-6aaf1.md)
  Submits a closure to the context’s queue for synchronous execution.
- [NSManagedObjectContext.ScheduledTaskType](nsmanagedobjectcontext/scheduledtasktype.md)
  The different types of scheduled tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/perform(_:))*