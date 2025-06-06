# GroupActivity.Sessions

**Framework**: Group Activities  
**Kind**: typealias

A type that provides asynchronous, sequential, iterated access to the sessions for the activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
typealias Sessions = GroupSession<Self>.Sessions
```

#### Discussion

A `Sessions` type contains a sequence of [`GroupSession`](groupsession.md) objects specific to the current activity. The [`sessions()`](groupactivity/sessions().md) method returns this type, and you use it to retrieve the current session, if any, for that activity. The system creates only one [`GroupSession`](groupsession.md) object for each new activity. To detect changes to the session’s state, activity type, or active participants, subscribe to the corresponding properties.

## See Also

- [static func sessions() -> Self.Sessions](groupactivity/sessions.md)
  Returns the sessions for this activity as an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivity/sessions)*