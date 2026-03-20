# messageChannel(for:)

**Framework**: Foveated Streaming  
**Kind**: method

Creates or retrieves a message channel for the given message channel ID.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
final func messageChannel(for channelID: FoveatedStreamingSession.MessageChannel.ID) -> FoveatedStreamingSession.MessageChannel?
```

#### Return Value

The requested message channel if the session is connected and the channel ID is valid, otherwise `nil`.

#### Discussion

If a channel with the given ID already exists, returns the existing channel. Otherwise, creates a new channel and opens it asynchronously.

## Parameters

- `channelID`: The ID of the requested message channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/messagechannel(for:))*