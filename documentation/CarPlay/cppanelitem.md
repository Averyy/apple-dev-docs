# CPPanelItem

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class CPPanelItem
```

#### Overview

Subclasses represent items specific to a particular template context (e.g., @c CPMapPanelItem for map templates).

## Topics

### Initializers
- [init?(coder: NSCoder)](cppanelitem/init(coder:).md)
- [init(gridButtons: [CPGridButton])](cppanelitem/init(gridbuttons:).md)
  Initializes a panel item wrapping an array of @c CPGridButton objects.
- [init(listItem: CPListItem)](cppanelitem/init(listitem:).md)
  Initializes a panel item wrapping a @c CPListItem.
### Instance Properties
- [var isEnabled: Bool](cppanelitem/isenabled.md)
  Whether the item is interactable. Defaults to @c YES.
- [var showsBottomSeparator: Bool](cppanelitem/showsbottomseparator.md)
  When @c NO, the bottom separator line below this item is not drawn. Defaults to @c YES.
- [var userInfo: Any?](cppanelitem/userinfo.md)
  Any custom user info related to this item.

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