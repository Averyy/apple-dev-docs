# CPMapPanelSection

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class CPMapPanelSection
```

#### Overview

Each section contains a title, a collection of content items, and an optional item selection handler.

## Topics

### Initializers
- [init?(coder: NSCoder)](cpmappanelsection/init(coder:).md)
- [init(title: String?, items: [CPMapPanelItem])](cpmappanelsection/init(title:items:).md)
  Initializes a section with items conforming to @c CPMapPanelItem. Only items that adopt @c CPMapPanelItem are supported when displaying panel sections on a @c CPMapTemplate.
### Instance Properties
- [var items: [CPMapPanelItem]](cpmappanelsection/items.md)
  The items displayed in this section, or @c nil if the section does not contain items.
- [var title: String?](cpmappanelsection/title.md)
  The title of the section.
### Instance Methods
- [func updateItems([CPMapPanelItem])](cpmappanelsection/updateitems(_:).md)
  Update the items in this section. If this section is currently visible in a panel, the panel will refresh to show the new items.

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelsection)*