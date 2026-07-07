# NSManagedObjectContext.DidSaveObjectIDsMessage

**Framework**: Core Data  
**Kind**: struct

Posted after a main queue context saves, containing object IDs rather than full objects.

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
struct DidSaveObjectIDsMessage
```

#### Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](nsmanagedobjectcontext/didsaveobjectidsmessage/context.md)
- [let deletedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didsaveobjectidsmessage/deletedids.md)
  Object IDs of objects that were deleted during this save.
- [let historyToken: NSPersistentHistoryToken?](nsmanagedobjectcontext/didsaveobjectidsmessage/historytoken.md)
  The persistent history token representing the state after the save.
- [let insertedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didsaveobjectidsmessage/insertedids.md)
  Object IDs of objects that were inserted during this save.
- [let invalidatedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didsaveobjectidsmessage/invalidatedids.md)
  Object IDs of objects that were invalidated during this save.
- [let queryGeneration: NSQueryGenerationToken?](nsmanagedobjectcontext/didsaveobjectidsmessage/querygeneration.md)
  Query generation token after the save.
- [let refreshedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didsaveobjectidsmessage/refreshedids.md)
  Object IDs of objects that were refreshed during this save.
- [let updatedIDs: Set<NSManagedObjectID>](nsmanagedobjectcontext/didsaveobjectidsmessage/updatedids.md)
  Object IDs of objects that were updated during this save.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsmessage)*