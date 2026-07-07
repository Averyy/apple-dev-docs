# NSManagedObjectContext.DidMergeChangesMessage

**Framework**: Core Data  
**Kind**: struct

Posted after a main queue context merges changes from another context, containing object IDs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct DidMergeChangesMessage
```

#### Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`. For private queue contexts, use [`NSManagedObjectContext.DidMergeChangesAsyncMessage`](nsmanagedobjectcontext/didmergechangesasyncmessage.md).

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](nsmanagedobjectcontext/didmergechangesmessage/context.md)
- [let deletedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesmessage/deletedids.md)
  Object IDs of objects that were deleted during the merge.
- [let historyToken: NSPersistentHistoryToken?](nsmanagedobjectcontext/didmergechangesmessage/historytoken.md)
  The persistent history token representing the state after the merge.
- [let insertedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesmessage/insertedids.md)
  Object IDs of objects that were inserted during the merge.
- [let invalidatedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesmessage/invalidatedids.md)
  Object IDs of objects that were invalidated during the merge.
- [let queryGeneration: NSQueryGenerationToken?](nsmanagedobjectcontext/didmergechangesmessage/querygeneration.md)
  Query generation token after the merge.
- [let refreshedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesmessage/refreshedids.md)
  Object IDs of objects that were refreshed during the merge.
- [let updatedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didmergechangesmessage/updatedids.md)
  Object IDs of objects that were updated during the merge.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didmergechangesmessage)*