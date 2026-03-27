# Managed Settings UI

**Framework**: Managed Settings UI  
**Kind**: module

Define and configure the appearance of shielding views.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

#### Overview

Use Managed Settings UI to customize the appearance of shields that the system displays when someone applies access restrictions to apps or websites. Shields appear when someone exceeds app or website usage limits, such as their daily time allowance, or when access attempts occur during restricted hours.

This framework works with [`Managed Settings`](https://developer.apple.com/documentation/managedsettings) to customize access control shielding. [`Managed Settings`](https://developer.apple.com/documentation/managedsettings) handles shield actions and enforcement, and Managed Settings UI lets you customize the visual presentation with custom button style, titles, icons, colors, and submenu items.

## Topics

### Shield appearance
- [struct ShieldConfiguration](shieldconfiguration.md)
  An object that defines the appearance of a shield to display over an application or website.
- [class ShieldConfigurationDataSource](shieldconfigurationdatasource.md)
  The base class for the principal object of an app extension that configures a shield’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ManagedSettingsUI)*