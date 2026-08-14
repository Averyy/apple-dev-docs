# isActive

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether the channel is sampling the microphone.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get set }
```

## Mentions

- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)

#### Discussion

If you set this property to [`true`](https://developer.apple.com/documentation/swift/true), the voice chat object transmits the voice data from the microphone to other players in the channel. If another voice chat object is using the microphone, GameKit switches the microphone to this channel and sets that voice chat object’s [`isActive`](gkvoicechat/isactive.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func start()](gkvoicechat/start.md)
  Starts communication with other players in a channel.
- [func stop()](gkvoicechat/stop.md)
  Ends communication with other players in a channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/isactive)*