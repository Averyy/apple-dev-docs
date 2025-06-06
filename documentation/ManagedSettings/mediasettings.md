# MediaSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints on the media content the user can access.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct MediaSettings
```

## Topics

### Limiting Movie and TV Show Ratings
- [var maximumMovieRating: Int?](mediasettings/maximummovierating-swift.property.md)
  The maximum movie rating the user may view.
- [var maximumTVShowRating: Int?](mediasettings/maximumtvshowrating-swift.property.md)
  The maximum TV show rating that the user may view.
- [static let maximumMovieRating: BoundedSettingMetadata<Int>](mediasettings/maximummovierating-swift.type.property.md)
  The metadata for the setting that controls the maximum movie rating.
- [static let maximumTVShowRating: BoundedSettingMetadata<Int>](mediasettings/maximumtvshowrating-swift.type.property.md)
  The metadata for the setting that controls the maximum TV show rating.
### Denying Explicit Media
- [var denyExplicitContent: Bool?](mediasettings/denyexplicitcontent-swift.property.md)
  A Boolean value that indicates whether to prevent the user from accessing explicit content.
- [static let denyExplicitContent: SettingMetadata<Bool>](mediasettings/denyexplicitcontent-swift.type.property.md)
  The metadata for the setting that denies explicit content.
### Denying the Apple Music Service
- [var denyMusicService: Bool?](mediasettings/denymusicservice-swift.property.md)
  A Boolean value that indicates whether to prevent the user from accessing Apple Music’s streaming content.
- [static let denyMusicService: SettingMetadata<Bool>](mediasettings/denymusicservice-swift.type.property.md)
  The metadata associated with denying access to Apple Music.
### Constraining Content in the Books App
- [var denyBookstoreErotica: Bool?](mediasettings/denybookstoreerotica-swift.property.md)
  A Boolean value that indicates whether to deny media categorized as erotica in the Books store.
- [static let denyBookstoreErotica: SettingMetadata<Bool>](mediasettings/denybookstoreerotica-swift.type.property.md)
  The metadata associated with the setting that denies access to content in the Books store categorized as erotica.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/mediasettings)*