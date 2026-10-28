# GroupSession.Sessions

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence of sessions you use to manage a specific activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Sessions
```

Available when `ActivityType` conforms to `GroupActivity`.

## Overview

When a participant engages one of your app’s activities, a `Sessions` structure provides the session you use to handle synchronization. Iterate over the contents of this structure asynchronously to retrieve each new session the system delivers to your app. The system delivers only one [`GroupSession`](../groupsession.md) for each activity. To monitor changes to that session, configure subscribers to its published properties.

Don’t create this structure directly. Instead, use the [`sessions()`](../groupactivity/sessions%28%29.md) method to retrieve the sessions.

## Topics

### Creating an iterator
- [GroupSession.Sessions.Iterator](./sessions/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/sessions)*