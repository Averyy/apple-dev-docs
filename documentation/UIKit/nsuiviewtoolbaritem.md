# NSUIViewToolbarItem

**Framework**: UIKit  
**Kind**: class

An item in a window’s toolbar that hosts a custom UIKit view.

**Availability**:
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
class NSUIViewToolbarItem
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Overview

The [`NSUIViewToolbarItem`](nsuiviewtoolbaritem.md) class lets you display a [`UIView`](uiview.md) in an [`NSToolbar`](https://developer.apple.com/documentation/AppKit/NSToolbar). Use this class if you have a custom UIKit view you want to appear as a control in a toolbar when you build your app with Mac Catalyst.

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
- [NSToolbarItem](../AppKit/NSToolbarItem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## See Also

- [@MainActor class NSToolbarItem](../AppKit/NSToolbarItem.md)
  A single item that appears in a window’s toolbar.
- [@MainActor class NSToolbarItemGroup](../AppKit/NSToolbarItemGroup.md)
  A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](../AppKit/NSToolbarItemGroup/ControlRepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](../AppKit/NSToolbarItemGroup/SelectionMode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.
- [@MainActor class NSMenuToolbarItem](../AppKit/NSMenuToolbarItem.md)
  A control that presents a menu in a window’s toolbar.
- [@MainActor class NSSearchToolbarItem](../AppKit/NSSearchToolbarItem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.
- [@MainActor class NSTrackingSeparatorToolbarItem](../AppKit/NSTrackingSeparatorToolbarItem.md)
  A toolbar separator that aligns with the vertical split view in the same window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsuiviewtoolbaritem)*