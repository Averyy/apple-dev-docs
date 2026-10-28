# stop()

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Ends communication with other players in a channel.

**Availability**:
- iOS 4.1+ - Deprecated in 18.0
- iPadOS 4.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported

## Declaration

```swift
func stop()
```

```objc
- (void) stop;
```

## Mentions

- [Adding voice chat to multiplayer games](../adding-voice-chat-to-multiplayer-games.md)

## Discussion

This method disconnects the player from the channel. You should call `stop()` before you set the voice chat object to `nil`.

## See Also

### Related Documentation
- [var playerStateUpdateHandler: (String, GKVoiceChat.PlayerState) -> Void](./playerstateupdatehandler.md)
  Handles when a player in the chat changes state.
### Starting and Stopping Voice Chat
- [func start()](./start%28%29.md)
  Starts communication with other players in a channel.
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the channel is sampling the microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/stop())*