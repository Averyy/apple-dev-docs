# isPersonalizedCommunicationRestricted

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player can use personalized communication on the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isPersonalizedCommunicationRestricted: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPersonalizedCommunicationRestricted) BOOL personalizedCommunicationRestricted;
```

## Mentions

- [Authenticating a player](../authenticating-a-player.md)

#### Discussion

If this property or the underage property is [`true`](../../Swift/true.md), the local player can’t include personalized messages on invitations or enable voice communication in multiplayer games. If your game includes any custom communication features, you should disable them.

On iOS and macOS, the value for this property comes from the Screen Time settings that the system syncs between devices using the same iCloud account. To change this value when testing your game, see [Restrict Game Center section of Use parental controls on your child’s iPhone, iPad, and iPod touch](https://support.apple.com/en-us/HT201304) and [Change Content Restrictions settings in Screen Time on Mac](https://support.apple.com/guide/mac-help/change-content-restrictions-settings-screen-mchlbcf0dfe2/mac).

On tvOS, players set this value on the device using the Restrictions menu. This setting is local only; the system doesn’t sync this setting to other devices. To change this value when testing your game, see [Restrict access to content on Apple TV](https://support.apple.com/guide/tv/restrict-access-to-content-atvbbaf126df/tvos).

## See Also

### Determining Whether the Player Is Underage or Restricted
- [var isUnderage: Bool](./isunderage.md)
  A Boolean value that indicates whether the local player is underage.
- [var isMultiplayerGamingRestricted: Bool](./ismultiplayergamingrestricted.md)
  A Boolean value that indicates whether the player can join multiplayer games.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/ispersonalizedcommunicationrestricted)*