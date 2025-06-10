# GCSupportsControllerUserInteraction

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether the app supports a game controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

#### Discussion

To add this key to the information property list, enable the Game Controllers capability in Xcode. If you set this key to `YES` and check ExtendedGamepad under the Game Controllers capability in your project, App Store adds a game controller support badge to your app. Then users can customize their game controller mappings in Settings and Preferences.

> ❗ **Important**:  To recommend the use of a game controller on iOS or if your app requires a game controller on visionOS, add an entry into the [`GCRequiresControllerUserInteraction`](information-property-list/gcrequirescontrolleruserinteraction.md) dictionary for that platform and set the value to `YES`.

## See Also

- [AVGameBypassSystemSpatialAudio](information-property-list/avgamebypasssystemspatialaudio.md)
  A key that ignores the system spatial-audio toggle in Control Center.
- [GKGameCenterBadgingDisabled](information-property-list/gkgamecenterbadgingdisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.
- [GKShowChallengeBanners](information-property-list/gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.
- [GCSupportedGameControllers](information-property-list/gcsupportedgamecontrollers.md)
  The types of game controller profiles that the app supports or requires.
- [GCRequiresControllerUserInteraction](information-property-list/gcrequirescontrolleruserinteraction.md)
  The platforms for which your app requires or you recommend a game controller.
- [GCSupportsMultipleMicroGamepads](information-property-list/gcsupportsmultiplemicrogamepads.md)
  A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [LSSupportsGameMode](information-property-list/lssupportsgamemode.md)
  A Boolean value indicating whether the app supports Game Mode.
- [GCSupportsGameMode](information-property-list/gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/gcsupportscontrolleruserinteraction)*