# ShieldConfiguration

**Framework**: ManagedSettingsUI  
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

### Defining the Appearance
- [let backgroundBlurStyle: UIBlurEffect.Style?](shieldconfiguration/backgroundblurstyle.md)
  A blur style to apply to the background of the shield.
- [let backgroundColor: UIColor?](shieldconfiguration/backgroundcolor.md)
  A color for a shield to use in the background blur effect.
- [let icon: UIImage?](shieldconfiguration/icon.md)
  An icon to display in the center of the shield.
- [let primaryButtonBackgroundColor: UIColor?](shieldconfiguration/primarybuttonbackgroundcolor.md)
  The color to fill the contents of the rounded rectangle primary button.
- [let primaryButtonLabel: ShieldConfiguration.Label?](shieldconfiguration/primarybuttonlabel.md)
  The label of the topmost rounded rectangle button.
- [let secondaryButtonLabel: ShieldConfiguration.Label?](shieldconfiguration/secondarybuttonlabel.md)
  The label of the optional secondary button.
- [let subtitle: ShieldConfiguration.Label?](shieldconfiguration/subtitle.md)
  The subtitle for a shield to display below the title.
- [let title: ShieldConfiguration.Label?](shieldconfiguration/title.md)
  The title of the shield to display below the icon.
- [ShieldConfiguration.Label](shieldconfiguration/label.md)
  The appearance of text labels within a shield.
### Creating the Shield Configuration
- [init(backgroundBlurStyle: UIBlurEffect.Style?, backgroundColor: UIColor?, icon: UIImage?, title: ShieldConfiguration.Label?, subtitle: ShieldConfiguration.Label?, primaryButtonLabel: ShieldConfiguration.Label?, primaryButtonBackgroundColor: UIColor?, secondaryButtonLabel: ShieldConfiguration.Label?)](shieldconfiguration/init(backgroundblurstyle:backgroundcolor:icon:title:subtitle:primarybuttonlabel:primarybuttonbackgroundcolor:secondarybuttonlabel:).md)
  Creates a shield configuration with the specified values.

## See Also

- [class ShieldConfigurationDataSource](shieldconfigurationdatasource.md)
  The base class for the principal object of an app extension that configures a shield’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration)*