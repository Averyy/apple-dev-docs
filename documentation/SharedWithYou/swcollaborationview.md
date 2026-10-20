# SWCollaborationView

**Framework**: Shared with You  
**Kind**: class  
**Role**: Class

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

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@interface SWCollaborationView : UIView
```

*macOS*

```objc
@interface SWCollaborationView : NSView
```

## Mentions

- [Adding shared content collaboration to your app](./adding-shared-content-collaboration-to-your-app.md)

#### Overview

The system presents an `SWCollaborationView` that displays participants and sharing options to a collaborator. For CloudKit and iCloud Drive adopters, the collaboration view includes a manage button. The button brings up the manage user interface, where collaborators can add and remove participants or change the share settings.

## Topics

### Creating a collaboration view
- [init(itemProvider: NSItemProvider)](./swcollaborationview/init%28itemprovider%29.md)
  Creates and initializes a collaboration view.
### Accessing view attributes
- [var activeParticipantCount: Int](./swcollaborationview/activeparticipantcount.md)
  The number of participants in a collaboration.
- [var cloudSharingDelegate: (any UICloudSharingControllerDelegate)?](./swcollaborationview/cloudsharingdelegate.md)
  The delegate object for the cloud-sharing controller.
- [var delegate: (any SWCollaborationViewDelegate)?](./swcollaborationview/delegate.md)
  The delegate object for the collaboration view.
- [var headerImage: UIImage](./swcollaborationview/headerimage.md)
  The image that the system displays in the header.
- [var headerSubtitle: String](./swcollaborationview/headersubtitle.md)
  The subtitle that the system displays in the header.
- [var headerTitle: String](./swcollaborationview/headertitle.md)
  The title that the system displays in the header.
- [var manageButtonTitle: String](./swcollaborationview/managebuttontitle.md)
  The manage button title that the system displays in the header.
- [var menuFormRepresentation: NSMenuItem](./swcollaborationview/menuformrepresentation-3sffe.md)
  Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.
- [var menuFormRepresentation: NSMenuItem](./swcollaborationview/menuformrepresentation-55skx.md)
  Returns a menu item suitable to display the collaboration detail view from the toolbar overflow menu.
### Setting view attributes
- [func setContent(UIView)](./swcollaborationview/setcontent%28_%29.md)
  Sets the content view.
- [func setDetailViewListContent<ListContent>(ListContent)](./swcollaborationview/setdetailviewlistcontent%28_%29-88gy5.md)
  Sets the detail view for the list content.
- [func setDetailViewListContent<ListContent>(() -> ListContent)](./swcollaborationview/setdetailviewlistcontent%28_%29-8ml1c.md)
  Sets the detail view for the list content from view builder closures.
- [func setShowManageButton(Bool)](./swcollaborationview/setshowmanagebutton%28_%29.md)
  A Boolean value the system uses to show or hide the default manage-participants button in the collaboration popover.
### Dismissing the popover
- [func dismissPopover((() -> Void)?)](./swcollaborationview/dismisspopover%28_%29.md)
  Dismisses the popover.
### Customizing the cloud-sharing behavior
- [var cloudSharingControllerDelegate: (any UICloudSharingControllerDelegate)?](./swcollaborationview/cloudsharingcontrollerdelegate.md)
  A reference to an object that conforms to the CloudKit sharing controller delegate protocol.
- [var cloudSharingServiceDelegate: (any NSCloudSharingServiceDelegate)?](./swcollaborationview/cloudsharingservicedelegate.md)
  A reference to an object that conforms to the cloud-sharing service delegate protocol.
### Instance Properties
- [var pendingAccessRequestsCount: Int](./swcollaborationview/pendingaccessrequestscount.md)
- [var showsParticipantCount: Bool](./swcollaborationview/showsparticipantcount.md)
  Whether the collaboration button should show the participant count. Defaults to YES.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview)*