# stop()

**Framework**: GameKit  
**Kind**: method

Ends communication with other players in a channel.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func stop()
```

## Mentions

- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)

#### Discussion

This method disconnects the player from the channel. You should call `stop()` before you set the voice chat object to `nil`.

## See Also

- [var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void](gkvoicechat/playerstateupdatehandler.md)
  Handles when a player in the chat changes state.
- [func start()](gkvoicechat/start.md)
  Starts communication with other players in a channel.
- [var isActive: Bool](gkvoicechat/isactive.md)
  A Boolean value that indicates whether the channel is sampling the microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/stop())*