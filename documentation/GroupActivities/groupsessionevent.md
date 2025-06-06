# GroupSessionEvent

**Framework**: Group Activities  
**Kind**: struct

A session-related event that appears in the system UI.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct GroupSessionEvent
```

#### Overview

Use this structure to specify the contents of custom activity-related events. The AV Foundation framework posts media-related events to the system on your app’s behalf; create an instance of this structure if your app posts additional events that don’t route through AV Foundation.

After creating an instance of this structure, post it to the system using the [`showNotice(_:)`](groupsession/shownotice(_:).md) method of [`GroupSession`](groupsession.md).

## Topics

### Creating a group session event
- [init(originator: Participant, action: GroupSessionEvent.Action, url: URL?)](groupsessionevent/init(originator:action:url:).md)
  Creates a new event with the specified participant and action details.
### Getting the event details
- [let originator: Participant](groupsessionevent/originator.md)
  The participant that initiated the event.
- [let url: URL?](groupsessionevent/url.md)
  The URL to open when the participant taps the event link in the system UI.
- [let action: GroupSessionEvent.Action](groupsessionevent/action-swift.property.md)
  The reason for the event.
- [GroupSessionEvent.Action](groupsessionevent/action-swift.struct.md)
  A playback-related change that occurs during the session.

## See Also

- [func showNotice(GroupSessionEvent)](groupsession/shownotice(_:).md)
  Posts an event to the system, which displays the information in the system UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent)*