# NSManagedObjectContext.DidMergeChangesMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted after a main queue context merges changes from another context, containing object IDs.

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
struct DidMergeChangesMessage
```

## Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`. For private queue contexts, use [`NSManagedObjectContext.DidMergeChangesAsyncMessage`](./didmergechangesasyncmessage.md).

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](./didmergechangesmessage/context.md)
- [let deletedIDs: Set<NSManagedObjectID>](./didmergechangesmessage/deletedids.md)
  Object IDs of objects that were deleted during the merge.
- [let historyToken: NSPersistentHistoryToken?](./didmergechangesmessage/historytoken.md)
  The persistent history token representing the state after the merge.
- [let insertedIDs: Set<NSManagedObjectID>](./didmergechangesmessage/insertedids.md)
  Object IDs of objects that were inserted during the merge.
- [let invalidatedIDs: Set<NSManagedObjectID>](./didmergechangesmessage/invalidatedids.md)
  Object IDs of objects that were invalidated during the merge.
- [let queryGeneration: NSQueryGenerationToken?](./didmergechangesmessage/querygeneration.md)
  Query generation token after the merge.
- [let refreshedIDs: Set<NSManagedObjectID>](./didmergechangesmessage/refreshedids.md)
  Object IDs of objects that were refreshed during the merge.
- [let updatedIDs: Set<NSManagedObjectID>](./didmergechangesmessage/updatedids.md)
  Object IDs of objects that were updated during the merge.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didmergechangesmessage)*