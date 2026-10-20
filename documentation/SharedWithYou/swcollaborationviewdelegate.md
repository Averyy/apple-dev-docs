# SWCollaborationViewDelegate

**Framework**: Shared with You  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol SWCollaborationViewDelegate <NSObject>
```

## Topics

### Responding to popover activity
- [func collaborationViewShouldPresentPopover(SWCollaborationView) -> Bool](./swcollaborationviewdelegate/collaborationviewshouldpresentpopover%28_%29.md)
  Asks the delegate whether the system can display the popover.
- [func collaborationViewDidDismissPopover(SWCollaborationView)](./swcollaborationviewdelegate/collaborationviewdiddismisspopover%28_%29.md)
  Notifies the delegate after the system dismisses the popover.
- [func collaborationViewWillPresentPopover(SWCollaborationView)](./swcollaborationviewdelegate/collaborationviewwillpresentpopover%28_%29.md)
  Notifies the delegate before the system presents the popover.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Collaboration management
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationviewdelegate)*