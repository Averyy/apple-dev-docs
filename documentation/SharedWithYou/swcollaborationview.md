# SWCollaborationView

**Framework**: Shared With You  
**Kind**: class

A view that contains the collaboration content and options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class SWCollaborationView
```

## Mentions

- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)

#### Overview

The system presents an `SWCollaborationView` that displays participants and sharing options to a collaborator. For CloudKit and iCloud Drive adopters, the collaboration view includes a manage button. The button brings up the manage user interface, where collaborators can add and remove participants or change the share settings.

## Topics

### Creating a collaboration view
- [init(itemProvider: NSItemProvider)](swcollaborationview/init(itemprovider:).md)
  Creates and initializes a collaboration view.
### Accessing view attributes
- [var activeParticipantCount: Int](swcollaborationview/activeparticipantcount.md)
  The number of participants in a collaboration.
- [var cloudSharingDelegate: (any UICloudSharingControllerDelegate)?](swcollaborationview/cloudsharingdelegate.md)
  The delegate object for the cloud-sharing controller.
- [var delegate: (any SWCollaborationViewDelegate)?](swcollaborationview/delegate.md)
  The delegate object for the collaboration view.
- [var headerImage: UIImage](swcollaborationview/headerimage.md)
  The image that the system displays in the header.
- [var headerSubtitle: String](swcollaborationview/headersubtitle.md)
  The subtitle that the system displays in the header.
- [var headerTitle: String](swcollaborationview/headertitle.md)
  The title that the system displays in the header.
- [var manageButtonTitle: String](swcollaborationview/managebuttontitle.md)
  The manage button title that the system displays in the header.
- [var menuFormRepresentation: NSMenuItem](swcollaborationview/menuformrepresentation-3sffe.md)
  Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.
- [var menuFormRepresentation: NSMenuItem](swcollaborationview/menuformrepresentation-55skx.md)
  Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.
### Setting view attributes
- [func setContent(UIView)](swcollaborationview/setcontent(_:).md)
  Sets the content view.
- [func setDetailViewListContent<ListContent>(ListContent)](swcollaborationview/setdetailviewlistcontent(_:)-88gy5.md)
  Sets the detail view for the list content.
- [func setDetailViewListContent<ListContent>(() -> ListContent)](swcollaborationview/setdetailviewlistcontent(_:)-8ml1c.md)
  Sets the detail view for the list content from view builder closures.
- [func setShowManageButton(Bool)](swcollaborationview/setshowmanagebutton(_:).md)
  A Boolean value the system uses to show or hide the default manage-participants button in the collaboration popover.
### Dismissing the popover
- [func dismissPopover((() -> Void)?)](swcollaborationview/dismisspopover(_:).md)
  Dismisses the popover.
### Customizing the cloud-sharing behavior
- [var cloudSharingControllerDelegate: (any UICloudSharingControllerDelegate)?](swcollaborationview/cloudsharingcontrollerdelegate.md)
  A reference to an object that conforms to the CloudKit sharing controller delegate protocol.
- [var cloudSharingServiceDelegate: (any NSCloudSharingServiceDelegate)?](swcollaborationview/cloudsharingservicedelegate.md)
  A reference to an object that conforms to the cloud-sharing service delegate protocol.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview)*