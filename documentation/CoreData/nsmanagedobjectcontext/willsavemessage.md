# NSManagedObjectContext.WillSaveMessage

**Framework**: Core Data  
**Kind**: struct

Posted before a main queue context saves.

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
struct WillSaveMessage
```

#### Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Topics

### Instance Properties
- [let context: NSManagedObjectContext](nsmanagedobjectcontext/willsavemessage/context.md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/willsavemessage)*