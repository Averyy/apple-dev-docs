# Shared with You Core

**Framework**: SharedWithYouCore  
**Kind**: module  
**Role**: Framework

Integrate custom collaboration with Messages, Mail, and FaceTime.

#### Overview

The Shared with You Core framework provides classes to collaborate and share documents directly with the Messages, Mail, and FaceTime apps. Use the classes in this framework to share content, create configurable collaboration settings, and manage participants.

The framework provides a customizable popover to your app to manage details of the collaboration and connect to conversations. The UI incorporates technologies you already use, like share sheet and drag and drop. An indicator in the share sheet header identifies a collaboration.

Use the [`SWCollaborationCoordinator`](./swcollaborationcoordinator.md) to manage collaboration activities in your app. The [`SWCollaborationMetadata`](./swcollaborationmetadata.md) objects contain the collaboration metadata with essential information like, identifiers, titles, and share option configuration that update the UI. To customize collaboration settings, use the [`SWCollaborationOption`](./swcollaborationoption.md), [`SWCollaborationOptionsGroup`](./swcollaborationoptionsgroup.md), and [`SWCollaborationShareOptions`](./swcollaborationshareoptions.md) classes. These options appear in Messages, Mail, and FaceTime, providing people with the opportunity to make choices about permissions, access levels, and other collaboration parameters.

For more information on integrating with Messages, Mail, and FaceTime, see [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md).

> **Note**: Shared with You Core is a [Shared with You](../SharedWithYou/SharedWithYou.md) framework.

## Topics

### Coordinate collaborations
- [class SWCollaborationCoordinator](./swcollaborationcoordinator.md)
  An object that contains the shared collaboration coordinator.
### Handle collaboration actions
- [class SWAction](./swaction.md)
  An object that represents a collaboration action.
- [protocol SWCollaborationActionHandler](./swcollaborationactionhandler.md)
  A delegate to handle incoming collaboration actions from a collaboration coordinator.
- [class SWStartCollaborationAction](./swstartcollaborationaction.md)
  An object that represents the first action sent to an app when the user shares a collaboration.
- [class SWUpdateCollaborationParticipantsAction](./swupdatecollaborationparticipantsaction.md)
  An action that contains the cryptographic identities the system uses to add to or remove from an existing collaboration.
### Register the collaboration metadata
- [class SWCollaborationMetadata](./swcollaborationmetadata.md)
  A model object for conveying data during a collaboration.
### Manage options in a collaboration
- [class SWCollaborationOption](./swcollaborationoption.md)
  An object that determines how the system shares a document in a collaboration.
- [class SWCollaborationOptionsGroup](./swcollaborationoptionsgroup.md)
  An object that represents a group of collaboration options that the system displays together.
- [class SWCollaborationOptionsPickerGroup](./swcollaborationoptionspickergroup.md)
  An object that represents a group of collaboration options that the system displays together with mutually exclusive options.
- [class SWCollaborationShareOptions](./swcollaborationshareoptions.md)
  An object that represents the state of the collaboration options for the document.
- [struct SWLocalCollaborationIdentifier](./swlocalcollaborationidentifier.md)
  A local identifier for a collaboration.
- [let UTCollaborationOptionsTypeIdentifier: String](./utcollaborationoptionstypeidentifier.md)
  A string constant for the options type identifier.
### Manage collaboration participants
- [class SWPerson](./swperson.md)
  An object that tracks participants in a collaboration.
- [struct SWCollaborationIdentifier](./swcollaborationidentifier.md)
  A unique identifier for a collaboration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore)*