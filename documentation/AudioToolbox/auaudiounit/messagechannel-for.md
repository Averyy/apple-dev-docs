# messageChannel(for:)

**Framework**: Audio Toolbox  
**Kind**: method

Returns an object for bidirectional communication between an audio unit and its host.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func messageChannel(for channelName: String) -> any AUMessageChannel
```

#### Return Value

An object that conforms to [`AUMessageChannel`](aumessagechannel.md).

#### Discussion

Message channels provide a way for custom data exchanges between an audio unit and its host. An audio unit may support multiple message channels.

The host manages the message channel object’s lifetime. Design message channel objects so they can outlive the audio unit that vended them.

## Parameters

- `channelName`: The name of the message channel the audio unit returns.

## See Also

- [protocol AUMessageChannel](aumessagechannel.md)
  A specification for a bidirectional communication message channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/messagechannel(for:))*