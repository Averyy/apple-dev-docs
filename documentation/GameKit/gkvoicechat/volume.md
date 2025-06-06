# volume

**Framework**: GameKit  
**Kind**: property

The volume level for the channel.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var volume: Float { get set }
```

## Mentions

- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)

#### Discussion

GameKit mixes voice data received from all other players and scales it by the `volume` property. The `volume` property has a range between `0.0` and `1.0`, inclusive. To mute the entire channel, set the volume to `0.0`. To play the voice data at full volume, set the volume to `1.0`. The default value is `1.0`.

## See Also

- [func setPlayer(GKPlayer, muted: Bool)](gkvoicechat/setplayer(_:muted:).md)
  Mutes a player in the chat, including the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/volume)*