# AppStoreSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints on a user’s App Store settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct AppStoreSettings
```

#### Overview

Use `AppStoreSettings` to manage a user’s App Store settings. You can set a maximum age rating for apps, deny in-app purchases, and require passwords for purchases.

## Topics

### Denying In-App Purchases
- [var denyInAppPurchases: Bool?](appstoresettings/denyinapppurchases-swift.property.md)
  A Boolean value that indicates whether to deny the user permission to make in-app purchases.
- [static let denyInAppPurchases: SettingMetadata<Bool>](appstoresettings/denyinapppurchases-swift.type.property.md)
  The metadata associated with the setting to deny in-app purchases.
### Setting an App Rating Limit
- [var maximumRating: Int?](appstoresettings/maximumrating-swift.property.md)
  The maximum app rating the user can download.
- [static let maximumRating: BoundedSettingMetadata<Int>](appstoresettings/maximumrating-swift.type.property.md)
  The metadata associated with the maximum app rating setting.
### Requiring a Password
- [var requirePasswordForPurchases: Bool?](appstoresettings/requirepasswordforpurchases-swift.property.md)
  A Boolean value that indicates whether to require the user’s password to make App Store transactions.
- [static let requirePasswordForPurchases: SettingMetadata<Bool>](appstoresettings/requirepasswordforpurchases-swift.type.property.md)
  The metadata associated with the setting that requires a password for App Store purchases.

## Relationships

### Conforms To
- [ManagedSettingsGroup](managedsettingsgroup.md)

## See Also

- [var appStore: AppStoreSettings](managedsettingsstore/appstore.md)
  Settings that affect the App Store.
- [var application: ApplicationSettings](managedsettingsstore/application.md)
  Settings that affect applications.
- [struct ApplicationSettings](applicationsettings.md)
  Constraints on the apps and categories of apps a user can run on their device.
- [var effectiveMaximumMovieRating: Int](managedsettingsstore/effectivemaximummovierating.md)
  The movie rating constraint that is active on this device.
- [var effectiveMaximumTVShowRating: Int](managedsettingsstore/effectivemaximumtvshowrating.md)
  The TV rating constraint that is active on this device.
- [var gameCenter: GameCenterSettings](managedsettingsstore/gamecenter.md)
  Settings that affect Game Center.
- [struct GameCenterSettings](gamecentersettings.md)
  Constraints on the user’s Game Center settings.
- [var media: MediaSettings](managedsettingsstore/media.md)
  Settings that affect media.
- [struct MediaSettings](mediasettings.md)
  Constraints on the media content the user can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/appstoresettings)*