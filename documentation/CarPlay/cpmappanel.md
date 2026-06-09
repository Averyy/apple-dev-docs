# CPMapPanel

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class CPMapPanel
```

## Topics

### Protocols
- [CPMapPanel.Delegate](cpmappanel/delegate-swift.protocol.md)
### Initializers
- [init(title: String?, sections: [CPMapPanelSection], buttonConfiguration: CPMapPanelButtonConfiguration?)](cpmappanel/init(title:sections:buttonconfiguration:).md)
  Initializes a new overlay page.
### Instance Properties
- [var buttonConfiguration: CPMapPanelButtonConfiguration?](cpmappanel/buttonconfiguration.md)
  The button configuration for this page.
- [var delegate: (any CPMapPanel.Delegate)?](cpmappanel/delegate-swift.property.md)
  The @c CPMapPanelDelegate.
- [var sections: [CPMapPanelSection]](cpmappanel/sections.md)
  The sections contained in this page.
- [var title: String?](cpmappanel/title.md)
  The title of the page.

## Relationships

### Inherits From
- [CPPanel](cppanel.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanel)*