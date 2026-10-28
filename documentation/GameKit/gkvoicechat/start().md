# start()

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Starts communication with other players in a channel.

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
func start()
```

```objc
- (void) start;
```

## Mentions

- [Adding voice chat to multiplayer games](../adding-voice-chat-to-multiplayer-games.md)

## Discussion

You must provide a reason, by adding the [`NSMicrophoneUsageDescription`](../../BundleResources/information-property-list/nsmicrophoneusagedescription.md) key to the Information Property List, to start voice chat with other players.

If the player grants permission to use the microphone and this method successfully connects to the channel, GameKit plays voice data from the other players automatically. Use the [`isActive`](./isactive.md) property to begin sending the local player’s microphone data to the channel.

A player can only start voice chat if their device has a microphone and they connect to Wi-Fi.

## See Also

### Starting and Stopping Voice Chat
- [func stop()](./stop%28%29.md)
  Ends communication with other players in a channel.
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the channel is sampling the microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/start())*