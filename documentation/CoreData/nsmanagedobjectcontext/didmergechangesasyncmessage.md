# NSManagedObjectContext.DidMergeChangesAsyncMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted after a private queue context merges changes from another context, containing object IDs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct DidMergeChangesAsyncMessage
```

## Overview

Only use this message type for contexts with `NSPrivateQueueConcurrencyType`. For main queue contexts, use [`NSManagedObjectContext.DidMergeChangesMessage`](./didmergechangesmessage.md).

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](./didmergechangesasyncmessage/context.md)
- [let deletedIDs: Set<NSManagedObjectID>](./didmergechangesasyncmessage/deletedids.md)
  Object IDs of objects that were deleted during the merge.
- [let historyToken: NSPersistentHistoryToken?](./didmergechangesasyncmessage/historytoken.md)
  The persistent history token representing the state after the merge.
- [let insertedIDs: Set<NSManagedObjectID>](./didmergechangesasyncmessage/insertedids.md)
  Object IDs of objects that were inserted during the merge.
- [let invalidatedIDs: Set<NSManagedObjectID>](./didmergechangesasyncmessage/invalidatedids.md)
  Object IDs of objects that were invalidated during the merge.
- [let queryGeneration: NSQueryGenerationToken?](./didmergechangesasyncmessage/querygeneration.md)
  Query generation token after the merge.
- [let refreshedIDs: Set<NSManagedObjectID>](./didmergechangesasyncmessage/refreshedids.md)
  Object IDs of objects that were refreshed during the merge.
- [let updatedIDs: Set<NSManagedObjectID>](./didmergechangesasyncmessage/updatedids.md)
  Object IDs of objects that were updated during the merge.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../../Foundation/notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didmergechangesasyncmessage)*