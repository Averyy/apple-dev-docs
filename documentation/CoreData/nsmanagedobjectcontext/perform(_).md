# perform(_:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Asynchronously performs the specified closure on the context’s queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func perform(_ block: @escaping @Sendable () -> Void)
```

```objc
- (void) performBlock:(void (^)()) block;
```

## Mentions

- [Using Core Data in the background](../using-core-data-in-the-background.md)

#### Discussion

This method encapsulates an autorelease pool and a call to [`processPendingChanges()`](./processpendingchanges%28%29.md).

## Parameters

- `block`: The closure to perform.

## See Also

### Performing block operations
- [func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () throws -> T) async rethrows -> T](./perform%28schedule,_%29.md)
  Submits a closure to the context’s queue for asynchronous execution.
- [func performAndWait(() -> Void)](./performandwait%28_%29-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [func performAndWait<T>(() throws -> T) rethrows -> T](./performandwait%28_%29-6aaf1.md)
  Submits a closure to the context’s queue for synchronous execution.
- [NSManagedObjectContext.ScheduledTaskType](./scheduledtasktype.md)
  The different types of scheduled tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/perform(_:))*