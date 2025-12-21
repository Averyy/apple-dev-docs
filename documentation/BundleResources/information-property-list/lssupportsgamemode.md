# LSSupportsGameMode

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether the app supports Game Mode.

**Availability**:
- iOS 18.6+
- iPadOS 18.6+
- macOS 26.0+

#### Discussion

Game Mode turns on automatically when you launch a game, and minimizes background activity for smoother gameplay and more consistent frame rates. Set this key to `YES` to make Game Mode available when your app is running. For games that aren’t resource intensive enough to benefit from Game Mode, set this key to `NO` to turn off Game Mode for your app.

> ❗ **Important**: If you don’t include this key in your `Info.plist`, Game Mode might not turn on for your game.

## See Also

- [AVGameBypassSystemSpatialAudio](information-property-list/avgamebypasssystemspatialaudio.md)
  A key that ignores the system spatial-audio toggle in Control Center.
- [GKGameCenterBadgingDisabled](information-property-list/gkgamecenterbadgingdisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.
- [GCSupportedGameControllers](information-property-list/gcsupportedgamecontrollers.md)
  The types of game controller profiles that the app supports or requires.
- [GCSupportsControllerUserInteraction](information-property-list/gcsupportscontrolleruserinteraction.md)
  A Boolean value indicating whether the app supports a game controller.
- [GCRequiresControllerUserInteraction](information-property-list/gcrequirescontrolleruserinteraction.md)
  The platforms for which your app requires or you recommend a game controller.
- [GCSupportsMultipleMicroGamepads](information-property-list/gcsupportsmultiplemicrogamepads.md)
  A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [GCSupportsGameMode](information-property-list/gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.
- [GKShowChallengeBanners](information-property-list/gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/lssupportsgamemode)*