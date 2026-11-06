# SWCollaborationBarButtonItem

**Framework**: Shared with You  
**Kind**: class  
**Role**: Class

A bar button item that presents collaboration content and options.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
class SWCollaborationBarButtonItem
```

```objc
@interface SWCollaborationBarButtonItem : UIBarButtonItem
```

## Topics

### Customizing the manage button
- [var manageButtonTitle: String](./swcollaborationbarbuttonitem/managebuttontitle.md)
  The title of the built-in button that manages a share.
- [var showManageButton: Bool](./swcollaborationbarbuttonitem/showmanagebutton.md)
  A Boolean value that indicates whether the item shows the built-in button that manages a share.
### Customizing the participant display
- [var showsParticipantCount: Bool](./swcollaborationbarbuttonitem/showsparticipantcount.md)
  A Boolean value that indicates whether the item shows the participant count.
### Customizing the cloud-sharing behavior
- [var cloudSharingControllerDelegate: (any UICloudSharingControllerDelegate)?](./swcollaborationbarbuttonitem/cloudsharingcontrollerdelegate.md)
  The delegate for the sharing controller that the button that manages the share presents.
### Initializers
- [init(itemProvider: NSItemProvider)](./swcollaborationbarbuttonitem/init%28itemprovider%29.md)
### Instance Properties
- [var activeParticipantCount: Int](./swcollaborationbarbuttonitem/activeparticipantcount.md)
- [var detailViewListContent: UIView?](./swcollaborationbarbuttonitem/detailviewlistcontent.md)
- [var pendingAccessRequestsCount: Int](./swcollaborationbarbuttonitem/pendingaccessrequestscount.md)
### Instance Methods
- [func dismissPopover(animated: Bool, completion: (() -> Void)?)](./swcollaborationbarbuttonitem/dismisspopover%28animated,completion%29.md)

## Relationships

### Inherits From
- [UIBarButtonItem](../UIKit/uibarbuttonitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UISpringLoadedInteractionSupporting](../UIKit/uispringloadedinteractionsupporting.md)

## See Also

### Collaboration views
- [class SWCollaborationView](./swcollaborationview.md)
  A view that contains the collaboration content and options.
- [class SWCollaborationToolbarItem](./swcollaborationtoolbaritem.md)
  A toolbar button that presents collaboration content and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationbarbuttonitem)*