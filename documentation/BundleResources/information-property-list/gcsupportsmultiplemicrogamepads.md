# GCSupportsMultipleMicroGamepads

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether the physical Apple TV Remote and the Apple TV Remote app operate as separate game controllers.

**Availability**:
- tvOS 9.0+

#### Discussion

If set to `YES`, your app supports multiple remotes with gamepads; otherwise, it doesn’t. If you support the 2nd Generation Siri Remote, set this key to `YES`. If you don’t set this key to `YES`, the combined micro gamepads won’t have the extra inputs of the 2nd Generation Siri Remote.

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
- [LSSupportsGameMode](information-property-list/lssupportsgamemode.md)
  A Boolean value indicating whether the app supports Game Mode.
- [GCSupportsGameMode](information-property-list/gcsupportsgamemode.md)
  A Boolean value indicating whether the app supports game mode.
- [GKShowChallengeBanners](information-property-list/gkshowchallengebanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/gcsupportsmultiplemicrogamepads)*