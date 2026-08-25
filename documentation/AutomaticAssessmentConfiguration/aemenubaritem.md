# AEMenuBarItem

**Framework**: Automatic Assessment Configuration  
**Kind**: struct

Identifies a menu bar item that can remain visible during an assessment session.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct AEMenuBarItem
```

#### Overview

Use these constants with [`allowedMenuBarItems`](aeassessmentconfiguration/allowedmenubaritems.md) to control which menu bar items stay visible while [`allowsMenuBar`](aeassessmentconfiguration/allowsmenubar.md) is enabled. To allow a third-party menu extra, use its bundle identifier as the raw value.

## Topics

### Initializers
- [init(String)](aemenubaritem/init(_:).md)
- [init(rawValue: String)](aemenubaritem/init(rawvalue:).md)
### Type Properties
- [static let battery: AEMenuBarItem](aemenubaritem/battery.md)
  The Battery system menu bar item.
- [static let bluetooth: AEMenuBarItem](aemenubaritem/bluetooth.md)
  The Bluetooth system menu bar item.
- [static let clock: AEMenuBarItem](aemenubaritem/clock.md)
  The Clock system menu bar item.
- [static let displays: AEMenuBarItem](aemenubaritem/displays.md)
  The Displays system menu bar item.
- [static let keyboard: AEMenuBarItem](aemenubaritem/keyboard.md)
  The Input Menu system menu bar item, which selects keyboard layouts.
- [static let volume: AEMenuBarItem](aemenubaritem/volume.md)
  The Volume system menu bar item.
- [static let wifi: AEMenuBarItem](aemenubaritem/wifi.md)
  The Wi-Fi system menu bar item.
### Type Methods
- [static func menuBarExtra(bundleIdentifier: String) -> AEMenuBarItem](aemenubaritem/menubarextra(bundleidentifier:).md)
  Creates a menu bar extra item representing a custom menu extra.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aemenubaritem)*