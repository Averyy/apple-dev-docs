# NSManagedObjectContext.DidMergeChangesAsyncMessage

**Framework**: Core Data  
**Kind**: struct

Posted after a private queue context merges changes from another context, containing object IDs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct DidMergeChangesAsyncMessage
```

#### Overview

Only use this message type for contexts with `NSPrivateQueueConcurrencyType`. For main queue contexts, use [`NSManagedObjectContext.DidMergeChangesMessage`](nsmanagedobjectcontext/didmergechangesmessage.md).

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](nsmanagedobjectcontext/didmergechangesasyncmessage/context.md)
- [let deletedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesasyncmessage/deletedids.md)
  Object IDs of objects that were deleted during the merge.
- [let historyToken: NSPersistentHistoryToken?](nsmanagedobjectcontext/didmergechangesasyncmessage/historytoken.md)
  The persistent history token representing the state after the merge.
- [let insertedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesasyncmessage/insertedids.md)
  Object IDs of objects that were inserted during the merge.
- [let invalidatedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesasyncmessage/invalidatedids.md)
  Object IDs of objects that were invalidated during the merge.
- [let queryGeneration: NSQueryGenerationToken?](nsmanagedobjectcontext/didmergechangesasyncmessage/querygeneration.md)
  Query generation token after the merge.
- [let refreshedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesasyncmessage/refreshedids.md)
  Object IDs of objects that were refreshed during the merge.
- [let updatedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesasyncmessage/updatedids.md)
  Object IDs of objects that were updated during the merge.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../Foundation/NotificationCenter/AsyncMessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didmergechangesasyncmessage)*