# SFSafariToolbarItem

**Framework**: Safari Services  
**Kind**: class

A proxy for a Safari app extension toolbar item in a Safari window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariToolbarItem
```

#### Overview

Your app extension only uses this object when it wants to explicitly set the toolbar item state. Typically, other state changes occur automatically. Safari calls [`validateToolbarItem(in:validationHandler:)`](sfsafariextensionhandling/validatetoolbaritem(in:validationhandler:).md) on your app extension handler when changes, such as navigation to a webpage, could affect the state of the toolbar item.

## Topics

### Controlling Toolbar Items
- [func setEnabled(Bool, withBadgeText: String?)](sfsafaritoolbaritem/setenabled(_:withbadgetext:).md)
  Sets the enabled state and the badge text for the toolbar item.
- [func setBadgeText(String?)](sfsafaritoolbaritem/setbadgetext(_:).md)
  Sets the badge text for the toolbar item.
- [func setEnabled(Bool)](sfsafaritoolbaritem/setenabled(_:).md)
  Sets whether the toolbar item is enabled.
- [func setImage(NSImage?)](sfsafaritoolbaritem/setimage(_:).md)
  Sets the image displayed in the toolbar button.
- [func setLabel(String?)](sfsafaritoolbaritem/setlabel(_:).md)
### Instance Methods
- [func showPopover()](sfsafaritoolbaritem/showpopover.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Using contextual menu and toolbar item keys](using-contextual-menu-and-toolbar-item-keys.md)
  Learn about adding contextual menu items and toolbar items to a Safari app extension with information property list keys.
- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)
  Customize a toolbar item for your Safari app extension.
- [Adjusting settings for contextual menu items](adjusting-settings-for-contextual-menu-items.md)
  Customize contextual menu items for your Safari app extension.
- [class SFSafariExtensionViewController](sfsafariextensionviewcontroller.md)
  The view controller for a popover associated with your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem)*