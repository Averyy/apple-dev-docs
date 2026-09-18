# CPMapPanelSection

**Framework**: CarPlay  
**Kind**: class

A single section of a map panel that you fill with a title and one or more items.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPMapPanelSection
```

#### Overview

The `CPMapPanelSection` class organizes a single section of content in a [`CPMapPanel`](cpmappanel.md) interface. In a navigation app, you use map panels to display relevant information such as route options or the location of charging stations on top of your custom map. Section objects manage one or more related items you want to display. For example, you might use one section to display upcoming charging stations and a different section to display route choices.

Create a `CPMapPanelSection` object and configure it with the section title and a [`CPMapPanelItem`](cpmappanelitem.md) object for each item you want to display. Add the section to your [`CPMapPanel`](cpmappanel.md) object before showing the panel from your map template. If you modify a section after the panel is visible, the system updates the section’s contents in your CarPlay interface.

## Topics

### Initializers
- [init?(coder: NSCoder)](cpmappanelsection/init(coder:).md)
- [init(title: String?, items: [CPMapPanelItem])](cpmappanelsection/init(title:items:).md)
  Initializes the section with the specified title and items.
### Instance Properties
- [var items: [CPMapPanelItem]](cpmappanelsection/items.md)
  The items to display in the section.
- [var title: String?](cpmappanelsection/title.md)
  The localized string to display for the section title.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelsection)*