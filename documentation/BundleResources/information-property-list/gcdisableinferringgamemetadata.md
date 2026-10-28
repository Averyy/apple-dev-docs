# GCDisableInferringGameMetadata

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the Games app excludes game information for non-App Store games.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- macOS 26.4+

## Details

- **Name**: `GCDisableInferringGameMetadata` (Opt out of inferring game knowledge in Games App)
- **Type**: boolean

## Discussion

For games distributed outside of the App Store, the Games app infers game details by using Siri’s knowledge graph. Set this key to `YES` to opt-out of that behavior and remove those details from your game detail page in the Games app.

## See Also

### Games
- [AVGameBypassSystemSpatialAudio](./avgamebypasssystemspatialaudio.md)
  A key that ignores the system spatial-audio toggle in Control Center.
- [GKGameCenterBadgingDisabled](./gkgamecenterbadgingdisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.
- [GCSupportedGameControllers](./gcsupportedgamecontrollers.md)
  The types of game controller profiles that the app supports or requires.
- [GCSupportsControllerUserInteraction](./gcsupportscontrolleruserinteraction.md)
  A Boolean value indicating whether the app supports a game controller.
- [GCRequiresControllerUserInteraction](./gcrequirescontrolleruserinteraction.md)
  The platforms for which your app requires or you recommend a game controller.
- [GCSupportsMultipleMicroGamepads](./gcsupportsmultiplemicrogamepads.md)
  A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [LSSupportsGameMode](./lssupportsgamemode.md)
  A Boolean value indicating whether the app supports Game Mode.
- [GCSupportsGameMode](./gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.
- [GKShowChallengeBanners](./gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/gcdisableinferringgamemetadata)*