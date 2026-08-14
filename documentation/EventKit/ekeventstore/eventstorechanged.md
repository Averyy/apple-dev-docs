# EKEventStore.EventStoreChanged

**Framework**: EventKit  
**Kind**: struct

A notification posted when changes are made to the Calendar or Reminders database.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct EventStoreChanged
```

#### Overview

Let observation = NotificationCenter.default.addObserver(of: eventStore, for: .changed) { message in … }

## Topics

### Initializers
- [init()](ekeventstore/eventstorechanged/init.md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/eventstorechanged)*