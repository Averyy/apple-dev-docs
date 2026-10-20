# action

**Framework**: Group Activities  
**Kind**: property  
**Role**: Instance Property

The reason for the event.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
let action: GroupSessionEvent.Action
```

#### Discussion

The system uses this information to craft a message in the system UI.

## See Also

### Getting the event details
- [let originator: Participant](./originator.md)
  The participant that initiated the event.
- [let url: URL?](./url.md)
  The URL to open when the participant taps the event link in the system UI.
- [GroupSessionEvent.Action](./action-swift.struct.md)
  A playback-related change that occurs during the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.property)*