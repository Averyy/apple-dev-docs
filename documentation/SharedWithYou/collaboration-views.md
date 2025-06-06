# Collaboration views

**Framework**: Shared With You

Create and customize a collaboration view to manage the shared content actions.

## Topics

### Collaboration views
- [class SWCollaborationView](swcollaborationview.md)
  A view that contains the collaboration content and options.
### Collaboration attributes
- [class SWCollaborationHighlight](swcollaborationhighlight.md)
  A highlight object that represents an active collaboration.
- [class SWCollaborationMetadata](../sharedwithyoucore/swcollaborationmetadata.md)
  A model object for conveying data during a collaboration.
- [struct SWCollaborationIdentifier](../sharedwithyoucore/swcollaborationidentifier.md)
  A unique identifier for a collaboration.
- [struct SWLocalCollaborationIdentifier](../sharedwithyoucore/swlocalcollaborationidentifier.md)
  A local identifier for a collaboration.
- [let SWCollaborationMetadataTypeIdentifier: String](swcollaborationmetadatatypeidentifier.md)
  A string constant for the metadata type identifier.
### Collaboration management
- [protocol SWCollaborationViewDelegate](swcollaborationviewdelegate.md)
  A delegate object that the system notifies about changes to the collaboration popover state.
- [class SWCollaborationCoordinator](../sharedwithyoucore/swcollaborationcoordinator.md)
  An object that contains the shared collaboration coordinator.
- [class SWCollaborationOption](../sharedwithyoucore/swcollaborationoption.md)
  An object that determines how the system shares a document in a collaboration.
- [class SWCollaborationOptionsGroup](../sharedwithyoucore/swcollaborationoptionsgroup.md)
  An object that represents a group of collaboration options that the system displays together.
- [class SWCollaborationOptionsPickerGroup](../sharedwithyoucore/swcollaborationoptionspickergroup.md)
  An object that represents a group of collaboration options that the system displays together with mutually exclusive options.
- [class SWCollaborationShareOptions](../sharedwithyoucore/swcollaborationshareoptions.md)
  An object that represents the state of the collaboration options for the document.
- [let UTCollaborationOptionsTypeIdentifier: String](../sharedwithyoucore/utcollaborationoptionstypeidentifier.md)
  A string constant for the options type identifier.
### Actions
- [class SWAction](../sharedwithyoucore/swaction.md)
  An object that represents a collaboration action.
- [class SWStartCollaborationAction](../sharedwithyoucore/swstartcollaborationaction.md)
  An object that represents the first action sent to an app when the user shares a collaboration.
- [protocol SWCollaborationActionHandler](../sharedwithyoucore/swcollaborationactionhandler.md)
  A delegate to handle incoming collaboration actions from a collaboration coordinator.
- [class SWUpdateCollaborationParticipantsAction](../sharedwithyoucore/swupdatecollaborationparticipantsaction.md)
  An action that contains the cryptographic identities the system uses to add to or remove from an existing collaboration.

## See Also

- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)
  Manage shared content collaboration in your app using CloudKit and iCloud Drive.
- [Adding custom collaboration to your app](adding-custom-collaboration-to-your-app.md)
  Integrate your custom collaboration app with Messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/collaboration-views)*