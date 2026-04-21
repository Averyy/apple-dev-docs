# GCSupportedGameControllers

**Framework**: Bundle Resources  
**Kind**: dictionary

The types of game controller profiles that the app supports or requires.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+



**Type**: dictionary 

#### Discussion

The dictionary keys are `ProfileName` and the possible game controller values are:

- **`ExtendedGamepad`**: The extended set of gamepad controls. See [`GCExtendedGamepad`](https://developer.apple.com/documentation/GameController/GCExtendedGamepad).
- **`SpatialGamepad`**: The set of spatial gamepad controls.
- **`MicroGamepad`**: The 1st Generation Siri Remote. See [`GCMicroGamepad`](https://developer.apple.com/documentation/GameController/GCMicroGamepad).
- **`DirectionalGamepad`**: The 2nd Generation Siri Remote. A directional pad without motion or rotation. See [`GCDirectionalGamepad`](https://developer.apple.com/documentation/GameController/GCDirectionalGamepad). Available in iOS 14.3+, macOS 11.1+, Mac Catalyst 14.3+, and tvOS 14.3+.

## Properties

- `ProfileName` (string)

## See Also

- [AVGameBypassSystemSpatialAudio](information-property-list/avgamebypasssystemspatialaudio.md)
  A key that ignores the system spatial-audio toggle in Control Center.
- [GKGameCenterBadgingDisabled](information-property-list/gkgamecenterbadgingdisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.
- [GCDisableInferringGameMetadata](information-property-list/gcdisableinferringgamemetadata.md)
  A Boolean value that indicates whether the Games app excludes game information for non-App Store games.
- [GCSupportsControllerUserInteraction](information-property-list/gcsupportscontrolleruserinteraction.md)
  A Boolean value indicating whether the app supports a game controller.
- [GCRequiresControllerUserInteraction](information-property-list/gcrequirescontrolleruserinteraction.md)
  The platforms for which your app requires or you recommend a game controller.
- [GCSupportsMultipleMicroGamepads](information-property-list/gcsupportsmultiplemicrogamepads.md)
  A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.
- [LSSupportsGameMode](information-property-list/lssupportsgamemode.md)
  A Boolean value indicating whether the app supports Game Mode.
- [GCSupportsGameMode](information-property-list/gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.
- [GKShowChallengeBanners](information-property-list/gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/gcsupportedgamecontrollers)*