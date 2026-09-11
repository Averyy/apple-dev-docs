# NSManagedObjectContext.WillSaveMessage

**Framework**: Core Data  
**Kind**: struct

Posted before a main queue context saves.

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
struct WillSaveMessage
```

#### Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](nsmanagedobjectcontext/willsavemessage/context.md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/willsavemessage)*