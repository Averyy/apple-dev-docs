# SWCollaborationToolbarItem

**Framework**: Shared with You  
**Kind**: class  
**Role**: Class

A toolbar button that presents collaboration content and options.

**Availability**:
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
class SWCollaborationToolbarItem
```

```objc
@interface SWCollaborationToolbarItem : NSToolbarItem
```

## Topics

### Customizing the manage button
- [var manageButtonTitle: String](./swcollaborationtoolbaritem/managebuttontitle.md)
  The title of the built-in button that manages a share.
- [var showManageButton: Bool](./swcollaborationtoolbaritem/showmanagebutton.md)
  A Boolean value that indicates whether the item shows the built-in button that manages the share.
### Customizing the participant display
- [var showsParticipantCount: Bool](./swcollaborationtoolbaritem/showsparticipantcount.md)
  A Boolean value that indicates whether the item shows the participant count.
### Initializers
- [init(itemProvider: NSItemProvider)](./swcollaborationtoolbaritem/init%28itemprovider%29.md)
### Instance Properties
- [var activeParticipantCount: Int](./swcollaborationtoolbaritem/activeparticipantcount.md)
- [var detailViewListContent: NSView?](./swcollaborationtoolbaritem/detailviewlistcontent.md)
- [var pendingAccessRequestsCount: Int](./swcollaborationtoolbaritem/pendingaccessrequestscount.md)
### Instance Methods
- [func dismissPopover(animated: Bool, completion: (() -> Void)?)](./swcollaborationtoolbaritem/dismisspopover%28animated,completion%29.md)

## Relationships

### Inherits From
- [NSToolbarItem](../AppKit/nstoolbaritem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMenuItemValidation](../AppKit/nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSValidatedUserInterfaceItem](../AppKit/nsvalidateduserinterfaceitem.md)

## See Also

### Collaboration views
- [class SWCollaborationView](./swcollaborationview.md)
  A view that contains the collaboration content and options.
- [class SWCollaborationBarButtonItem](./swcollaborationbarbuttonitem.md)
  A bar button item that presents collaboration content and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationtoolbaritem)*