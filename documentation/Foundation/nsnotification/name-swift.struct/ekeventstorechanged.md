# EKEventStoreChanged

**Framework**: Foundation  
**Kind**: property

A notification posted when changes are made to the Calendar database.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let EKEventStoreChanged: NSNotification.Name
```

#### Discussion

This notification is posted whenever changes are made to the Calendar database, including adding, removing, and changing events or reminders. Individual changes are not described. When you receive this notification, you should refetch all [`EKEvent`](https://developer.apple.com/documentation/eventkit/ekevent) and [`EKReminder`](https://developer.apple.com/documentation/eventkit/ekreminder) objects you have accessed, as they are considered stale.

If you are actively editing an event and do not wish to refetch it unless it is absolutely necessary to do so, you can call the refresh method on it. If the method returns `true`, you do not need to refetch the event.

> **Note**:   The system posts this notification on the main actor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ekeventstorechanged)*