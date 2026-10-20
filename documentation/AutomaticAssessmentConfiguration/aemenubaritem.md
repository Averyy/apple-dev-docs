# AEMenuBarItem

**Framework**: Automatic Assessment Configuration  
**Kind**: struct  
**Role**: Structure

Identifies a menu bar item that can remain visible during an assessment session.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct AEMenuBarItem
```

```c
typedef NSString * AEMenuBarItem;
```

#### Overview

Use these constants with [`allowedMenuBarItems`](./aeassessmentconfiguration/allowedmenubaritems.md) to control which menu bar items stay visible while [`allowsMenuBar`](./aeassessmentconfiguration/allowsmenubar.md) is enabled. To allow a third-party menu extra, use its bundle identifier as the raw value.

## Topics

### Initializers
- [init(String)](./aemenubaritem/init%28_%29.md)
- [init(rawValue: String)](./aemenubaritem/init%28rawvalue%29.md)
### Type Properties
- [static let battery: AEMenuBarItem](./aemenubaritem/battery.md)
  The Battery system menu bar item.
- [static let bluetooth: AEMenuBarItem](./aemenubaritem/bluetooth.md)
  The Bluetooth system menu bar item.
- [static let clock: AEMenuBarItem](./aemenubaritem/clock.md)
  The Clock system menu bar item.
- [static let displays: AEMenuBarItem](./aemenubaritem/displays.md)
  The Displays system menu bar item.
- [static let keyboard: AEMenuBarItem](./aemenubaritem/keyboard.md)
  The Input Menu system menu bar item, which selects keyboard layouts.
- [static let volume: AEMenuBarItem](./aemenubaritem/volume.md)
  The Volume system menu bar item.
- [static let wifi: AEMenuBarItem](./aemenubaritem/wifi.md)
  The Wi-Fi system menu bar item.
### Type Methods
- [static func menuBarExtra(bundleIdentifier: String) -> AEMenuBarItem](./aemenubaritem/menubarextra%28bundleidentifier%29.md)
  Creates a menu bar extra item representing a custom menu extra.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aemenubaritem)*