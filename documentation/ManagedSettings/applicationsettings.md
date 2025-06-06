# ApplicationSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints on the apps and categories of apps a user can run on their device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct ApplicationSettings
```

## Topics

### Blocking Applications
- [var blockedApplications: Set<Application>?](applicationsettings/blockedapplications-swift.property.md)
  A set of applications for the system to block.
- [static let blockedApplications: SettingMetadata<Set<Application>>](applicationsettings/blockedapplications-swift.type.property.md)
  A description of the setting that controls which apps a user can launch on their device.
### Preventing App Installation and Removal
- [var denyAppInstallation: Bool?](applicationsettings/denyappinstallation-swift.property.md)
  A Boolean value that indicates whether to prevent the user from installing applications.
- [static let denyAppInstallation: SettingMetadata<Bool>](applicationsettings/denyappinstallation-swift.type.property.md)
  The metadata for the setting to prevent app installation.
- [var denyAppRemoval: Bool?](applicationsettings/denyappremoval-swift.property.md)
  A Boolean value that indicates whether to prevent the user from removing applications.
- [static let denyAppRemoval: SettingMetadata<Bool>](applicationsettings/denyappremoval-swift.type.property.md)
  The metadata for the setting to prevent app removal.

## Relationships

### Conforms To
- [ManagedSettingsGroup](managedsettingsgroup.md)

## See Also

- [var appStore: AppStoreSettings](managedsettingsstore/appstore.md)
  Settings that affect the App Store.
- [struct AppStoreSettings](appstoresettings.md)
  Constraints on a user’s App Store settings.
- [var application: ApplicationSettings](managedsettingsstore/application.md)
  Settings that affect applications.
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

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/applicationsettings)*