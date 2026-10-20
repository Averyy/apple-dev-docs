# GroupSessionEvent.Action

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

A playback-related change that occurs during the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Action
```

#### Overview

Use this structure to communicate playback-related changes to participants using the system UI. You can use this structure to communicate the following types of events:

- Transport-related events for a custom player.
- Changes to a playback queue your app manages.

When a change occurs in your custom player or playback queue, create an instance of this structure to describe the change and wrap it in a [`GroupSessionEvent`](../groupsessionevent.md) structure. To display the event to the participant call the [`showNotice(_:)`](../groupsession/shownotice%28_%29.md) method of the session. The system formats and displays the information you provide.

> **Note**: If your app uses AV Foundation to play content, you don’t need to communicate transport-related events yourself. AV Foundation generates appropriate events when the user plays, pauses, seeks, or skips tracks.

## Topics

### Getting playback-related actions
- [static let play: GroupSessionEvent.Action](./action-swift.struct/play.md)
  An action that indicates the start of playback.
- [static let pause: GroupSessionEvent.Action](./action-swift.struct/pause.md)
  An action that indicates an end to playback.
- [static let seek: GroupSessionEvent.Action](./action-swift.struct/seek.md)
  An event that indicates a change to the current playback location.
- [static func skip(item: String) -> GroupSessionEvent.Action](./action-swift.struct/skip%28item%29.md)
  Returns an event that indicates a skipped track or playback item.
### Getting change-related actions
- [static func updatedQueue(GroupSessionEvent.Action.QueueChange) -> GroupSessionEvent.Action](./action-swift.struct/updatedqueue%28_%29.md)
  Returns an action that represents a change to the playback queue.
- [static let updatedQueue: GroupSessionEvent.Action](./action-swift.struct/updatedqueue.md)
  An action that represents a nonspecific change to the queue.
- [GroupSessionEvent.Action.QueueChange](./action-swift.struct/queuechange.md)
  A type that describes a modification to the playback queue.

## See Also

### Getting the event details
- [let originator: Participant](./originator.md)
  The participant that initiated the event.
- [let url: URL?](./url.md)
  The URL to open when the participant taps the event link in the system UI.
- [let action: GroupSessionEvent.Action](./action-swift.property.md)
  The reason for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct)*