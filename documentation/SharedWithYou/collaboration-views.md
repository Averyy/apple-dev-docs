# Collaboration views

**Framework**: Shared with You  
**Role**: API Collection

Create and customize a collaboration view to manage the shared content actions.

## Topics

### Collaboration views
- [class SWCollaborationView](./swcollaborationview.md)
  A view that contains the collaboration content and options.
### Collaboration attributes
- [class SWCollaborationHighlight](./swcollaborationhighlight.md)
  A highlight object that represents an active collaboration.
- [class SWCollaborationMetadata](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata)
  A model object for conveying data during a collaboration.
- [struct SWCollaborationIdentifier](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationidentifier)
  A unique identifier for a collaboration.
- [struct SWLocalCollaborationIdentifier](https://developer.apple.com/documentation/sharedwithyoucore/swlocalcollaborationidentifier)
  A local identifier for a collaboration.
- [let SWCollaborationMetadataTypeIdentifier: String](./swcollaborationmetadatatypeidentifier.md)
  A string constant for the metadata type identifier.
### Collaboration management
- [protocol SWCollaborationViewDelegate](./swcollaborationviewdelegate.md)
  A delegate object that the system notifies about changes to the collaboration popover state.
- [class SWCollaborationCoordinator](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationcoordinator)
  An object that contains the shared collaboration coordinator.
- [class SWCollaborationOption](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoption)
  An object that determines how the system shares a document in a collaboration.
- [class SWCollaborationOptionsGroup](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoptionsgroup)
  An object that represents a group of collaboration options that the system displays together.
- [class SWCollaborationOptionsPickerGroup](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoptionspickergroup)
  An object that represents a group of collaboration options that the system displays together with mutually exclusive options.
- [class SWCollaborationShareOptions](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationshareoptions)
  An object that represents the state of the collaboration options for the document.
- [let UTCollaborationOptionsTypeIdentifier: String](https://developer.apple.com/documentation/sharedwithyoucore/utcollaborationoptionstypeidentifier)
  A string constant for the options type identifier.
### Actions
- [class SWAction](https://developer.apple.com/documentation/sharedwithyoucore/swaction)
  An object that represents a collaboration action.
- [class SWStartCollaborationAction](https://developer.apple.com/documentation/sharedwithyoucore/swstartcollaborationaction)
  An object that represents the first action sent to an app when the user shares a collaboration.
- [protocol SWCollaborationActionHandler](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationactionhandler)
  A delegate to handle incoming collaboration actions from a collaboration coordinator.
- [class SWUpdateCollaborationParticipantsAction](https://developer.apple.com/documentation/sharedwithyoucore/swupdatecollaborationparticipantsaction)
  An action that contains the cryptographic identities the system uses to add to or remove from an existing collaboration.

## See Also

### Collaboration
- [Adding shared content collaboration to your app](./adding-shared-content-collaboration-to-your-app.md)
  Manage shared content collaboration in your app using CloudKit and iCloud Drive.
- [Adding custom collaboration to your app](./adding-custom-collaboration-to-your-app.md)
  Integrate your custom collaboration app with Messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/collaboration-views)*