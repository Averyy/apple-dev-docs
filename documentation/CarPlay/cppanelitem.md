# CPPanelItem

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that provides the common behaviors for items you display in a section of a panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPPanelItem
```

```objc
@interface CPPanelItem : NSObject
```

## Overview

The `CPPanelItem` type defines the default behaviors for content you display in a panel. You don’t create this type directly or use it to configure the contents of your panel. Instead, instantiate one of the defined subclasses based on the type of panel you’re configuring. For example, create [`CPMapPanelItem`](./cpmappanelitem.md) objects when configuring the content for a [`CPMapPanel`](./cpmappanel.md) type.

## Topics

### Initializing the panel
- [init(listItem: CPListItem)](./cppanelitem/init%28listitem%29.md)
  Initialize the item using a list item.
- [init(gridButtons: [CPGridButton])](./cppanelitem/init%28gridbuttons%29.md)
  Initialize the item using one or more grid buttons.
- [init?(coder: NSCoder)](./cppanelitem/init%28coder%29.md)
### Configuring the panel’s behavior
- [var isEnabled: Bool](./cppanelitem/isenabled.md)
  A Boolean value that indicates whether the item supports interactions.
- [var showsBottomSeparator: Bool](./cppanelitem/showsbottomseparator.md)
  A Boolean value that indicates whether a separator line appears at the bottom edge of the item.
### Accessing app-specific data
- [var userInfo: Any?](./cppanelitem/userinfo.md)
  Custom information you want to store with the item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPMapPanelItem](./cpmappanelitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Common types
- [class CPTemplate](./cptemplate.md)
  An abstract base class for interface templates.
- [class CPTextButton](./cptextbutton.md)
  A button that displays a stylized title.
- [class CPButton](./cpbutton.md)
  A button that displays an image and invokes a handler when the user taps it.
- [class CPImageSet](./cpimageset.md)
  Light and dark representations of an image.
- [class CPPanel](./cppanel.md)
  A type that provides the common behaviors for panels you display on top of your app’s content.
- [class CPPanelButtonConfiguration](./cppanelbuttonconfiguration.md)
  A type that provides the common behaviors for a button layout in a panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanelitem)*