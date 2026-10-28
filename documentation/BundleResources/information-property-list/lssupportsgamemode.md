# LSSupportsGameMode

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether the app supports Game Mode.

**Availability**:
- iOS 18.6+
- iPadOS 18.6+
- macOS 26.0+

## Details

- **Name**: `LSSupportsGameMode` (Supports Game Mode)
- **Type**: boolean

## Discussion

Game Mode turns on automatically when you launch a game, and minimizes background activity for smoother gameplay and more consistent frame rates. Set this key to `YES` to make Game Mode available when your app is running. For games that aren’t resource intensive enough to benefit from Game Mode, set this key to `NO` to turn off Game Mode for your app.

> ❗ **Important**: If you don’t include this key in your `Info.plist`, Game Mode might not turn on for your game.

## See Also

### Games
- [AVGameBypassSystemSpatialAudio](./avgamebypasssystemspatialaudio.md)
  A key that ignores the system spatial-audio toggle in Control Center.
- [GKGameCenterBadgingDisabled](./gkgamecenterbadgingdisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.
- [GCDisableInferringGameMetadata](./gcdisableinferringgamemetadata.md)
  A Boolean value that indicates whether the Games app excludes game information for non-App Store games.
- [GCSupportedGameControllers](./gcsupportedgamecontrollers.md)
  The types of game controller profiles that the app supports or requires.
- [GCSupportsControllerUserInteraction](./gcsupportscontrolleruserinteraction.md)
  A Boolean value indicating whether the app supports a game controller.
- [GCRequiresControllerUserInteraction](./gcrequirescontrolleruserinteraction.md)
  The platforms for which your app requires or you recommend a game controller.
- [GCSupportsMultipleMicroGamepads](./gcsupportsmultiplemicrogamepads.md)
  A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [GCSupportsGameMode](./gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.
- [GKShowChallengeBanners](./gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/lssupportsgamemode)*