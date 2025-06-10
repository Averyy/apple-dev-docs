# GCRequiresControllerUserInteraction

**Framework**: Bundle Resources  
**Kind**: dictionary

The platforms for which your app requires or you recommend a game controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- visionOS 1.0+

#### Discussion

Add this key to your information property list if your app requires a game controller in visionOS or to recommend a game controller in iOS. Adding this key requires you to enable the Game Controllers capability in Xcode and ExtendedGamepad under the Game Controllers capability. Xcode sets the value of [`GCSupportsControllerUserInteraction`](information-property-list/gcsupportscontrolleruserinteraction.md) to `YES` and includes an entry in the [`GCSupportedGameControllers`](information-property-list/gcsupportedgamecontrollers.md) dictionary with ProfileName set to ExtendedGamepad.

If your app requires a game controller for input in visionOS, add [`visionOS`](information-property-list/gcrequirescontrolleruserinteraction/visionos.md) to the [`GCRequiresControllerUserInteraction`](information-property-list/gcrequirescontrolleruserinteraction.md) dictionary and set the value to `YES`. If the value is `YES`, the App Store adds a Controller Required badge to your app.

To recommend a game controller in iOS, add [`iOS`](information-property-list/gcrequirescontrolleruserinteraction/ios.md) to the dictionary and set the value to `YES`. If the value is `YES`, the App Store adds a Controller Recommended badge to your app.

For apps built for visionOS, use only a [`visionOS`](information-property-list/gcrequirescontrolleruserinteraction/visionos.md) platform key in the dictionary. For iOS apps, you can include [`iOS`](information-property-list/gcrequirescontrolleruserinteraction/ios.md) or [`visionOS`](information-property-list/gcrequirescontrolleruserinteraction/visionos.md) platform keys to indicate behavior in iOS or a compatible iPad or iPhone app running in visionOS.

> ❗ **Important**:  If your app doesn’t provide an alternate to the game controller for input in visionOS then you need to include an entry in the [`GCRequiresControllerUserInteraction`](information-property-list/gcrequirescontrolleruserinteraction.md) dictionary and set the value to `YES`.

## Topics

### Platforms
- [iOS](information-property-list/gcrequirescontrolleruserinteraction/ios.md)
  A Boolean value you use to indicate that a game controller is recommended on iOS.
- [visionOS](information-property-list/gcrequirescontrolleruserinteraction/visionos.md)
  A Boolean value you use to indicate that a game controller is required on visionOS.

## See Also

- [AVGameBypassSystemSpatialAudio](information-property-list/avgamebypasssystemspatialaudio.md)
  A key that ignores the system spatial-audio toggle in Control Center.
- [GKGameCenterBadgingDisabled](information-property-list/gkgamecenterbadgingdisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.
- [GKShowChallengeBanners](information-property-list/gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.
- [GCSupportedGameControllers](information-property-list/gcsupportedgamecontrollers.md)
  The types of game controller profiles that the app supports or requires.
- [GCSupportsControllerUserInteraction](information-property-list/gcsupportscontrolleruserinteraction.md)
  A Boolean value indicating whether the app supports a game controller.
- [GCSupportsMultipleMicroGamepads](information-property-list/gcsupportsmultiplemicrogamepads.md)
  A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [LSSupportsGameMode](information-property-list/lssupportsgamemode.md)
  A Boolean value indicating whether the app supports Game Mode.
- [GCSupportsGameMode](information-property-list/gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/gcrequirescontrolleruserinteraction)*