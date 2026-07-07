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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CPMapPanelItem](cpmappanelitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanelitem)*