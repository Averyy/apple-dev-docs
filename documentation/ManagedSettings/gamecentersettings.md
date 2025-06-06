# GameCenterSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints on the user’s Game Center settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct GameCenterSettings
```

#### Overview

Use `GameCenterSettings` to prevent the user from changing Game Center’s settings for adding friends and joining multiplayer games.

## Topics

### Denying the Ability to Join Multiplayer Games
- [var denyMultiplayerGaming: Bool?](gamecentersettings/denymultiplayergaming-swift.property.md)
  A Boolean value that indicates whether your app prevents the user joining multiplayer games.
- [static let denyMultiplayerGaming: SettingMetadata<Bool>](gamecentersettings/denymultiplayergaming-swift.type.property.md)
  The metadata associated with the setting that prevents users from joining multiplayer games.
### Denying the Ability to Add Friends
- [var denyAddingFriends: Bool?](gamecentersettings/denyaddingfriends-swift.property.md)
  A Boolean value that indicates whether to prevent the user from adding Game Center friends.
- [static let denyAddingFriends: SettingMetadata<Bool>](gamecentersettings/denyaddingfriends-swift.type.property.md)
  The metadata for the setting that prevents the user from adding friends in Game Center.

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
- [var media: MediaSettings](managedsettingsstore/media.md)
  Settings that affect media.
- [struct MediaSettings](mediasettings.md)
  Constraints on the media content the user can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/gamecentersettings)*