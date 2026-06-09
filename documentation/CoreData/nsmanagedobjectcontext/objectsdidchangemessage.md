# NSManagedObjectContext.ObjectsDidChangeMessage

**Framework**: Core Data  
**Kind**: struct

Posted when objects in a main queue context change (inserted, updated, deleted, refreshed, or invalidated).

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
struct ObjectsDidChangeMessage
```

#### Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](nsmanagedobjectcontext/objectsdidchangemessage/context.md)
- [var deleted: Set<NSManagedObject>](nsmanagedobjectcontext/objectsdidchangemessage/deleted.md)
  Objects that were deleted.
- [var inserted: Set<NSManagedObject>](nsmanagedobjectcontext/objectsdidchangemessage/inserted.md)
  Objects that were inserted.
- [var invalidated: Set<NSManagedObject>](nsmanagedobjectcontext/objectsdidchangemessage/invalidated.md)
  Objects that were invalidated.
- [let invalidatedAll: Bool?](nsmanagedobjectcontext/objectsdidchangemessage/invalidatedall.md)
  True if all objects in the context were invalidated.
- [var refreshed: Set<NSManagedObject>](nsmanagedobjectcontext/objectsdidchangemessage/refreshed.md)
  Objects that were refreshed.
- [var updated: Set<NSManagedObject>](nsmanagedobjectcontext/objectsdidchangemessage/updated.md)
  Objects that were updated.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/objectsdidchangemessage)*