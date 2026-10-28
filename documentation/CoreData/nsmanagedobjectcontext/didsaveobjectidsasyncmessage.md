# NSManagedObjectContext.DidSaveObjectIDsAsyncMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted after a private queue context saves, containing object IDs rather than full objects.

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
struct DidSaveObjectIDsAsyncMessage
```

## Overview

Only use this message type for contexts with `NSPrivateQueueConcurrencyType`. For main queue contexts, use [`NSManagedObjectContext.DidSaveObjectIDsMessage`](./didsaveobjectidsmessage.md).

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](./didsaveobjectidsasyncmessage/context.md)
- [let deletedIDs: Set<NSManagedObjectID>](./didsaveobjectidsasyncmessage/deletedids.md)
  Object IDs of objects that were deleted during this save.
- [let historyToken: NSPersistentHistoryToken?](./didsaveobjectidsasyncmessage/historytoken.md)
  The persistent history token representing the state after the save.
- [let insertedIDs: Set<NSManagedObjectID>](./didsaveobjectidsasyncmessage/insertedids.md)
  Object IDs of objects that were inserted during this save.
- [let invalidatedIDs: Set<NSManagedObjectID>](./didsaveobjectidsasyncmessage/invalidatedids.md)
  Object IDs of objects that were invalidated during this save.
- [let queryGeneration: NSQueryGenerationToken?](./didsaveobjectidsasyncmessage/querygeneration.md)
  Query generation token after the save.
- [let refreshedIDs: Set<NSManagedObjectID>](./didsaveobjectidsasyncmessage/refreshedids.md)
  Object IDs of objects that were refreshed during this save.
- [let updatedIDs: Set<NSManagedObjectID>](./didsaveobjectidsasyncmessage/updatedids.md)
  Object IDs of objects that were updated during this save.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../../Foundation/notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsasyncmessage)*