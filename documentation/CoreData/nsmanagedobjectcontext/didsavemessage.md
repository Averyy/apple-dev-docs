# NSManagedObjectContext.DidSaveMessage

**Framework**: Core Data  
**Kind**: struct

Posted after a main queue context saves.

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
struct DidSaveMessage
```

#### Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](nsmanagedobjectcontext/didsavemessage/context.md)
- [var deleted: Set<NSManagedObject>](nsmanagedobjectcontext/didsavemessage/deleted.md)
  Managed objects that were deleted during this save.
- [let historyToken: NSPersistentHistoryToken?](nsmanagedobjectcontext/didsavemessage/historytoken.md)
- [var inserted: Set<NSManagedObject>](nsmanagedobjectcontext/didsavemessage/inserted.md)
  Managed objects that were inserted during this save.
- [let queryGeneration: NSQueryGenerationToken?](nsmanagedobjectcontext/didsavemessage/querygeneration.md)
  Query generation token after the save.
- [var updated: Set<NSManagedObject>](nsmanagedobjectcontext/didsavemessage/updated.md)
  Managed objects that were updated during this save.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didsavemessage)*