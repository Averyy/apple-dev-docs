# start()

**Framework**: GameKit  
**Kind**: method

Starts communication with other players in a channel.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func start()
```

## Mentions

- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)

#### Discussion

You must provide a reason, by adding the [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) key to the Information Property List, to start voice chat with other players.

If the player grants permission to use the microphone and this method successfully connects to the channel, GameKit plays voice data from the other players automatically. Use the [`isActive`](gkvoicechat/isactive.md) property to begin sending the local player’s microphone data to the channel.

A player can only start voice chat if their device has a microphone and they connect to Wi-Fi.

## See Also

- [func stop()](gkvoicechat/stop.md)
  Ends communication with other players in a channel.
- [var isActive: Bool](gkvoicechat/isactive.md)
  A Boolean value that indicates whether the channel is sampling the microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/start())*