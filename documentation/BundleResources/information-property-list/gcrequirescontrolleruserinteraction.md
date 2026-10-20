# GCRequiresControllerUserInteraction

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The platforms for which your app requires or you recommend a game controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- visionOS 1.0+

## Details

- **Name**: `GCRequiresControllerUserInteraction`
- **Type**: dictionary

#### Discussion

Add this key to your information property list if your app requires a game controller in visionOS or to recommend a game controller in iOS. Adding this key requires you to enable the Game Controllers capability in Xcode and ExtendedGamepad under the Game Controllers capability. Xcode sets the value of [`GCSupportsControllerUserInteraction`](./gcsupportscontrolleruserinteraction.md) to `YES` and includes an entry in the [`GCSupportedGameControllers`](./gcsupportedgamecontrollers.md) dictionary with ProfileName set to ExtendedGamepad.

If your app requires a game controller for input in visionOS, add [`visionOS`](./gcrequirescontrolleruserinteraction/visionos.md) to the [`GCRequiresControllerUserInteraction`](./gcrequirescontrolleruserinteraction.md) dictionary and set the value to `YES`. If the value is `YES`, the App Store adds a Controller Required badge to your app.

To recommend a game controller in iOS, add [`iOS`](./gcrequirescontrolleruserinteraction/ios.md) to the dictionary and set the value to `YES`. If the value is `YES`, the App Store adds a Controller Recommended badge to your app.

For apps built for visionOS, use only a [`visionOS`](./gcrequirescontrolleruserinteraction/visionos.md) platform key in the dictionary. For iOS apps, you can include [`iOS`](./gcrequirescontrolleruserinteraction/ios.md) or [`visionOS`](./gcrequirescontrolleruserinteraction/visionos.md) platform keys to indicate behavior in iOS or a compatible iPad or iPhone app running in visionOS.

> ❗ **Important**:  If your app doesn’t provide an alternate to the game controller for input in visionOS then you need to include an entry in the [`GCRequiresControllerUserInteraction`](./gcrequirescontrolleruserinteraction.md) dictionary and set the value to `YES`.

## Topics

### Platforms
- [iOS](./gcrequirescontrolleruserinteraction/ios.md)
  A Boolean value you use to indicate that a game controller is recommended on iOS.
- [visionOS](./gcrequirescontrolleruserinteraction/visionos.md)
  A Boolean value you use to indicate that a game controller is required on visionOS.

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
- [GCSupportsMultipleMicroGamepads](./gcsupportsmultiplemicrogamepads.md)
  A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [LSSupportsGameMode](./lssupportsgamemode.md)
  A Boolean value indicating whether the app supports Game Mode.
- [GCSupportsGameMode](./gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.
- [GKShowChallengeBanners](./gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/gcrequirescontrolleruserinteraction)*