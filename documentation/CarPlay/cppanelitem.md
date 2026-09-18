# CPPanelItem

**Framework**: CarPlay  
**Kind**: class

A type that provides the common behaviors for items you display in a section of a panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPPanelItem
```

#### Overview

The `CPPanelItem` type defines the default behaviors for content you display in a panel. You don’t create this type directly or use it to configure the contents of your panel. Instead, instantiate one of the defined subclasses based on the type of panel you’re configuring. For example, create [`CPMapPanelItem`](cpmappanelitem.md) objects when configuring the content for a [`CPMapPanel`](cpmappanel.md) type.

## Topics

### Initializers
- [init?(coder: NSCoder)](cppanelitem/init(coder:).md)
- [init(gridButtons: [CPGridButton])](cppanelitem/init(gridbuttons:).md)
  Initialize the item using one or more grid buttons.
- [init(listItem: CPListItem)](cppanelitem/init(listitem:).md)
  Initialize the item using a list item.
### Instance Properties
- [var isEnabled: Bool](cppanelitem/isenabled.md)
  A Boolean value that indicates whether the item supports interactions.
- [var showsBottomSeparator: Bool](cppanelitem/showsbottomseparator.md)
  A Boolean value that indicates whether a separator line appears at the bottom edge of the item.
- [var userInfo: Any?](cppanelitem/userinfo.md)
  Custom information you want to store with the item.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [CPMapPanelItem](cpmappanelitem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanelitem)*