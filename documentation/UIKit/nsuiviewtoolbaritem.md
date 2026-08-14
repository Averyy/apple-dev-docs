# NSUIViewToolbarItem

**Framework**: UIKit  
**Kind**: class

An item in a window’s toolbar that hosts a custom UIKit view.

**Availability**:
- Mac Catalyst 16.0+

## Declaration

```swift
class NSUIViewToolbarItem
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Overview

The [`NSUIViewToolbarItem`](nsuiviewtoolbaritem.md) class lets you display a [`UIView`](uiview.md) in an [`NSToolbar`](https://developer.apple.com/documentation/appkit/nstoolbar). Use this class if you have a custom UIKit view you want to appear as a control in a toolbar when you build your app with Mac Catalyst.

For UIKit controls that support behavioral styles, set [`preferredBehavioralStyle`](uibutton/preferredbehavioralstyle.md) to [`UIBehavioralStyle.mac`](uibehavioralstyle/mac.md) if you want them to appear in the toolbar with the appearance and behavior of AppKit controls.

## Topics

### Creating a toolbar item
- [init(itemIdentifier: NSToolbarItem.Identifier, uiView: UIView)](nsuiviewtoolbaritem/init(itemidentifier:uiview:).md)
  Creates a toolbar item with the identifier and underlying UIKit view you specify.
### Managing the view
- [var uiView: UIView](nsuiviewtoolbaritem/uiview.md)
  The UIKit view to host in an AppKit toolbar.

## Relationships

### Inherits From
- [NSToolbarItem](../appkit/nstoolbaritem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## See Also

- [class NSToolbarItem](../appkit/nstoolbaritem.md)
  A single item that appears in a window’s toolbar.
- [class NSToolbarItemGroup](../appkit/nstoolbaritemgroup.md)
  A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](../appkit/nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](../appkit/nstoolbaritemgroup/selectionmode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.
- [class NSMenuToolbarItem](../appkit/nsmenutoolbaritem.md)
  A control that presents a menu in a window’s toolbar.
- [class NSSearchToolbarItem](../appkit/nssearchtoolbaritem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.
- [class NSTrackingSeparatorToolbarItem](../appkit/nstrackingseparatortoolbaritem.md)
  A toolbar separator that aligns with the vertical split view in the same window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsuiviewtoolbaritem)*