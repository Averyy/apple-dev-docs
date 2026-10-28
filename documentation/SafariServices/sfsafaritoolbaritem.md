# SFSafariToolbarItem

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

A proxy for a Safari app extension toolbar item in a Safari window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariToolbarItem
```

```objc
@interface SFSafariToolbarItem : NSObject
```

## Overview

Your app extension only uses this object when it wants to explicitly set the toolbar item state. Typically, other state changes occur automatically. Safari calls [`validateToolbarItem(in:validationHandler:)`](./sfsafariextensionhandling/validatetoolbaritem%28in,validationhandler%29.md) on your app extension handler when changes, such as navigation to a webpage, could affect the state of the toolbar item.

## Topics

### Controlling Toolbar Items
- [func setEnabled(Bool, withBadgeText: String?)](./sfsafaritoolbaritem/setenabled%28_,withbadgetext%29.md)
  Sets the enabled state and the badge text for the toolbar item.
- [func setBadgeText(String?)](./sfsafaritoolbaritem/setbadgetext%28_%29.md)
  Sets the badge text for the toolbar item.
- [func setEnabled(Bool)](./sfsafaritoolbaritem/setenabled%28_%29.md)
  Sets whether the toolbar item is enabled.
- [func setImage(NSImage?)](./sfsafaritoolbaritem/setimage%28_%29.md)
  Sets the image displayed in the toolbar button.
- [func setLabel(String?)](./sfsafaritoolbaritem/setlabel%28_%29.md)
### Instance Methods
- [func showPopover()](./sfsafaritoolbaritem/showpopover%28%29.md)
### Initializers
- [init?(coder: NSCoder)](./sfsafaritoolbaritem/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Contextual menu and toolbar items
- [Using contextual menu and toolbar item keys](./using-contextual-menu-and-toolbar-item-keys.md)
  Learn about adding contextual menu items and toolbar items to a Safari app extension with information property list keys.
- [Adjusting settings for a toolbar item](./adjusting-settings-for-a-toolbar-item.md)
  Customize a toolbar item for your Safari app extension.
- [Adjusting settings for contextual menu items](./adjusting-settings-for-contextual-menu-items.md)
  Customize contextual menu items for your Safari app extension.
- [class SFSafariExtensionViewController](./sfsafariextensionviewcontroller.md)
  The view controller for a popover associated with your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem)*