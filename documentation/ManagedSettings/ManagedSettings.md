# ManagedSettings

**Framework**: ManagedSettings  
**Kind**: module

Access and change settings with your app while maintaining user privacy and control.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

#### Overview

Managed Settings provides a privacy-preserving way for users to restrict access to certain settings and features on their devices. With the user’s permission, your app can limit media showings, restrict app purchases, lock passcode settings, and configure other device behavior.

![A diagram consisting of three icons with an on-and-off toggle switch below each one. On the left is a Settings icon with an toggle switch representing the on state. In the middle is an App Store icon with a toggle switch represeting the off state. To the right is a Safari icon with a toggle switch representing the on state.](https://docs-assets.developer.apple.com/published/acc1e9abeed55948d8f76d19856eac54/managed-settings-overview%402x.png)

Managed Settings works together with [`ManagedSettingsUI`](https://developer.apple.com/documentation/ManagedSettingsUI), [`DeviceActivity`](https://developer.apple.com/documentation/DeviceActivity), and [`FamilyControls`](https://developer.apple.com/documentation/FamilyControls) to allow your app to restrict, authorize, and monitor device usage. To learn more about authorizing Managed Settings on your app, see [`FamilyControls`](https://developer.apple.com/documentation/FamilyControls). For more information about monitoring and scheduling device usage with your app, see [`DeviceActivity`](https://developer.apple.com/documentation/DeviceActivity).

## Topics

### Essentials
- [Manage Settings on Devices in a Family Sharing Group](connectionwithframeworks.md)
  Empower parents and guardians to configure constraints on other devices while preserving the family’s privacy.
- [Confirming the Effective TV and Movie Ratings](readingmedia.md)
  Read the media rating on a device and determine what media to display on your app.
### Settings
- [class ManagedSettingsStore](managedsettingsstore.md)
  A data store that applies settings to the current user or device.
### Shield Actions
- [class ShieldActionDelegate](shieldactiondelegate.md)
  A class for an extension that handles shield actions.
### Family Privacy
- [struct Token](token.md)
  A representation of an activity, such as an app or website, that doesn’t reveal its identity.
### Apps
- [struct Application](application.md)
  A representation of an application on the user’s device.
- [typealias ApplicationToken](applicationtoken.md)
  A representation of an application.
### Categories
- [struct ActivityCategory](activitycategory.md)
  An activity’s category, such as Entertainment or Social.
- [typealias ActivityCategoryToken](activitycategorytoken.md)
  A token that represents a category of app or website activity.
### Websites
- [struct WebDomain](webdomain.md)
  An object that represents a website.
- [typealias WebDomainToken](webdomaintoken.md)
  A representation of a web domain that preserves the user’s privacy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ManagedSettings)*