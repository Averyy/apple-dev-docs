# NSManagedObjectContext.ScheduledTaskType.enqueued

**Framework**: Core Data  
**Kind**: case

The enqueued scheduled task type.

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
case enqueued
```

#### Discussion

Enqueued tasks execute asynchronously on the context’s queue. An enqueued task encapsulates an autorelease pool and a call to [`processPendingChanges()`](nsmanagedobjectcontext/processpendingchanges().md), and its behavior is analogous to [`perform(_:)`](nsmanagedobjectcontext/perform(_:).md). The context’s queue executes tasks in the order you add them.

## See Also

- [NSManagedObjectContext.ScheduledTaskType.immediate](nsmanagedobjectcontext/scheduledtasktype/immediate.md)
  The immediate scheduled task type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype/enqueued)*