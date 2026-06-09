# sendDataOnChannel(channelId:data:)

**Framework**: Foveated Streaming  
**Kind**: method  
**Required**: Yes

Sends data on an open message channel.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func sendDataOnChannel(channelId: String, data: Data) throws
```

## Parameters

- `channelId`: The string identifier of the channel.
- `data`: The data to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/senddataonchannel(channelid:data:))*