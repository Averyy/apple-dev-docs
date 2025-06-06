# perform(schedule:_:)

**Framework**: Core Data  
**Kind**: method

Submits a closure to the context’s queue for asynchronous execution.

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
func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType = .immediate, _ block: @escaping () throws -> T) async rethrows -> T
```

## Parameters

- `schedule`: The required execution schedule. For more information, see  .
- `block`: The closure to perform.

## See Also

- [func perform(() -> Void)](nsmanagedobjectcontext/perform(_:).md)
  Asynchronously performs the specified closure on the context’s queue.
- [func performAndWait(() -> Void)](nsmanagedobjectcontext/performandwait(_:)-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [func performAndWait<T>(() throws -> T) rethrows -> T](nsmanagedobjectcontext/performandwait(_:)-6aaf1.md)
  Submits a closure to the context’s queue for synchronous execution.
- [NSManagedObjectContext.ScheduledTaskType](nsmanagedobjectcontext/scheduledtasktype.md)
  The different types of scheduled tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/perform(schedule:_:))*