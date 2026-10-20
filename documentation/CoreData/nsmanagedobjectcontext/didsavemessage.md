# NSManagedObjectContext.DidSaveMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted after a main queue context saves.

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
struct DidSaveMessage
```

#### Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](./didsavemessage/context.md)
- [var deleted: Set<NSManagedObject>](./didsavemessage/deleted.md)
  Managed objects that were deleted during this save.
- [let historyToken: NSPersistentHistoryToken?](./didsavemessage/historytoken.md)
- [var inserted: Set<NSManagedObject>](./didsavemessage/inserted.md)
  Managed objects that were inserted during this save.
- [let queryGeneration: NSQueryGenerationToken?](./didsavemessage/querygeneration.md)
  Query generation token after the save.
- [var updated: Set<NSManagedObject>](./didsavemessage/updated.md)
  Managed objects that were updated during this save.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didsavemessage)*