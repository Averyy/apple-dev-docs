# GroupSession

**Framework**: Group Activities  
**Kind**: class

A session for an in-progress activity that synchronizes content among participant devices.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final class GroupSession<ActivityType> where ActivityType : GroupActivity
```

## Mentions

- [Joining and managing a shared activity](joining-and-managing-a-shared-activity.md)
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)
- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md)

#### Overview

A `GroupSession` object contains details about the user’s currently selected activity, its status, and its participants. When a participant engages in an activity, the system binds a session to that activity for you. You use the session object to synchronize your app’s activity-related content, including your app’s UI.

You don’t create `GroupSession` objects directly. Instead, the system creates sessions and makes them available to your app asynchronously. Use the `AsyncSequence` type returned by the [`sessions()`](groupactivity/sessions().md) method of your activity to retrieve new sessions when they become available.

Before the system can create a session object, your app must create a `GroupActivity` object and activate it. For information about how to configure group activities, see [`GroupActivity`](groupactivity.md).

##### Start and Stop the Session

When you receive a new session object, it’s initially in the [`GroupSession.State.waiting`](groupsession/state-swift.enum/waiting.md) state. As soon as your app is ready to begin the associated activity, call the session’s [`join()`](groupsession/join().md) method. Joining a session validates the connection and starts the synchronization process between the current device and other participants’ devices. If your app successfully joins the session, the session transitions to the [`GroupSession.State.joined`](groupsession/state-swift.enum/joined.md) state.

When the user quits your app, or navigates away from the shared activity, call the session’s [`leave()`](groupsession/leave().md) method. Leaving a session gracefully transitions it to the [`GroupSession.State.invalidated(reason:)`](groupsession/state-swift.enum/invalidated(reason:).md) state, and informs the system that the user isn’t currently engaged in the activity.

## Topics

### Getting the current session
- [GroupSession.Sessions](groupsession/sessions.md)
  An asynchronous sequence of sessions you use to manage a specific activity.
### Joining and leaving the session
- [func join()](groupsession/join.md)
  Starts the shared activity on the current device.
- [func leave()](groupsession/leave.md)
  Leaves the current activity and stops receiving synchronized data.
- [func end()](groupsession/end.md)
  Ends the activity for the entire group and stops the transfer of synchronized data.
### Accessing the shared activity
- [var activity: ActivityType](groupsession/activity.md)
  The current activity associated with the session.
### Getting the session details
- [var state: GroupSession<ActivityType>.State](groupsession/state-swift.property.md)
  The current state of the session.
- [GroupSession.State](groupsession/state-swift.enum.md)
  The possible states of a session.
- [let id: UUID](groupsession/id.md)
  The unique identifier of the current session.
- [var description: String](groupsession/description.md)
  A textual representation of this instance.
### Getting the participants
- [var localParticipant: Participant](groupsession/localparticipant.md)
  The participant on the current device.
- [var activeParticipants: Set<Participant>](groupsession/activeparticipants.md)
  The set of participants currently engaged in the activity.
### Getting the scene-association identifier
- [var sceneSessionIdentifier: String?](groupsession/scenesessionidentifier.md)
  The persistent identifier of the session’s associated scene.
### Getting the participant’s attention
- [func requestForegroundPresentation()](groupsession/requestforegroundpresentation.md)
  Tells the system that your app needs to be in the foreground to continue an activity.
### Notifying participants of playback changes
- [func showNotice(GroupSessionEvent)](groupsession/shownotice(_:).md)
  Posts an event to the system, which displays the information in the system UI.
- [struct GroupSessionEvent](groupsessionevent.md)
  A session-related event that appears in the system UI.
### Publishing changes
- [var objectWillChange: ObservableObjectPublisher](groupsession/objectwillchange.md)
### Structures
- [GroupSession.Event](groupsession/event.md)
  A session-related event to display in the system UI.
### Instance Properties
- [var $activeParticipants: Published<Set<Participant>>.Publisher](groupsession/$activeparticipants.md)
- [var $activity: Published<ActivityType>.Publisher](groupsession/$activity.md)
- [var $state: Published<GroupSession<ActivityType>.State>.Publisher](groupsession/$state.md)
- [let isLocallyInitiated: Bool](groupsession/islocallyinitiated.md)
  A Boolean value that is true if the current session was created by the local participant.
- [var systemCoordinator: SystemCoordinator?](groupsession/systemcoordinator.md)
  The system coordinator associated with an active session.
### Instance Methods
- [func postEvent(GroupSession<ActivityType>.Event)](groupsession/postevent(_:).md)
  Posts an event to the system, which displays the information in the system UI.
### Type Aliases
- [GroupSession.ObjectWillChangePublisher](groupsession/objectwillchangepublisher.md)
  The type of publisher that emits before the object has changed.
### Default Implementations
- [CustomStringConvertible Implementations](groupsession/customstringconvertible-implementations.md)
- [ObservableObject Implementations](groupsession/observableobject-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [ObservableObject](../Combine/ObservableObject.md)

## See Also

- [Joining and managing a shared activity](joining-and-managing-a-shared-activity.md)
  Configure the session when a SharePlay activity starts, and handle events that occur during the lifetime of the activity.
- [Drawing content in a group session](drawing_content_in_a_group_session.md)
  Invite your friends to draw on a shared canvas while on a FaceTime call.
- [protocol CustomMessageIdentifiable](custommessageidentifiable.md)
  A type that assigns a custom ID string to messages you send to other devices.
- [struct Participant](participant.md)
  An active participant in a group session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession)*