# Participant

**Framework**: Group Activities  
**Kind**: struct

An active participant in a group session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Participant
```

## Mentions

- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md)
- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)

#### Overview

Use a `Participant` object to differentiate among users in a session. A participant object doesn’t contain any sensitive data about the user, but provides a unique identifier to distinguish the user while the session is active.

You don’t create participant objects directly. The system creates a participant object for each user that joins an activity. Access the current set of participants from the [`activeParticipants`](groupsession/activeparticipants.md) property of the [`GroupSession`](groupsession.md) object associated with the activity.

## Topics

### Getting the unique identifier
- [let id: UUID](participant/id-swift.property.md)
  A globally unique identifier for the session participant.
### Comparing participants
- [static func != (Self, Self) -> Bool](participant/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Participant, Participant) -> Bool](participant/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](participant/hashvalue.md)
  The hash value.
- [var isNearbyWithLocalParticipant: Bool](participant/isnearbywithlocalparticipant.md)
  A Boolean value that indicates whether the participant is physically nearby with the local participant.
### Instance Methods
- [func hash(into: inout Hasher)](participant/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [Participant.ID](participant/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomStringConvertible Implementations](participant/customstringconvertible-implementations.md)
- [Equatable Implementations](participant/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Joining and managing a shared activity](joining-and-managing-a-shared-activity.md)
  Configure the session when a SharePlay activity starts, and handle events that occur during the lifetime of the activity.
- [Drawing content in a group session](drawing_content_in_a_group_session.md)
  Invite your friends to draw on a shared canvas while on a FaceTime call.
- [class GroupSession](groupsession.md)
  A session for an in-progress activity that synchronizes content among participant devices.
- [protocol CustomMessageIdentifiable](custommessageidentifiable.md)
  A type that assigns a custom ID string to messages you send to other devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/participant)*