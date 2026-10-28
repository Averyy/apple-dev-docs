# NSUIViewToolbarItem

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An item in a window’s toolbar that hosts a custom UIKit view.

**Availability**:
- Mac Catalyst 16.0+

## Declaration

```swift
class NSUIViewToolbarItem
```

```objc
@interface NSUIViewToolbarItem : NSToolbarItem
```

## Mentions

- [Building a desktop-class iPad app](./building-a-desktop-class-ipad-app.md)

## Overview

The [`NSUIViewToolbarItem`](./nsuiviewtoolbaritem.md) class lets you display a [`UIView`](./uiview.md) in an [`NSToolbar`](../AppKit/nstoolbar.md). Use this class if you have a custom UIKit view you want to appear as a control in a toolbar when you build your app with Mac Catalyst.

For UIKit controls that support behavioral styles, set [`preferredBehavioralStyle`](./uibutton/preferredbehavioralstyle.md) to [`UIBehavioralStyle.mac`](./uibehavioralstyle/mac.md) if you want them to appear in the toolbar with the appearance and behavior of AppKit controls.

## Topics

### Creating a toolbar item
- [init(itemIdentifier: NSToolbarItem.Identifier, uiView: UIView)](./nsuiviewtoolbaritem/init%28itemidentifier,uiview%29.md)
  Creates a toolbar item with the identifier and underlying UIKit view you specify.
### Managing the view
- [var uiView: UIView](./nsuiviewtoolbaritem/uiview.md)
  The UIKit view to host in an AppKit toolbar.

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
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIPopoverPresentationControllerSourceItem](./uipopoverpresentationcontrollersourceitem.md)

## See Also

### Items
- [class NSToolbarItem](../AppKit/nstoolbaritem.md)
  A single item that appears in a window’s toolbar.
- [class NSToolbarItemGroup](../AppKit/nstoolbaritemgroup.md)
  A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](../AppKit/nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](../AppKit/nstoolbaritemgroup/selectionmode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.
- [class NSMenuToolbarItem](../AppKit/nsmenutoolbaritem.md)
  A control that presents a menu in a window’s toolbar.
- [class NSSearchToolbarItem](../AppKit/nssearchtoolbaritem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.
- [class NSTrackingSeparatorToolbarItem](../AppKit/nstrackingseparatortoolbaritem.md)
  A toolbar separator that aligns with the vertical split view in the same window.
- [NSToolbarItemIdentifier](./nstoolbaritemidentifier.md)
  UIKit-specific constants for the standard toolbar items that the system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsuiviewtoolbaritem)*