# NSManagedObjectContext.ScheduledTaskType.immediate

**Framework**: Core Data  
**Kind**: case

The immediate scheduled task type.

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
case immediate
```

#### Discussion

Immediate tasks execute right away if the context operates within the current scope; otherwise, the context enqueues the task. Tasks of this type are reentrant, nonblocking, and continuation-aware.

## See Also

- [NSManagedObjectContext.ScheduledTaskType.enqueued](nsmanagedobjectcontext/scheduledtasktype/enqueued.md)
  The enqueued scheduled task type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype/immediate)*