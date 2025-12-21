# SWCollaborationViewDelegate

**Framework**: Shared with You  
**Kind**: protocol

A delegate object that the system notifies about changes to the collaboration popover state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol SWCollaborationViewDelegate : NSObjectProtocol
```

## Topics

### Responding to popover activity
- [func collaborationViewShouldPresentPopover(SWCollaborationView) -> Bool](swcollaborationviewdelegate/collaborationviewshouldpresentpopover(_:).md)
  Asks the delegate whether the system can display the popover.
- [func collaborationViewDidDismissPopover(SWCollaborationView)](swcollaborationviewdelegate/collaborationviewdiddismisspopover(_:).md)
  Notifies the delegate after the system dismisses the popover.
- [func collaborationViewWillPresentPopover(SWCollaborationView)](swcollaborationviewdelegate/collaborationviewwillpresentpopover(_:).md)
  Notifies the delegate before the system presents the popover.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationviewdelegate)*