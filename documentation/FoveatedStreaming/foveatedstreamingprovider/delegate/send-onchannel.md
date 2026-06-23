# send(_:onChannel:)

**Framework**: Foveated Streaming  
**Kind**: method  
**Required**: Yes

Sends data on an open message channel.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func send(_ data: Data, onChannel channelID: FoveatedStreamingSession.MessageChannel.ID) throws
```

## Parameters

- `data`: The data to send.
- `channelID`: The identifier of the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/delegate/send(_:onchannel:))*