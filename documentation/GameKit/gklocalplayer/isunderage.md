# isUnderage

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the local player is underage.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isUnderage: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, getter=isUnderage) BOOL underage;
```

*macOS*

```objc
@property (atomic, readonly, getter=isUnderage) BOOL underage;
```

## Mentions

- [Authenticating a player](../authenticating-a-player.md)

#### Discussion

If this property is [`true`](../../Swift/true.md), Game Center disables some features for the local player. On all platforms, Game Center provides the value for the underage property for the Game Center account that the player signs into on the device. Note that the Game Center account defaults to the iCloud account that the player signs into on the device, but the player can sign into a different Game Center account.

## See Also

### Determining Whether the Player Is Underage or Restricted
- [var isMultiplayerGamingRestricted: Bool](./ismultiplayergamingrestricted.md)
  A Boolean value that indicates whether the player can join multiplayer games.
- [var isPersonalizedCommunicationRestricted: Bool](./ispersonalizedcommunicationrestricted.md)
  A Boolean value that indicates whether the player can use personalized communication on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/isunderage)*