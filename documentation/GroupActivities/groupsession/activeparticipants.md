# activeParticipants

**Framework**: Group Activities  
**Kind**: property  
**Role**: Instance Property

The set of participants currently engaged in the activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@Published
<Set<Participant>> final var activeParticipants: Set<Participant> { get }
```

## Mentions

- [Configure your visionOS app for sharing with people nearby](../configure-your-app-for-sharing-with-people-nearby.md)
- [Joining and managing a shared activity](../joining-and-managing-a-shared-activity.md)

## Discussion

This property reflects the set of people invited to a group session and currently engaged in the shared activity on their device. Members who join the conversation over FaceTime but don’t join the shared activity aren’t active participants. As people join or leave the activity, the session object updates the set of active participants. To detect changes to this property, configure a subscriber.

Each [`Participant`](../participant.md) object corresponds to a joined session on a device. If a single person joins the activity from two devices simultaneously, the set contains a separate [`Participant`](../participant.md) object for each device.

## See Also

### Getting the participants
- [var localParticipant: Participant](./localparticipant.md)
  The participant on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/activeparticipants)*