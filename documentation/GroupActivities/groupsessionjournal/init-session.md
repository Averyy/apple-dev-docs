# init(session:)

**Framework**: Group Activities  
**Kind**: init

Creates a journal and associates it with the specified session of a group activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init<Activity>(session: GroupSession<Activity>) where Activity : GroupActivity
```

#### Return Value

A [`GroupSessionJournal`](groupsessionjournal.md) object configured for the specified session.

## Parameters

- `session`: The session you use for communicating with participants.   The session must be in the   or    state when you create the   journal, and the session must be in the    state before you can send or receive attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionjournal/init(session:))*