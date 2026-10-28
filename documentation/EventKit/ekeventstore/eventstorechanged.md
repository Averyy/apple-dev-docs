# EKEventStore.EventStoreChanged

**Framework**: EventKit  
**Kind**: struct  
**Role**: Structure

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

## Overview

Let observation = NotificationCenter.default.addObserver(of: eventStore, for: .changed) { message in … }

## Topics

### Initializers
- [init()](./eventstorechanged/init%28%29.md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/eventstorechanged)*