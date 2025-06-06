# Group Activities

**Framework**: Groupactivities  
**Kind**: module

Create app-specific activities your users can share and experience together.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

#### Overview

With the Group Activities framework, you can provide your app’s content in SharePlay experiences, which create a sense of connection and immediacy for your users. For example, a video-streaming app might offer the ability to attend movie-watching parties in which participants watch simultaneously from their personal devices. The app handles the playback on each device, but the Group Activities framework synchronizes that playback and facilitates communication between the devices.

This framework leverages the FaceTime infrastructure to synchronize your app’s activities and to invite other participants to join those activities. When your app’s UI contains shareable activities, adopt the [`GroupActivity`](groupactivity.md) protocol in the objects you use to represent those activities. When a group activity begins, use the [`GroupSession`](groupsession.md) object to synchronize your app’s behavior with other participating devices.

> **Note**: The Group Activities framework uses end-to-end encryption on all session data that the [`GroupSession`](groupsession.md) object synchronizes between devices. Apple doesn’t have the keys to decrypt this data. Your use of the Group Activities framework doesn’t provide Apple with visibility into the content your app shares, or information related to playback of media content in your app, such as where in the content a user starts, pauses, or skips a session. Apple servers facilitating Group Activities sessions don’t know the identity of your app. Occasionally, Apple may ask a small number of users to help troubleshoot issues, such as by [`capturing a sysdiagnose or installing a debugging profile`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/), which may incidentally result in Apple collecting some information related to content shared in your app.

## Topics

### Essentials
- [com.apple.developer.group-session](../BundleResources/Entitlements/com.apple.developer.group-session.md)
  A Boolean value that indicates whether the app may implement shared group experiences.
### Activity definition
- [Defining your app’s SharePlay activities](defining-your-apps-shareplay-activities.md)
  Configure your app’s SharePlay support and define the activities that people can perform from your app.
- [Supporting Coordinated Media Playback](../AVFoundation/supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [protocol GroupActivity](groupactivity.md)
  A type that can advertise your app’s activities to other participants.
- [struct GroupActivityMetadata](groupactivitymetadata.md)
  Text and image content that describes an activity to potential participants.
- [enum GroupActivityActivationResult](groupactivityactivationresult.md)
  The result of preparing to start a custom activity.
- [struct GroupActivityTransferRepresentation](groupactivitytransferrepresentation.md)
  A type that lets you start a group activity from a known context.
### Interface presentation
- [Presenting SharePlay activities from your app’s UI](promoting-shareplay-activities-from-your-apps-ui.md)
  Make it easy for people to start activities from your app’s UI, from the system share sheet, or using AirPlay over AirDrop.
- [class GroupActivitySharingController](groupactivitysharingcontroller-4gtfk.md)
  A macOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.
- [class GroupActivitySharingController](groupactivitysharingcontroller-ybcy.md)
  An iOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.
### Session management
- [Joining and managing a shared activity](joining-and-managing-a-shared-activity.md)
  Configure the session when a SharePlay activity starts, and handle events that occur during the lifetime of the activity.
- [Drawing content in a group session](drawing_content_in_a_group_session.md)
  Invite your friends to draw on a shared canvas while on a FaceTime call.
- [class GroupSession](groupsession.md)
  A session for an in-progress activity that synchronizes content among participant devices.
- [protocol CustomMessageIdentifiable](custommessageidentifiable.md)
  A type that assigns a custom ID string to messages you send to other devices.
- [struct Participant](participant.md)
  An active participant in a group session.
### Spatial activities
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)
  Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [class SystemCoordinator](systemcoordinator.md)
  A type you use to coordinate your interface’s behavior when an active SharePlay session supports spatial placement of content.
- [SystemCoordinator.ParticipantState](systemcoordinator/participantstate.md)
  A structure that tells you whether a participant supports a shared simulation space for the current activity.
### Custom spatial templates
- [Building a guessing game for visionOS](building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
- [protocol SpatialTemplate](spatialtemplate.md)
  An interface you use to create custom arrangements of spatial Personas in a scene.
- [struct SpatialTemplateSeatElement](spatialtemplateseatelement.md)
  A spatial template element that represents a seat for a participant in the activity.
- [protocol SpatialTemplateElement](spatialtemplateelement.md)
  An interface that defines an element in your spatial template.
- [struct SpatialTemplateElementPosition](spatialtemplateelementposition.md)
  A type that defines the position of an element in a spatial template.
- [struct SpatialTemplateElementDirection](spatialtemplateelementdirection.md)
  The initial direction a participant faces when an activity starts.
- [protocol SpatialTemplateRole](spatialtemplaterole.md)
  An interface for defining roles that you assign to the participants of a group activity.
### File and data transfer
- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md)
  Send custom messages and data between devices to synchronize content for your activity, and incorporate messages your app receives from other participants.
- [class GroupSessionMessenger](groupsessionmessenger.md)
  An object that transfers app-specific data between the devices joined in a group session.
- [class GroupSessionJournal](groupsessionjournal.md)
  An object that manages file and data transfers between participants joined in a group session.
### System status
- [class GroupStateObserver](groupstateobserver.md)
  An object that contains information about the system’s ability to start SharePlay experiences.
### Structures
- [struct SpatialTemplatePreference](spatialtemplatepreference.md)
  A structure that specifies the preferred arrangement of participant spatial Personas in a shared simulation space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/GroupActivities)*