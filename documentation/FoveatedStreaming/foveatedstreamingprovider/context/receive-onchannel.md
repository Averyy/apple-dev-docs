# receive(_:onChannel:)

**Framework**: Foveated Streaming  
**Kind**: method

Notifies the host app that a message channel received data.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func receive(_ data: Data, onChannel channelID: FoveatedStreamingSession.MessageChannel.ID)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/context/receive(_:onchannel:))*