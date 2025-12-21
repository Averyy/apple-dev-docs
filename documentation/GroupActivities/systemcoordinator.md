# SystemCoordinator

**Framework**: Group Activities  
**Kind**: class

A type you use to coordinate your interface’s behavior when an active SharePlay session supports spatial placement of content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final class SystemCoordinator
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Overview

A [`SystemCoordinator`](systemcoordinator.md) object helps you coordinate the presentation of your app’s content when spatial placement is active. In visionOS, the system can present a SharePlay activity as if the participants were together in the same room with the content. Each participant views the content from a particular vantage point, and sees the changes that others make. The system handles the placement of each participant’s spatial Persona relative to the content, but you handle any changes to the content itself with the help of the [`SystemCoordinator`](systemcoordinator.md) object.

You don’t create a [`SystemCoordinator`](systemcoordinator.md) object directly. After you receive a [`GroupSession`](groupsession.md) object for an activity, retrieve the system coordinator from the session’s [`systemCoordinator`](GroupSession/systemCoordinator.md) property. When you first retrieve the object, update its [`configuration`](systemcoordinator/configuration-swift.property.md) property to tell the system how you want to arrange participants in the scene. After that, use the information in the system coordinator’s properties to keep your app’s interface up to date. When participants support spatial placement, send additional data to synchronize your content for those participants. For example, when one person scrolls the contents of a window, update the scroll position in the window of other spatially aware participants to preserve the shared context for everyone.

You choose what information to share among participants, and you choose how to manage the corresponding updates. A system coordinator object only helps you know when to make those changes. Observe the object’s published properties to receive automatic updates when the values change.

## Topics

### Configuring the system coordinator
- [var configuration: SystemCoordinator.Configuration](systemcoordinator/configuration-swift.property.md)
  The current configuration of the system coordinator.
- [SystemCoordinator.Configuration](systemcoordinator/configuration-swift.struct.md)
  A structure that specifies your app’s support for activities that take place in a shared simulation space.
### Getting the participant state
- [var remoteParticipantStates: [Participant : SystemCoordinator.ParticipantState]](systemcoordinator/remoteparticipantstates.md)
- [var localParticipantState: SystemCoordinator.ParticipantState](systemcoordinator/localparticipantstate.md)
  The current participant’s level of support for an activity that takes place in a shared simulation space.
- [var localParticipantStates: SystemCoordinator.ParticipantStates](systemcoordinator/localparticipantstates.md)
  An asynchronous sequence that reports changes to the local participant’s state.
- [SystemCoordinator.ParticipantStates](systemcoordinator/participantstates.md)
  An asynchronous sequence that reports the current person’s ability to participate in a shared context.
### Getting the current immersion level
- [var groupImmersionStyle: SystemCoordinator.GroupImmersionStyles](systemcoordinator/groupimmersionstyle.md)
  The presentation style to apply to an immersive space for the current activity.
- [SystemCoordinator.GroupImmersionStyles](systemcoordinator/groupimmersionstyles.md)
  An asynchronous sequence that contains one or more incoming immersion styles for you to process.
### Assigning the local participant role
- [func assignRole(some SpatialTemplateRole)](systemcoordinator/assignrole(_:).md)
  Assigns the given spatial template role to the local participant.
- [func resignRole()](systemcoordinator/resignrole.md)
  Resigns the local participant from their current spatial template role.
### Structures
- [SystemCoordinator.ParticipantState](systemcoordinator/participantstate.md)
  A structure that tells you whether a participant supports a shared simulation space for the current activity.

## Relationships

### Conforms To
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)
  Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)
  Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [SystemCoordinator.ParticipantState](systemcoordinator/participantstate.md)
  A structure that tells you whether a participant supports a shared simulation space for the current activity.
- [func groupActivityAssociation(GroupActivityAssociationKind?) -> some View](../SwiftUI/View/groupActivityAssociation(_:).md)
  Specifies how a view should be associated with the current SharePlay group activity.
- [class GroupActivityAssociationInteraction](groupactivityassociationinteraction.md)
  An interaction configures a view’s association with the current SharePlay group activity.
- [struct GroupActivityAssociationKind](groupactivityassociationkind.md)
  An association a user-interface element can have with a SharePlay group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator)*