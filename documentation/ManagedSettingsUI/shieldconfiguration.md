# ShieldConfiguration

**Framework**: Managed Settings UI  
**Kind**: struct

An object that defines the appearance of a shield to display over an application or website.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct ShieldConfiguration
```

#### Overview

The system provides a default appearance for any properties you set to `nil`.

## Topics

### Initializing a shield configuration
- [init(backgroundBlurStyle: UIBlurEffect.Style?, backgroundColor: UIColor?, icon: UIImage?, title: ShieldConfiguration.Label?, subtitle: ShieldConfiguration.Label?, primaryButtonLabel: ShieldConfiguration.Label?, primaryButtonBackgroundColor: UIColor?, secondaryButtonLabel: ShieldConfiguration.Label?)](shieldconfiguration/init(backgroundblurstyle:backgroundcolor:icon:title:subtitle:primarybuttonlabel:primarybuttonbackgroundcolor:secondarybuttonlabel:).md)
  Creates a shield configuration with the specified values.
- [init(backgroundBlurStyle: UIBlurEffect.Style?, backgroundColor: UIColor?, icon: UIImage?, title: ShieldConfiguration.Label?, subtitle: ShieldConfiguration.Label?, primaryButtonLabel: ShieldConfiguration.Label?, primaryButtonBackgroundColor: UIColor?, secondaryButtonLabel: ShieldConfiguration.Label?, secondaryButtonSubmenuItems: [String]?)](shieldconfiguration/init(backgroundblurstyle:backgroundcolor:icon:title:subtitle:primarybuttonlabel:primarybuttonbackgroundcolor:secondarybuttonlabel:secondarybuttonsubmenuitems:).md)
  Initializes a shield configuration with optional submenu items for the secondary button.
### Configure the visual style
- [let backgroundBlurStyle: UIBlurEffect.Style?](shieldconfiguration/backgroundblurstyle.md)
  A blur style to apply to the background of the shield.
- [let backgroundColor: UIColor?](shieldconfiguration/backgroundcolor.md)
  A color for a shield to use in the background blur effect.
- [let icon: UIImage?](shieldconfiguration/icon.md)
  An icon to display in the center of the shield.
### Configure the text content
- [let title: ShieldConfiguration.Label?](shieldconfiguration/title.md)
  The title of the shield to display below the icon.
- [let subtitle: ShieldConfiguration.Label?](shieldconfiguration/subtitle.md)
  The subtitle for a shield to display below the title.
- [ShieldConfiguration.Label](shieldconfiguration/label.md)
  The appearance of text labels within a shield.
### Configure the primary button
- [let primaryButtonLabel: ShieldConfiguration.Label?](shieldconfiguration/primarybuttonlabel.md)
  The label of the topmost rounded rectangle button.
- [let primaryButtonBackgroundColor: UIColor?](shieldconfiguration/primarybuttonbackgroundcolor.md)
  The color to fill the contents of the rounded rectangle primary button.
### Configure the secondary button
- [let secondaryButtonLabel: ShieldConfiguration.Label?](shieldconfiguration/secondarybuttonlabel.md)
  The label of the optional secondary button.
- [let secondaryButtonSubmenuItems: [String]?](shieldconfiguration/secondarybuttonsubmenuitems.md)
  An array of strings that define the items to display in the secondary button’s submenu.

## See Also

- [class ShieldConfigurationDataSource](shieldconfigurationdatasource.md)
  The base class for the principal object of an app extension that configures a shield’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration)*