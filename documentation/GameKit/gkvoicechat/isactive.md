# isActive

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the channel is sampling the microphone.

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
var isActive: Bool { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, getter=isActive) BOOL active;
```

*macOS*

```objc
@property (atomic, assign, getter=isActive) BOOL active;
```

## Mentions

- [Adding voice chat to multiplayer games](../adding-voice-chat-to-multiplayer-games.md)

#### Discussion

If you set this property to [`true`](../../Swift/true.md), the voice chat object transmits the voice data from the microphone to other players in the channel. If another voice chat object is using the microphone, GameKit switches the microphone to this channel and sets that voice chat object’s [`isActive`](./isactive.md) property to [`false`](../../Swift/false.md).

The default value for this property is [`false`](../../Swift/false.md).

## See Also

### Starting and Stopping Voice Chat
- [func start()](./start%28%29.md)
  Starts communication with other players in a channel.
- [func stop()](./stop%28%29.md)
  Ends communication with other players in a channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechat/isactive)*