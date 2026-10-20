# NSManagedObjectContext.ObjectsDidChangeMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted when objects in a main queue context change (inserted, updated, deleted, refreshed, or invalidated).

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
struct ObjectsDidChangeMessage
```

#### Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](./objectsdidchangemessage/context.md)
- [var deleted: Set<NSManagedObject>](./objectsdidchangemessage/deleted.md)
  Objects that were deleted.
- [var inserted: Set<NSManagedObject>](./objectsdidchangemessage/inserted.md)
  Objects that were inserted.
- [var invalidated: Set<NSManagedObject>](./objectsdidchangemessage/invalidated.md)
  Objects that were invalidated.
- [let invalidatedAll: Bool?](./objectsdidchangemessage/invalidatedall.md)
  True if all objects in the context were invalidated.
- [var refreshed: Set<NSManagedObject>](./objectsdidchangemessage/refreshed.md)
  Objects that were refreshed.
- [var updated: Set<NSManagedObject>](./objectsdidchangemessage/updated.md)
  Objects that were updated.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/objectsdidchangemessage)*