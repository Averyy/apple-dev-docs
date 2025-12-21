# isMultiplayerGamingRestricted

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether the player can join multiplayer games.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var isMultiplayerGamingRestricted: Bool { get }
```

## Mentions

- [Authenticating a player](authenticating-a-player.md)

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/Swift/true), the local player can’t join multiplayer games. If your game uses a custom multiplayer feature, you should disable it.

On iOS and macOS, the value for this property comes from the Screen Time settings that the system syncs between devices using the same iCloud account. A person can configure multiplayer games to allow playing with everyone, allow with friends only, or prevent multiplayer games with everyone. The `isMultiplayerGamingRestricted` property reflects whether there are  restrictions. For example, when you configure the setting to friends only, this property returns `true` for restricted. To change this value when testing your game, see [`Restrict Game Center section of Use parental controls on your child’s iPhone, iPad, and iPod touch`](https://developer.apple.comhttps://support.apple.com/en-us/HT201304) and [`Change Content Restrictions settings in Screen Time on Mac`](https://developer.apple.comhttps://support.apple.com/guide/mac-help/change-content-restrictions-settings-screen-mchlbcf0dfe2/mac).

On tvOS, players set this value on the device using the Restrictions menu. This setting is local only; the system doesn’t sync this setting to other devices. To change this value when testing your game, see [`Restrict access to content on Apple TV`](https://developer.apple.comhttps://support.apple.com/guide/tv/restrict-access-to-content-atvbbaf126df/tvos).

## See Also

- [var isUnderage: Bool](gklocalplayer/isunderage.md)
  A Boolean value that indicates whether the local player is underage.
- [var isPersonalizedCommunicationRestricted: Bool](gklocalplayer/ispersonalizedcommunicationrestricted.md)
  A Boolean value that indicates whether the player can use personalized communication on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/ismultiplayergamingrestricted)*