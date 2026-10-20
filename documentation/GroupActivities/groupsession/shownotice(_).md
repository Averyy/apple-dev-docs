# showNotice(_:)

**Framework**: Group Activities  
**Kind**: method

Posts an event to the system, which displays the information in the system UI.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final func showNotice(_ event: GroupSessionEvent)
```

#### Discussion

Call this method to update the system’s UI with information about session-related events. For example, a music-listening app might post an event to notify the group that a participant stopped playback. The system displays the event information only on the current device, and doesn’t forward events to other devices.

## Parameters

- `event`: The event to display in the system UI.

## See Also

- [struct GroupSessionEvent](groupsessionevent.md)
  A session-related event that appears in the system UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/shownotice(_:))*